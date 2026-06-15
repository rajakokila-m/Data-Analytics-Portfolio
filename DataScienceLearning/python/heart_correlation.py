import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datasets/heart.csv", sep="\t")

corr = df.corr(numeric_only=True)

plt.imshow(corr)

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Heart Disease Correlation Matrix")

plt.tight_layout()

plt.savefig("../reports/heart_correlation.png")

print("Heart correlation chart saved!")