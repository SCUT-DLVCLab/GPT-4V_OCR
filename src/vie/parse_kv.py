# encoding: utf-8
import argparse
import json
import re
from typing import Dict, List, Tuple, Union

import numpy as np
import tqdm

from src.common.string_utils import string_f2h

SEPARATOR_LIST = ["->", ":", "-"]  # should be ordered
BRACKET_MAP = {
    ")": "(",
    "]": "[",
    "}": "{",
}
BRACKET_LIST = list(set(BRACKET_MAP.keys()) | set(BRACKET_MAP.values()))

SELECTED_SYMBOLS = ["checked", "selected", "(x)", "[x]", "✓", ": x", ":x"]

UNSELECTED_CHILD = [
    "unchecked",
    "unselected",
]


def calculate_edit_distance(str1: str, str2: str) -> int:
    if str1 == str2:
        return 0

    wl_1 = len(str1)
    wl_2 = len(str2)

    if wl_1 == 0 or wl_2 == 0:
        return max(wl_1, wl_2)

    v1, v2 = [], []
    for i in range(wl_2 + 1):
        v1.append(i), v2.append(i + 1)

    for i in range(1, wl_1 + 1):
        for j in range(1, wl_2 + 1):
            if str1[i - 1] == str2[j - 1]:
                d = 0

            else:
                d = 1

            minValue = min(
                v1[j] + 1,
                v1[j - 1] + d,
                v2[j - 1] + 1,
            )

            v2[j] = minValue

        for j in range(wl_2 + 1):
            v1[j] = v2[j]
            v2[j] = i + 1

    return float(v1[-1]) / max(len(str1), len(str2))


def parse_dummy_json(dir_orig: str) -> Dict[str, List[str]]:
    """parse the raw output of GPT-4V,
    each sample will be parsed into a list of line strings,
    indent of each line is kept for further processing

    Parameters
    ----------
    dir_orig : str
        Path to the original output

    """
    parsed_dict: Dict[str, List[str]] = {}

    dummy_lines: List[str]
    with open(dir_orig, "r", encoding="utf-8") as f:
        dummy_lines = f.readlines()

    bracket_stash: List[str] = []
    sample_lines: List[str] = []
    indent_list = []
    sample_id: int = None
    prev_line = None
    for dummy_line in dummy_lines:
        dummy_indent = len(dummy_line) - len(dummy_line.lstrip())
        dummy_line = string_f2h(dummy_line.strip())
        if dummy_line in BRACKET_LIST or dummy_line.replace(",", "") in BRACKET_LIST:
            # start/end line of each json block
            dummy_line = dummy_line.replace(",", "")
            if (
                len(bracket_stash) > 0
                and BRACKET_MAP.get(dummy_line, None) == bracket_stash[-1]
            ):
                bracket_stash.pop(-1)
                assert (
                    sample_id not in parsed_dict.keys()
                ), f"Duplicate sample id: {sample_id}"
                if len(sample_lines) > 0 and sample_lines[-1].endswith('"'):
                    sample_lines[-1] = sample_lines[-1][:-1]  # remove the last "

                if len(sample_lines) > 0:
                    min_indent = 100000
                    for idt in set(indent_list):
                        if idt == -1:
                            prev_line = dummy_line
                            continue
                        if idt < min_indent:
                            min_indent = idt
                    formatted_sample_lines = []
                    for line_indent, line_content in zip(indent_list, sample_lines):
                        if line_indent == -1:
                            formatted_sample_lines.append(line_content)
                        else:
                            formatted_sample_lines.append(
                                " " * (line_indent - min_indent) + line_content
                            )

                    parsed_dict[sample_id] = formatted_sample_lines
                    indent_list = []
                    sample_lines = []
                    sample_id = None
                prev_line = dummy_line
                continue
            elif dummy_line in BRACKET_MAP.values():
                bracket_stash.append(dummy_line)
                prev_line = dummy_line
                continue
            else:
                raise ValueError(f"Unknown bracket: {dummy_line}")
        elif (
            dummy_line.startswith('"')
            and re.match(r"\"[0-9]+\"", dummy_line) is not None
        ):
            # first line of each sample
            id_, content_ = dummy_line.split('": "')
            sample_id = int(id_.replace('"', ""))
            if "sure," or "here are" in content_.lower():
                # GPT's extra words
                pass
            else:
                sample_lines.append(content_)
                indent_list.append(-1)
            prev_line = dummy_line
        elif (
            ("note: " in dummy_line.lower() and prev_line == "")
            or ("that covers the content" in dummy_line.lower())
            or ("that's all the key-value pairs" in dummy_line.lower())
        ):
            # GPT's extra words, seems to be the last line of each sample
            prev_line = dummy_line
            continue
        elif dummy_line == "":
            prev_line = dummy_line
            continue
        else:
            # middle lines of each sample
            indent_list.append(dummy_indent)
            sample_lines.append(dummy_line)
            prev_line = dummy_line

    return parsed_dict


