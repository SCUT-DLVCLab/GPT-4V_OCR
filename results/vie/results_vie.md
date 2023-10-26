# <Center> Visual Information Extraction

# Dataset

## FUNSD

<a href="https://guillaumejaume.github.io/FUNSD/"><img src="https://img.shields.io/badge/dataset-link-yellow"></a>

FUNSD is a dataset for form understanding in natural language. It consists of 199 real scanned forms, in which 149 for training and 50 for testing. Previous works evaluate their performance on the SER task and RE task. The SER task aims to classify the text blocks into 4 categories: header, question, answer, and other. The RE task aims to identify the linking relationships between the known entities (SER ground-truth labels). 


## XFUND

<a href="https://github.com/doc-analysis/XFUND"><img src="https://img.shields.io/badge/dataset-link-yellow"></a>

XFUND dataset is a multilingual extension of FUNSD that covers seven languages (Chinese, Japanese, French, Italian, German, Spanish, and Portuguese). Each subset contains 199 real scanned forms, in which 149 for training and 50 for testing. 


# Prompt

Model Version: `Sep. 25`

## SER

```
Please read the text in this image and return the information in the following JSON format (note xxx is placeholder, if the information is not available in the image, put "N/A" instead)."header": [xxx, ...], "key": [xxx, ...], "value": [xxx, ...]
```

## End-to-End Pair Extraction

```
You are a document understanding AI, who reads the contents in the given document image and tells the information that the user needs. Respond with the original content in the document image, do not reformat. No extra explanation is needed. Extract all the key-value pairs from the document image.
```

# Results

## SER

<table>
    <tbody>
    <tr>
        <td rowspan="2">Method</td>
        <td colspan="4">FUNSD</td>
        <td colspan="4">XFUND-zh</td>
    </tr>
    <tr>
        <td>Precision ↑</td>
        <td>Recall ↑</td>
        <td>F1 ↑</td>
        <td>1-NED ↑</td>
        <td>Precision ↑</td>
        <td>Recall ↑</td>
        <td>F1 ↑</td>
        <td>1-NED ↑</td>
    </tr>
    <tr>
        <td>GPT-4V</td>
        <td>41.85%</td>
        <td>29.36%</td>
        <td>34.51%</td>
        <td>0.2697</td>
        <td>25.87%</td>
        <td>15.15%</td>
        <td>19.11%</td>
        <td>0.1544</td>
    </tr>
    <tr>
        <td>Supervised-SOTA</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>0.5500</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
</table>


## End-to-End Pair Extraction

We observe that there exists some erroneous annotations in the FUNSD and XFUND dataset, which is inconsistent with human understanding. Hence the results shown below may not be accurate. 

| Dataset  | Precision↑ (%) | Recall↑ (%) | F1↑ (%) | 1-NED↑ |
| :------: | :---------------: | :------------: | :--------: | :----: |
|  FUNSD   |       20.69       |     10.25      |   13.71    | 0.1979 |
| XFUND-zh |       0.07        |      0.02      |    0.03    | 0.0420 |


# Cases Visualization
  
Illustration of error cases of the SER task. The text content enclosed within the red box is incorrectly identified as *header* entities.

![0](ser_visualization_00.jpg)


Illustration of Entity Prediction on Full Document Images in the FUNSD Dataset. Due to GPT-4V's limited capability in recognizing Chinese characters, we have excluded examples from the XFUND-zh dataset in this context. Zoom in for best review.

![1](vis_ser_00.jpg)

Cases in the Pair Extraction task. GPT4V generates keys for the contents enclosed within the red box, which does not exist in the document image.

![2](linking_visualization.png)
