import pandas as pd

df = pd.read_csv("../datasets/StudentsPerformance.csv.csv")

# Drop any rows where Gender is NaN (corrupted rows)
df = df.dropna(subset=["Gender"])

print(df.head())
print(df.columns)

print("\nAverage Math Score:")
print(df["MathScore"].mean())

print("\nAverage Reading Score:")
print(df["ReadingScore"].mean())

print("\nAverage Writing Score:")
print(df["WritingScore"].mean())

import matplotlib.pyplot as plt

scores = [
    df["MathScore"].mean(),
    df["ReadingScore"].mean(),
    df["WritingScore"].mean()
]

subjects = ["Math", "Reading", "Writing"]

plt.bar(
    subjects,
    scores,
    color=["red", "blue", "green"]
)

plt.title("Average Student Scores")
plt.xlabel("Subjects")
plt.ylabel("Average Score")

plt.savefig("../reports/student_scores.png")

print("Chart saved!")