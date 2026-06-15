import pandas as pd
import matplotlib.pyplot as plt

import os

print(os.path.getsize("../datasets/heart.csv"))

df = pd.read_csv("../datasets/heart.csv", sep="\t")

print(df.head())
print(df.columns)  # Add this to confirm exact column names

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

heart_counts = df["Heart Disease"].value_counts()

plt.figure(figsize=(6,4))
heart_counts.plot(kind="bar")

plt.title("Heart Disease Distribution")
plt.xlabel("Heart Disease")
plt.ylabel("Count")

plt.savefig("../reports/heart_disease_distribution.png")

print("Heart disease chart saved!")