import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/wine.csv.csv.csv")

plt.pie(
    df["Quality"],
    labels=df["Name"],
    autopct="%1.1f%%"
)

plt.title("Wine Quality Share")

plt.savefig("../reports/wine_pie_chart.png")

print("Pie chart saved!")