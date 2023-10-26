# <Center> Handwritten mathematical expression recognition

# Dataset

- **CROHME2014** is a classical online dataset for handwritten mathematical expression recognition, which comprising 9,820 samples of mathematical expressions.
- **HME100K** is a large-scale handwritten mathematical expression recognition dataset, which contains 100k images from ten thousand writers, and mainly captured by cameras.
  
# Prompt 
```
This is an image of a handwritten mathematical expression. Please recognize the expression above as LaTeX.
```


# Results
- Results of handwritten mathematical expression recognitio
  
    <table>
        <tbody>
        <tr>
            <td rowspan="2">Method</td>
            <td colspan="4">CROHME2014</td>
            <td colspan="4">HME100K</td>
        </tr>
        <tr>
            <td>Exp rate ↑</td>
            <td><=1 ↑</td>
            <td><=2 ↑</td>
            <td><=3 ↑</td>
            <td>Exp rate ↑</td>
            <td><=1 ↑</td>
            <td><=2 ↑</td>
            <td><=3 ↑</td>
        </tr>
        <tr>
            <td>GPT-4V</td>
            <td>34.0%</td>
            <td>44.0%</td>
            <td>50.0%</td>
            <td>54.0%</td>
            <td>16.0%</td>
            <td>18.0%</td>
            <td>22.0%</td>
            <td>28.0%</td>
        </tr>
        <tr>
            <td>Supervised-SOTA</td>
            <td>65.89%</td>
            <td>77.97%</td>
            <td>84.16%</td>
            <td>-</td>
            <td>68.09%</td>
            <td>83.22%</td>
            <td>89.91%</td>
            <td>-</td>
        </tr>
    </table>

- Illustration of handwritten mathematical expression recognition. In each example, the left side displays the input image, while the right side shows the image rendered from the LaTeX sequence output by GPT-4V. In the answer of GPT-4V, we highlight elements match the GT in green and elements do not match in red. Symbol \_ in red represent the missing elements in the output.
![0](./vis_HMER.png)