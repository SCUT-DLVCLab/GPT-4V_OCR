# encoding: utf-8
import argparse
import json
import re
from typing import Dict, List

from src.common.string_utils import string_f2h

BRACKET_MAP = {
    ")": "(",
    "]": "[",
    "}": "{",
}
BRACKET_SET = set(BRACKET_MAP.keys()) | set(BRACKET_MAP.values())


def parse_dummy_json(dir_orig: str):
    parsed_dict: Dict[str, List[str]] = {}

    dummy_lines: List[str]
    with open(dir_orig, "r", encoding="utf-8") as f:
        dummy_lines = f.readlines()

    bracket_stash: List[str] = []
    sample_lines: List[str] = []
    sample_id: int = None
    for dummy_line in dummy_lines:
        dummy_line = string_f2h(dummy_line.strip())
        if dummy_line in BRACKET_SET or dummy_line.replace(",", "") in BRACKET_SET:
            # start/end line of each json block
            dummy_line = dummy_line.replace(",", "")
            if len(bracket_stash) > 0 and BRACKET_MAP.get(dummy_line, None) == bracket_stash[-1]:
                bracket_stash.pop(-1)
                assert (
                    sample_id not in parsed_dict.keys()
                ), f"Duplicate sample id: {sample_id}"
                if len(sample_lines) > 0 and sample_lines[-1].endswith('"'):
                    sample_lines[-1] = sample_lines[-1][:-1]  # remove the last "
                parsed_dict[sample_id] = sample_lines
                sample_lines = []
                sample_id = None
                continue
            elif dummy_line in BRACKET_MAP.values():
                bracket_stash.append(dummy_line)
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
                # GPT's stupid extra words
                pass
            else:
                sample_lines.append(content_)
        elif "note: " in dummy_line.lower():
            # GPT's stupid extra words, seems to be the last line of each sample
            continue
        elif dummy_line == "":
            continue
        else:
            # middle lines of each sample
            sample_lines.append(dummy_line)

    return parsed_dict


def parse_single_content(content_lines: List[str]):
    pass


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--dir_orig", type=str, help="Path to the original dummy.json")
    # args = parser.parse_args()
    
    # parsed_dict = parse_dummy_json(args.dir_orig)

    # FIXME DEBUG
    parsed_dict = parse_dummy_json("results/vie/private_FUNSD_res.json")