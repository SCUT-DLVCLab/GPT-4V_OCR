<h1 align="center">Visual Information Extraction</h1>

- [FUNSD](#funsd)
- [XFUND](#xfund)
  - [XFUND zh](#xfund-zh)



# FUNSD

<a href="https://guillaumejaume.github.io/FUNSD/"><img src="https://img.shields.io/badge/dataset-link-yellow"></a>

FUNSD is a dataset for form understanding in natural language. It consists of 199 real scanned forms, in which 149 for training and 50 for testing. Previous works evaluate their performance on the SER task and RE task. The SER task aims to classify the text blocks into 4 categories: header, question, answer, and other. The RE task aims to identify the linking relationships between the known entities (SER ground-truth labels). In our experiments, we evaluate the performance of GPT-4V on the pair extraction task, which aims at extracting the key-value pairs from the document image in an end-to-end manner.

<h2>Settings</h2>

- Model Version: `Sep. 25`
- Prompt
    ```
    You are a document understanding AI, who reads the contents in the given document image and tells the information that the user needs. Respond with the original content in the document image, do not reformat. No extra explanation is needed.
    Extract all the key-value pairs from the document image.
    ```

<h2>Results</h2>

| Model  | Precision | Recall | F1  |
| ------ | --------- | ------ | --- |
| GPT-4V |           |        |     |

----

# XFUND

<a href="https://github.com/doc-analysis/XFUND"><img src="https://img.shields.io/badge/dataset-link-yellow"></a>

XFUND is a multi-language extension of FUNSD. It contains 7 subsets, covering languages including Chinese, Japanese, French, German, Italian, Spanish, and Portuguese. Each subset contains 199 real scanned forms, in which 149 for training and 60 for testing. In our experiments, we evaluate the performance of GPT-4V on the pair extraction task, which aims at extracting the key-value pairs from the document image in an end-to-end manner.

## XFUND zh

<h2>Settings</h2>

- Model Version: `Sep. 25`
- Prompt
    ```
    你是一个文档理解智能助手。你能阅读给定文本图像的内容，并根据用户的需求给出回答。回答的内容要求是文档中的原始文本，不需要修改格式。回答不需要做出额外的解释。
    从文档图像中抽取出所有键值对
    ```

<h2>Results</h2>

| Model  | Precision | Recall | F1  |
| ------ | --------- | ------ | --- |
| GPT-4V |           |        |     |