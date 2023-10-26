# GPT-4V_OCR

<div align="center">
  <p>
      <!-- <h1>GPT4OCR</h1> -->
      <img width="100%" src="images/GPT4OCR.png"></a>
  </p>

  <!-- <a href=""><img src="https://img.shields.io/github/stars/{SCUT-DLVCLab}/{GPT4OCR}.svg"></a>
  <a href=""><img src="https://img.shields.io/github/issues/{SCUT-DLVCLab}/{GPT4OCR}.svg"></a>
  <a href=""><img src="https://img.shields.io/github/issues-pr/{SCUT-DLVCLab}/{GPT4OCR}.svg"></a> -->



<!-- [English](README.md) | [简体中文](README.zh-CN.md) -->

</div>

<br>

<!-- This repository evaluates the performance of GPT-4V(ision) on various OCR-related tasks for our paper [Exploring OCR Capabilities of GPT-4V(ision) : A Quantitative and In-depth Evaluation](https://arxiv.org/abs/2310.16809). 
Please see the corresponding [paper](https://arxiv.org/abs/2310.16809) for more details. -->

### [[arXiv 2310.16809]](https://arxiv.org/abs/2310.16809)Exploring OCR Capabilities of GPT-4V(ision) : A Quantitative and In-depth Evaluation
This paper presents a comprehensive evaluation of the Optical Character Recognition (OCR) capabilities of the recently released GPT-4V(ision), a Large Multimodal Model (LMM). We assess the model's performance across a range of OCR tasks, including scene text recognition, handwritten text recognition, handwritten mathematical expression recognition, table structure recognition, and information extraction from visually-rich document. The evaluation reveals that GPT-4V performs well in recognizing and understanding Latin contents, but struggles with multilingual scenarios and complex tasks. Based on these observations, we delve deeper into the necessity of specialized OCR models and deliberate on the strategies to fully harness the pretrained general LMMs like GPT-4V for OCR downstream tasks. The study offers a critical reference for future research in OCR with LMMs. 
<!-- Evaluation pipeline and results are available at this [https URL](https://github.com/SCUT-DLVCLab/GPT-4V_OCR). -->

<!-- <div>
    <a href=""><img src="https://img.shields.io/badge/-Run on gradio-orange" alt="gradio"></a>
</div> -->


<h2>Scene Text Recognition</h2>
<div>
    <a href="results/str/results_str.md"><img src="https://img.shields.io/badge/Evaluation- 🗒️Results-blue" alt="results_str"></a>
</div>
<div align="left">
Scene Text Recognition (STR) aims to recognize textual information in natural scene pictures.

<div align="left">
<h2>Handwritten Text Recognition</h2>
<div>
    <a href="results/htr/results_htr.md"><img src="https://img.shields.io/badge/Evaluation- 🗒️Results-blue" alt="results_htr"></a>
<div align="left">
Handwritten Text Recognition (HTR) aims to recognize handwritten text.
</div>
<div align="left">
<h2>Handwritten Mathematical Expression Recognition</h2>
<div>
    <a href="results/hmer/results_hmer.md"><img src="https://img.shields.io/badge/Evaluation- 🗒️Results-blue" alt="results_hmer"></a>
<div align="left">
Handwritten Mathematical Expression Recognition (HMER) aims to recognize handwritten mathematical formulas.
</div>
<div align="left">
<h2>Visual Information Extraction</h2>

<div>
    <a href="results/vie/results_vie.md"><img src="https://img.shields.io/badge/Evaluation- 🗒️Results-blue" alt="results_vie"></a>
    <a href="src/vie/parse_kv.py"><img src="https://img.shields.io/badge/Evaluation- 🛠️Scripts-blue" alt="results_vie"></a>
    <a href="https://github.com/SCUT-DLVCLab/Document-AI-Recommendations/tree/main"><img src="https://img.shields.io/badge/Resource-🧷Collections-orange" alt="recommendations_vie"></a>
</div>
<div align="left">

To learn more about Visual Information Extraction, please refer to [Document-AI-Recommendations](https://github.com/SCUT-DLVCLab/Document-AI-Recommendations/tree/main).

Visual Information Extraction(VIE) aims at mining, analyzing, and extracting key fields entities contained in visually rich documents. For example, given an image of a receipt, the VIE algorithms will tell information such as store name, product details, price, etc. For documents like forms, VIE algorithms will tell the key-value pairs contained.

<div align="left">
<h2>Table Structure Recognition</h2>
<div>
    <a href="results/tsr/results_tsr.md"><img src="https://img.shields.io/badge/Evaluation- 🗒️Results-blue" alt="results_tsr"></a>
    <a href="https://github.com/SCUT-DLVCLab/Document-AI-Recommendations/tree/main"><img src="https://img.shields.io/badge/Resource-🧷Collections-orange" alt="recommendations_tsr"></a>
</div>
<div align="left">

To learn more about Table Structure Recognition, please refer to [Document-AI-Recommendations](https://github.com/SCUT-DLVCLab/Document-AI-Recommendations/tree/main).

Table Structure Recognition(TSR) aims to recognize the cellular structures of tables from table images by extracting the coordinates of cell boxes and row/column spanning information. This task is very challenging since tables may have complex structures, diverse styles and contents, and become geometrically distorted or even curved during an image capturing process.

<!-- <h2>Layout Analysis</h2> -->

</div>

## Data Download
- [Google Drive](https://drive.google.com/file/d/1V3kW01k0ZDbEH6cnhBLWEVlnmIEHN72J/view?usp=drive_link)
- [Baidu Drive(6wyf)](https://pan.baidu.com/s/1qJvphPgtVIwGatRsqlSc7Q?pwd=6wyf)
## Citation
```
@misc{shi2023exploring,
      title={Exploring OCR Capabilities of GPT-4V(ision) : A Quantitative and In-depth Evaluation}, 
      author={Yongxin Shi and Dezhi Peng and Wenhui Liao and Zening Lin and Xinhong Chen and Chongyu Liu and Yuyi Zhang and Lianwen Jin},
      year={2023},
      eprint={2310.16809},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```