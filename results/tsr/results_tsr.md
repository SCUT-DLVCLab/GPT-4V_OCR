# <Center> Table structure recognition

# Dataset

- **SciTSR** is a dedicated dataset created to address the task of table structure recognition in scientific papers. The dataset consists of 12,000 training samples and 3,000 test samples.
- **WTW**’s images are collected in the wild. The dataset is split into training/testing sets with 10,970 and 3,611 samples respectively
  
# Prompt 
```
Please read the table in this image and return a html-style reconstructed table in text, do not omit anything.
```

# Results

| Dataset | TEDS-S↑ (%) |
| :-----: | :------------: |
| SciTSR  |     87.47      |
|   WTW   |     25.60      |
