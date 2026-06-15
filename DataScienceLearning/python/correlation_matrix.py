import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/wine.csv.csv.csv")

corr = df.corr(numeric_only=True)

plt.imshow(corr)

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Matrix")

plt.savefig("../reports/correlation_matrix.png")

print("Correlation chart saved!")