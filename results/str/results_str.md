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
    What are all the scene text in the image? Do not translate
    ```

# Results
- Results of word-level scene text recognition.
  
    |   Dataset    | WA↑(%) | WAI↑(%) |
    | :----------: | :----: | :-----: |
    |    CUTE80    |   20   |   88    |
    | SCUT-CTW1500 |   58   |   62    |
    |  Total-Text  |   56   |   60    |
    |   WordArt    |   56   |   60    |
    |    ReCTS     |   0    |    0    |

 - Results of MLT19.
    | Language | Precision↑(%) | Precision IC↑ (%) | Recall↑ (%) | Recall IC↑ (%) |
    | :------: | :-----------: | :---------------: | :---------: | :------------: |
    |  Arabic  |     17.76     |       17.76       |    18.18    |     18.18      |
    | English  |     86.96     |       93.48       |    79.33    |     86.67      |
    |  French  |     83.50     |       85.44       |    84.31    |     86.27      |
    | Chinese  |     1.14      |       1.14        |    1.49     |      1.49      |
    |  German  |     72.73     |       75.97       |    85.27    |     89.15      |
    |  Korean  |     10.40     |       10.40       |    12.17    |     12.17      |
    | Japanese |     11.49     |       11.49       |    11.63    |     11.63      |
    | Italian  |     63.06     |       65.61       |    67.87    |     70.04      |
    |  Bangla  |     2.44      |       2.44        |    2.60     |      2.60      |
    |  Hindi   |     7.07      |       7.07        |    8.08     |      8.08      |