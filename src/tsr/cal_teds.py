import os
import json
from convert_form import save_per_html_with_ocr
from convert_form import save_per_html
# from teds_multiprocess import evaluate
import time

pre_path = "/home/cxh/Downloads/Works/GPT-4V_TSR/test_img/SciTSR/predictions.json"
anno_dir = "/home/cxh/Downloads/Works/GPT-4V_TSR/test_img/SciTSR/annotations/structure"

pre_htmls = {}
anno_htmls = {}

with open(pre_path, "r") as f:
    pre_dic = json.load(f)

for anno_file in os.listdir(anno_dir):
    anno_path = os.path.join(os.path.join(anno_dir, anno_file))
    with open(anno_path, "r") as f:
        anno = json.load(f)
    anno = anno["cells"]
    anno.sort(key=lambda x: x["id"])
    html_anno = save_per_html_with_ocr(anno)
    html_anno.replace("\\textbf{", "").replace("}", "")
    anno_htmls.update({anno_file.replace(".json", ".png"):{"html":html_anno}})

for img_name in pre_dic.keys():
    pre_htmls.update({img_name:{"html":'<html><body><table>' + "".join(pre_dic[img_name]) + '</table></body></html>'}})

teds_s = evaluate(pre_htmls, anno_htmls, 40, False)
print("TEDS_S", teds_s)