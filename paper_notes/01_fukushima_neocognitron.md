# Fukushima 1980: Neocognitron

Paper: Kunihiko Fukushima, "Neocognitron: A Self-organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position"  
Link: https://doi.org/10.1007/BF00344251

This paper is important because it introduced a hierarchical neural model for visual pattern recognition before modern CNNs became common. The main question was how a system can recognize a visual pattern even when the pattern shifts position. Fukushima's answer was to build a layered model where local features are detected in early stages and then combined into more complex patterns in later stages.

The model used ideas that later became familiar in CNNs: local receptive fields, feature maps, hierarchy, and tolerance to small shifts. The paper did not present a modern backpropagation-trained CNN, so we should not describe it as LeNet. Its value is more foundational: it showed that visual recognition can be organized as repeated local feature extraction and spatial aggregation.

What we learn from this paper is that CNN design has biological and architectural roots. Locality is not an accident. Images have local structure, so a model that looks at local neighborhoods and reuses detectors across space is naturally suitable for vision.

The limitation is that the training method and practical deployment were not the same as later CNN systems. The Neocognitron is best understood as an early conceptual foundation, not as the final trainable CNN pipeline used today.
