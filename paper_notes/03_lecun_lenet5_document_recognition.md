# LeCun et al. 1998: Gradient-Based Learning Applied to Document Recognition

Paper: Yann LeCun, Leon Bottou, Yoshua Bengio, Patrick Haffner, "Gradient-Based Learning Applied to Document Recognition"  
Link: https://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf

This is the main LeNet-5 paper. The authors presented gradient-based learning for document recognition and described LeNet-5 as part of a full recognition system. The task was not an artificial toy problem only; the work connected neural networks to practical document and check reading.

LeNet-5 takes a 32x32 input image and passes it through convolution, subsampling, more convolution, more subsampling, and final classification layers. This sequence is important because early layers detect local strokes, intermediate layers combine strokes into larger structures, and final layers make the class decision.

The paper's main contribution is showing that a neural network can learn features and classification jointly. This is different from older pipelines where feature engineering and classification were separate. LeNet-5 made the case that end-to-end trainable visual recognition is practical.

What we learn is that CNN success comes from combining architecture and training: local filters, shared weights, spatial reduction, and gradient-based optimization.

The limitation is scale. LeNet-5 is small compared with modern CNNs and vision transformers. But the design principles remain central, which is why this paper is still worth reviewing.
