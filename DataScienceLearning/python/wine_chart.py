import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/wine.csv.csv.csv")

bars = plt.bar(
    df["Name"],
    df["Quality"],
    color=["red", "blue", "green", "orange", "purple"]
)

avg_quality = df["Quality"].mean()

plt.axhline(
    y=avg_quality,
    color="black",
    linestyle="--",
    label=f"Average = {avg_quality:.2f}"
)

plt.title("Wine Quality Analysis")
plt.xlabel("Wine")
plt.ylabel("Quality")

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        str(height),
        ha="center"
    )

plt.grid(axis="y")
plt.legend()

plt.savefig("../reports/charts.png")

print("Professional chart saved!")