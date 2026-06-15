import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/heart.csv", sep="\t")

heart_counts = df["Heart Disease"].value_counts()

plt.pie(
    heart_counts,
    labels=heart_counts.index,
    autopct="%1.1f%%"
)

plt.title("Heart Disease Distribution")

plt.savefig("../reports/heart_pie.png")

print("Heart pie chart saved!")