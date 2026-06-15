import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/StudentsPerformance.csv.csv")

df = df.dropna(subset=["Gender"])

gender_scores = df.groupby("Gender")[
    ["MathScore", "ReadingScore", "WritingScore"]
].mean()

print(gender_scores)

gender_scores.plot(kind="bar")

plt.title("Gender Performance Analysis")
plt.ylabel("Average Score")

plt.savefig("../reports/gender_analysis.png")

print("Gender chart saved!")