def parse_single_line(line: str) -> Union[List[Tuple[str, str]], None]:
    parsed_pairs = []
    processed = False

    for outer_separator in SEPARATOR_LIST:
        match_separators = re.findall(r"s?" + outer_separator + r"s?", line)
        if len(match_separators) == 1:
            key, value = line.split(outer_separator)
            key = key.replace("**", "").strip()
            value = value.replace("**", "").strip()
            parsed_pairs.append((key, value))
            processed = True
            break
        elif len(match_separators) > 1:
            if "," in line:
                # multiple pairs in one line
                curr_line_pairs = line.split(",")
                for pair in curr_line_pairs:
                    for inner_separator in SEPARATOR_LIST:
                        if inner_separator in pair:
                            key, value = pair.split(inner_separator, 1)
                            key = key.replace("**", "").strip()
                            value = value.replace("**", "").strip()
                            parsed_pairs.append((key, value))
                            break
                        else:
                            pass
            else:
                # hard cases, only use the first separator
                curr_line_pairs = line.split(outer_separator, 1)
                parsed_pairs.append((curr_line_pairs[0], curr_line_pairs[1]))

            processed = True
            break
        else:
            # no separator found
            pass

    if not processed:
        return None

    return parsed_pairs


def parse_single_file_content(content_lines: List[str]) -> List[Tuple[str, str]]:
    parsed_result = []
    father_line = None
    prev_indent = 0
    child_flag = False
    child_contents: List[str] = []
    for curr_line in content_lines:
        curr_indent = len(curr_line) - len(curr_line.lstrip())
        if curr_indent > prev_indent:
            # sub values
            child_flag = True
            child_contents.append(curr_line)
        elif curr_indent < prev_indent:
            # parse the child contents

            # identify the child type: selection boxes or sub-kv-pairs or group of values
            child_type = "group_value"
            for child_line in child_contents:
                child_line_ = child_line.strip()
                if child_line_.startswith("-"):
                    child_line_ = child_line_[1:].strip()
                for selected_symbol in SELECTED_SYMBOLS:
                    if (
                        selected_symbol in child_line_.lower()
                        or selected_symbol in child_line_.replace(" ", "").lower()
                    ):
                        child_type = "selection"
                        break

                if child_type == "selection":
                    break

                for split_symbol in SEPARATOR_LIST:
                    if split_symbol in child_line_:
                        child_type = "sub_pairs"
                        break
                if child_type == "sub_pairs":
                    break

            if child_type == "sub_pairs":
                for child_line in child_contents:
                    if re.match(r"[0-9]\.", child_line) is not None:
                        # start with number
                        child_line = child_line.split(".", 1)[-1].strip()
                    elif child_line.startswith("-"):
                        child_line = child_line[1:].strip()
                    else:
                        pass
                    line_pairs = parse_single_line(child_line)
                    if line_pairs is not None:
                        parsed_result.extend(line_pairs)
                    else:
                        # No separator found in child line
                        if len(child_contents) == 1:
                            # only one line, treat it as a value of the father line
                            parsed_result.append((father_line, child_line))
                        else:
                            pass
            elif child_type == "group_value":
                for child_line in child_contents:
                    child_line = child_line.strip()
                    if re.match(r"[0-9]\.", child_line) is not None:
                        # start with number
                        child_line = child_line.split(".", 1)[-1].strip()
                    elif child_line.startswith("-"):
                        child_line = child_line[1:].strip()
                    else:
                        pass
                    parsed_result.append((father_line, child_line))
            elif child_type == "selection":
                selected_child = None
                selected_found_flag = False
                for child_line in child_contents:
                    for selected_symbol in SELECTED_SYMBOLS:
                        if selected_symbol in child_line.replace(" ", "").lower():
                            fake_selected_flag = False
                            for unselected_symbol in UNSELECTED_CHILD:
                                if (
                                    unselected_symbol
                                    in child_line.replace(" ", "").lower()
                                ):
                                    fake_selected_flag = True
                                    break
                            if fake_selected_flag:
                                selected_found_flag = False
                                continue
                            else:
                                selected_found_flag = True
                                selected_child = child_line.strip()

                                if re.match(r"[0-9]\.", selected_child) is not None:
                                    # start with number
                                    selected_child = selected_child.split(".", 1)[
                                        -1
                                    ].strip()
                                elif selected_child.startswith("-"):
                                    selected_child = selected_child[1:].strip()

                                break
                    if selected_found_flag:
                        parsed_result.append((father_line, selected_child))
                        break
            else:
                pass

            child_flag = False
            child_contents = []

            # parse current line
            if re.match(r"[0-9]\.", curr_line) is not None:
                # start with number
                curr_line = curr_line.split(".", 1)[-1].strip()
                line_pairs = parse_single_line(curr_line)
            elif curr_line.startswith("-"):
                curr_line = curr_line[1:].strip()
                line_pairs = parse_single_line(curr_line)
            else:
                line_pairs = parse_single_line(curr_line)
            if line_pairs is not None:
                parsed_result.extend(line_pairs)
            else:
                pass
            father_line = curr_line
        else:
            if re.match(r"[0-9]+\.", curr_line) is not None:
                # start with number
                curr_line = curr_line.split(".", 1)[-1].strip()
                line_pairs = parse_single_line(curr_line)
            elif curr_line.startswith("-"):
                curr_line = curr_line[1:].strip()
                line_pairs = parse_single_line(curr_line)
            else:
                line_pairs = parse_single_line(curr_line)

            if child_flag:
                # sub values
                child_contents.append(curr_line)
            else:
                if line_pairs is not None:
                    parsed_result.extend(line_pairs)
                else:
                    pass
                father_line = curr_line

        prev_indent = curr_indent

    parsed_result_ = []
    for pairs in parsed_result:
        k, v = pairs
        if k.endswith(":"):
            k = k[:-1]

        if v.lower() == "[blank]" or v == "[空白]" or v == "":
            continue
        elif "_____" in v:
            # value is underline
            continue
        else:
            for selected_symbol in SELECTED_SYMBOLS:
                if selected_symbol in v.lower():
                    v_ = v.lower().replace("(" + selected_symbol + ")", "")
                    v_ = v_.lower().replace("[" + selected_symbol + "]", "")
                    v_ = v_.lower().replace(selected_symbol, "")
                    v = v[: len(v_)].strip()
                    if v.endswith(":"):
                        v = v[:-1]
                    break

            parsed_result_.append((k, v))

    return parsed_result_


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir_orig", type=str, help="Path to the original dummy.json")
    parser.add_argument(
        "--dir_gt_kv", type=str, help="Path to the ground truth kv.json"
    )
    parser.add_argument(
        "--dir_rename",
        type=str,
        help="Path to the ground truth kv_pairs.json",
        default="null",
    )
    args = parser.parse_args()

    # # ! For debugging ##
    # import dataclasses

    # @dataclasses.dataclass
    # class DebugArgs:
    #     dir_orig: str = "results/vie/private_XFUNDzh_res.json"
    #     dir_gt_kv: str = "private_eval/FUNSD/zh.val.kv.json"
    #     dir_rename: str = "private_eval/FUNSD/XFUNDzh_rename.txt"
    #     dir_orig: str = "results/vie/private_FUNSD_res.json"
    #     dir_gt_kv: str = "private_eval/FUNSD/en.val.kv.json"
    #     dir_rename: str = "private_eval/FUNSD/FUNSD_rename.txt"

    # args = DebugArgs()
    # # ! For debugging ##

    if args.dir_rename != "null":
        with open(args.dir_rename, "r", encoding="utf-8") as f:
            rename_lines = f.readlines()
            rename_maps = {}
            for rl in rename_lines:
                new, orig = rl.strip().split(" ")
                rename_maps[new] = orig
    else:
        rename_maps = None

    gt_kv_map = json.load(open(args.dir_gt_kv, "r", encoding="utf-8"))

    pred_dict = parse_dummy_json(args.dir_orig)

    num_TP, num_pred, num_gt = 0.0, 0.0, 0.0
    total_ed = 0.0
    total_ed_cnt = 0.0
    for renamed_file_id, file_content in tqdm.tqdm(pred_dict.items()):
        if rename_maps is not None:
            orig_file_id = rename_maps[str(renamed_file_id)]
        else:
            orig_file_id = renamed_file_id
        pred_kvs = parse_single_file_content(file_content)
        gt_kvs = gt_kv_map[orig_file_id]
        gt_kvs_ = []
        for gt_kv in gt_kvs:
            k, v = gt_kv
            k = k.replace("\u2611", "").strip()
            v = v.replace("\u2611", "").strip()
            if k.endswith(":"):
                k = k[:-1]

            if v.endswith(" X"):
                v = v[:-2]

            gt_kvs_.append((k, v))
        gt_kvs = gt_kvs_

        num_pred += len(pred_kvs)
        num_gt += len(gt_kvs)

        # calculate F1
        for pred_kv in pred_kvs:
            if pred_kv in gt_kvs:
                num_TP += 1

        matched_pred = []
        for i, gt_kv in enumerate(gt_kvs):
            gt_ed_score_list = []
            gt_pred_idx_list = []
            for j, pred_kv in enumerate(pred_kvs):
                if j in matched_pred:
                    continue

                pred_k, pred_v = pred_kv
                gt_k, gt_v = gt_kv

                ed = calculate_edit_distance(pred_k + pred_v, gt_k + gt_v)

                gt_ed_score_list.append(int(ed * 1000))
                gt_pred_idx_list.append(j)

            if len(gt_ed_score_list) == 0:
                break

            match_pred_idx = gt_pred_idx_list[np.argmin(gt_ed_score_list)]
            matched_pred.append(match_pred_idx)
            match_ed = np.min(gt_ed_score_list) / 1000.0
            total_ed += match_ed

        if len(pred_kvs) > len(gt_kvs):
            total_ed += len(pred_kvs) - len(gt_kvs)
        else:
            total_ed += len(gt_kvs) - len(pred_kvs)

        total_ed_cnt += max(len(pred_kvs), len(gt_kvs))

    precision = num_TP / num_pred if num_pred > 0 else 0
    recall = num_TP / num_gt if num_gt > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0

    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1: {f1:.4f}")

    ned = total_ed / total_ed_cnt
    minus_ned = 1 - ned
    print(f"NED: {ned:.4f}")
    print(f"1-NED: {minus_ned:.4f}")
