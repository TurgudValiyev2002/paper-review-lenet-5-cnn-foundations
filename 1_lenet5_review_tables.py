from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import FancyArrowPatch, Rectangle


RESULTS = Path("results")


def save_lenet_architecture() -> None:
    layers = [
        ("Input", "32x32\nimage"),
        ("C1", "6 x 28x28\n5x5 conv"),
        ("S2", "6 x 14x14\nsubsample"),
        ("C3", "16 x 10x10\n5x5 conv"),
        ("S4", "16 x 5x5\nsubsample"),
        ("C5", "120\nconv"),
        ("F6", "84\nfully connected"),
        ("Output", "10\nclasses"),
    ]
    fig, ax = plt.subplots(figsize=(12, 3.8))
    ax.axis("off")
    x = 0.02
    for idx, (name, detail) in enumerate(layers):
        width = 0.105 if idx < 6 else 0.12
        rect = Rectangle((x, 0.35), width, 0.32, facecolor="#dce9f8", edgecolor="#2f5f9f", linewidth=1.4)
        ax.add_patch(rect)
        ax.text(x + width / 2, 0.56, name, ha="center", va="center", fontsize=11, weight="bold")
        ax.text(x + width / 2, 0.43, detail, ha="center", va="center", fontsize=8)
        if idx < len(layers) - 1:
            ax.add_patch(FancyArrowPatch((x + width, 0.51), (x + width + 0.035, 0.51), arrowstyle="->", mutation_scale=14, linewidth=1.2))
        x += width + 0.045
    ax.set_title("LeNet-5 Architecture Flow", fontsize=15, weight="bold")
    plt.tight_layout()
    plt.savefig(RESULTS / "lenet5_architecture_flow.png", dpi=180)
    plt.close()


def main() -> None:
    RESULTS.mkdir(exist_ok=True)

    papers = pd.DataFrame(
        [
            {
                "paper": "Neocognitron: A Self-organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position",
                "authors": "Kunihiko Fukushima",
                "year": 1980,
                "url": "https://doi.org/10.1007/BF00344251",
                "main_question": "Can a hierarchical neural model recognize patterns despite shifts in position?",
                "what_they_did": "Proposed a multilayer visual recognition model with local feature extraction and downsampling-like stages.",
                "main_lesson": "CNN ideas did not appear suddenly; locality and hierarchy were already central in early neural vision models.",
            },
            {
                "paper": "Backpropagation Applied to Handwritten Zip Code Recognition",
                "authors": "Yann LeCun et al.",
                "year": 1989,
                "url": "https://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf",
                "main_question": "Can backpropagation train a constrained neural network for real handwritten digit recognition?",
                "what_they_did": "Applied backpropagation to handwritten ZIP code recognition using local receptive fields and shared weights.",
                "main_lesson": "Learning features end to end can outperform hand-designed recognition pipelines.",
            },
            {
                "paper": "Gradient-Based Learning Applied to Document Recognition",
                "authors": "Yann LeCun, Leon Bottou, Yoshua Bengio, Patrick Haffner",
                "year": 1998,
                "url": "https://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf",
                "main_question": "Can gradient-based learning solve practical document recognition at scale?",
                "what_they_did": "Presented LeNet-5 and a full document-recognition system for handwritten characters and bank checks.",
                "main_lesson": "LeNet-5 connected convolution, subsampling, dense layers, and real deployment.",
            },
            {
                "paper": "Handwritten Digit Recognition with a Committee of Deep Neural Nets on GPUs",
                "authors": "Dan C. Ciresan, Ueli Meier, Luca M. Gambardella, Jurgen Schmidhuber",
                "year": 2011,
                "url": "https://arxiv.org/abs/1103.4487",
                "main_question": "How far can deeper neural networks go on MNIST with GPU acceleration?",
                "what_they_did": "Used GPU-trained deep neural network committees to push MNIST error rates below earlier records.",
                "main_lesson": "Hardware and scale later revived neural methods that LeNet had made conceptually clear.",
            },
        ]
    )
    papers.to_csv(RESULTS / "reviewed_papers.csv", index=False)

    architecture = pd.DataFrame(
        [
            ("Input", "32x32 image", "normalizes handwritten digit input"),
            ("C1", "6 feature maps, 5x5 convolution", "learns local stroke detectors"),
            ("S2", "subsampling", "reduces spatial resolution and adds shift tolerance"),
            ("C3", "16 feature maps, 5x5 convolution", "combines lower-level strokes into larger patterns"),
            ("S4", "subsampling", "compresses representation before classification"),
            ("C5", "120 units", "moves from maps to compact learned representation"),
            ("F6", "84 units", "dense feature combination"),
            ("Output", "10 classes", "digit class decision"),
        ],
        columns=["stage", "structure", "purpose"],
    )
    architecture.to_csv(RESULTS / "lenet5_architecture_table.csv", index=False)

    comparison = pd.DataFrame(
        [
            ("Neocognitron", "hierarchical local feature extraction", "not trained end to end by modern backprop"),
            ("LeCun 1989", "backpropagation for handwritten ZIP codes", "smaller and earlier than LeNet-5"),
            ("LeNet-5 1998", "complete CNN-style document recognition system", "small by modern standards"),
            ("Ciresan 2011", "GPU scaling and model committees", "less focused on architectural interpretability"),
        ],
        columns=["work", "contribution", "limitation"],
    )
    comparison.to_csv(RESULTS / "paper_comparison.csv", index=False)

    save_lenet_architecture()
    print(papers[["year", "paper", "main_lesson"]].to_string(index=False))


if __name__ == "__main__":
    main()
