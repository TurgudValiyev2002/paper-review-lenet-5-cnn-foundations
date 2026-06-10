# Report: LeNet-5 and CNN Foundations

## Motivation

We reviewed LeNet-5 in context because CNNs did not appear from one paper alone. The goal was to understand the chain of ideas behind local receptive fields, shared weights, subsampling, backpropagation, and practical handwritten recognition.

## Papers Reviewed

We reviewed Fukushima's Neocognitron (1980), LeCun et al.'s handwritten ZIP code recognition paper (1989), LeCun et al.'s LeNet-5 document recognition paper (1998), and Ciresan et al.'s GPU-trained deep network paper for MNIST (2011).

## What The Papers Did

Fukushima introduced a hierarchical model for shift-tolerant pattern recognition. LeCun et al. 1989 applied backpropagation to handwritten ZIP code recognition. LeCun et al. 1998 presented LeNet-5 inside a practical document recognition system. Ciresan et al. 2011 showed how GPU training and model committees pushed handwritten digit recognition further.

## Method

We extracted the main contribution, limitation, and lesson from each paper. We also rebuilt the LeNet-5 architecture as a flow diagram and saved comparison tables.

## Review Artifacts

The repository contains a reviewed-papers table, a paper-comparison table, a LeNet-5 architecture table, an architecture flow diagram, and one short note for each reviewed paper in `paper_notes/`.

## Interpretation

LeNet-5 matters because it joined several ideas into one trainable system: local filters, shared weights, subsampling, and dense classification. It was not just a model; it was part of a practical recognition pipeline.

## Conclusion

The most important lesson is that modern CNNs are larger, but their basic logic is already visible in LeNet-5. Understanding these papers makes later computer vision architectures easier to understand.
