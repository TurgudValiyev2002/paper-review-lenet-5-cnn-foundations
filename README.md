# Paper Review: LeNet-5 and CNN Foundations

## Motivation

LeNet-5 is one of the most important early convolutional neural networks. Studying it helps us understand why modern computer vision models use local filters, weight sharing, pooling, and end-to-end learning.

## Project Goal

We reviewed the main architectural ideas of LeNet-5 and summarized why they still matter.

## Paper / Problem

The reviewed work is LeCun et al.'s gradient-based document recognition work, where LeNet-5 was used for handwritten digit recognition.

## Tools

Python, pandas, and matplotlib were used to create summary tables and a simple architecture-stage figure.

## Method

We converted the paper's architecture into a structured table and extracted the main technical lessons.

## Hyperparameters

No model was trained in this repository. The focus is paper review and architecture explanation.

## Results

The result files are:

- `results/lenet5_architecture_table.csv`
- `results/lenet5_key_lessons.csv`
- `results/lenet5_architecture_stages.png`

The architecture summary covers input, convolution, subsampling, higher-level convolution, fully connected layers, and output classes.

## Interpretation

LeNet-5 matters because it made image recognition learnable end to end. Instead of manually designing all features, the network learned useful filters from data. Pooling made the model less sensitive to small shifts, and weight sharing reduced the number of parameters.

## Conclusion

Modern CNNs are deeper and more powerful, but their basic logic is already visible in LeNet-5. This paper is worth studying because it explains the foundation, not only the final accuracy.

## How To Run

```bash
pip install -r requirements.txt
python 1_lenet5_review_tables.py
```
