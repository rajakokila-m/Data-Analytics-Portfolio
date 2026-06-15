import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/StudentsPerformance.csv.csv")

df = df.dropna(subset=["Gender"])

plt.scatter(
    df["ReadingScore"],
    df["WritingScore"]
)

plt.title("Reading vs Writing Scores")
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")

plt.savefig("../reports/scatter_plot.png")

print("Scatter plot saved!")