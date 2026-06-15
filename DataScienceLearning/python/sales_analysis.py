import pandas as pd

df = pd.read_csv("../datasets/wine.csv.csv.csv")

print(df)

print("\nAverage Alcohol:")
print(df["Alcohol"].mean())

print("\nHighest Quality:")
print(df["Quality"].max())

print("\nLowest Quality:")
print(df["Quality"].min())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

import pandas as pd

df = pd.read_csv("../datasets/wine.csv.csv.csv")

print(df.columns)

print("\nAverage Alcohol:")
print(df["Alcohol"].mean())

print("\nHighest Quality:")
print(df["Quality"].max())

print("\nLowest Quality:")
print(df["Quality"].min())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())