# <Center> Scene text recognition

# Dataset

## Word-level text recognition

   - **CUTE80**  is the first curved text dataset that consists of 80 curved text images.
   - **SCUT-CTW1500**  is a curved text dataset, which includes over 10,000 text annotations in 1500 images.
   - **Total-Text** has 1,555 scene images, 9,330 annotated words with 3 different text orientations including horizontal, multi-oriented, and curved text.
   - **WordArt** is a dataset which primarily features challenging artistic text.
   - **ReCTS**  is a large-scale dataset of 25,000 images, which mainly focuses on reading Chinese text on signboard.
## End-to-end text recognition
   - **MLT19**  is a real dataset for Multi-Lingual scene Text (MLT) detection and recognition, which consists of 20,000 images containing text from 10 languages.

# Prompt
- For word-level text recognition
    ```
    What is the scene text in the image?
    ```
- For end-to-end text recognition
    ```
    What are all the scene text in the image? Do not translate.
    ```
- For ReCTS in Chinese
    ```
    图片中的场景文字是什么？
    ```

# Results
- Results of word-level secne text recognition.
   |     Method      | CUTE80 | SCUT-CTW1500 | Total-Text | WordArt | ReCTS |
   | :-------------: | :----: | :----------: | :--------: | :-----: | :---: |
   |     GPT-4V      | 88.0%  |    62.0%     |   66.0%    |  62.0%  |   0   |
   | Supervised-SOTA | 98.6%  |    87.0%     |   90.1%    |  68.2%  | 94.0% |

- Results of MLT19.
   | Language | Precision ↑ | Recall ↑ |  F1 ↑  |
   | :------: | :---------: | :------: | :----: |
   |  Arabic  |   17.76%    |  18.18%  | 17.97% |
   | English  |   86.96%    |  79.33%  | 82.97% |
   |  French  |    83.5%    |  84.31%  | 83.9%  |
   | Chinese  |    1.14%    |  1.49%   | 1.29%  |
   |  German  |   72.73%    |  85.27%  | 78.5%  |
   |  Korean  |    10.4%    |  12.17%  | 11.22% |
   | Japanese |   11.49%    |  11.63%  | 11.56% |
   | Italian  |   63.06%    |  67.87%  | 65.38% |
   |  Bangla  |    2.44%    |   2.6%   | 2.52%  |
   |  Hindi   |    7.07%    |  8.08%   | 7.54%  |

- Impact of image resolution for recognition performance on MLT19 English subset.
   | Image size | Precision ↑ | Recall ↑ |  F1 ↑  |
   | :--------: | :---------: | :------: | :----: |
   |    128     |   47.10%    |  58.88%  | 52.34% |
   |    256     |   74.64%    |  86.67%  | 80.21% |
   |    512     |   86.23%    |  83.69%  | 84.94% |
   |    1024    |   90.58%    |  85.14%  | 87.78% |
   |    2048    |   92.75%    |  89.12%  | 89.46% |