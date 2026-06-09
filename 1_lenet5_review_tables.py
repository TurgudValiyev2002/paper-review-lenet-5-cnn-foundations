from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RESULTS = Path("results")

def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    layers = pd.DataFrame([
        ("Input", "32x32 image", "normalized digit image"),
        ("C1", "6 feature maps", "5x5 convolution"),
        ("S2", "6 feature maps", "subsampling / pooling"),
        ("C3", "16 feature maps", "partial convolution connections"),
        ("S4", "16 feature maps", "subsampling / pooling"),
        ("C5", "120 units", "convolution behaving like dense layer"),
        ("F6", "84 units", "fully connected layer"),
        ("Output", "10 classes", "digit class scores"),
    ], columns=["stage", "shape_or_units", "role"])
    layers.to_csv(RESULTS / "lenet5_architecture_table.csv", index=False)
    lessons = pd.DataFrame([
        ("local receptive fields", "nearby pixels form useful patterns"),
        ("weight sharing", "same filter detects pattern across locations"),
        ("pooling", "small shifts should not fully change prediction"),
        ("end-to-end learning", "features are learned from data"),
    ], columns=["idea", "why_it_matters"])
    lessons.to_csv(RESULTS / "lenet5_key_lessons.csv", index=False)
    plt.figure(figsize=(9, 2.8))
    plt.bar(layers["stage"], range(1, len(layers) + 1), color="#3d6fb6")
    plt.title("LeNet-5 Architecture Stages")
    plt.ylabel("Stage order")
    plt.tight_layout()
    plt.savefig(RESULTS / "lenet5_architecture_stages.png", dpi=160)
    print(layers.to_string(index=False))

if __name__ == "__main__":
    main()
