import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/wine.csv.csv.csv")

highest = df["Quality"].max()

plt.figure(figsize=(6,4))
plt.bar(["Highest Quality"], [highest])

plt.title("Highest Wine Quality")
plt.ylabel("Quality Score")

plt.savefig("../reports/highest_quality.png")

print("Highest quality chart saved!")