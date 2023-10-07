# encoding=utf-8
FUNSD_prefix = "You are a document understanding AI, who reads the contents in the given document image and tells the information that the user needs. Respond with the original content in the document image, do not reformat. No extra explanation is needed.\n"
FUNSD_prompt_list = [
    r"Extract all the key-value pairs from the document image.",
    r"Extract all the key-value pairs from the document image. Response with a two-column markdown table.",
    r"Extract all the key-value pairs from the document image. Response in json formatted as [{\"key\": <key_content>, \"value\": <value_content>}, {\"key\": <key_content>, \"value\": <value_content>}, ...]",
]

XFUND_ZH_prefix = (
    "你是一个文档理解智能助手。你能阅读给定文本图像的内容，并根据用户的需求给出回答。回答的内容要求是文档中的原始文本，不需要修改格式。回答不需要做出额外的解释。\n"
)
XFUND_ZH_prompt_list = [
    r"从文档图像中抽取出所有键值对",
    r"从文档图像中抽取出所有键值对。输出一个两列的markdown表格。",
    r"从文档图像中抽取出所有键值对。输出一个json样式的列表，格式为[{\"key\": <key_content>, \"value\": <value_content>}, {\"key\": <key_content>, \"value\": <value_content>}, ...]",
]
