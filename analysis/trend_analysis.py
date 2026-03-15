import pandas as pd

data = pd.read_csv("data/fashion_trends.csv")
print("Dataset Preview")
print(data.head())

growth = {}

for column in data.columns[1:-1]:
    growth[column] = data[column].iloc[-1] - data[column].iloc[0]

sorted_trends = sorted(growth.items(), key=lambda x: x[1], reverse=True)

print("\nTrending Items:")
for trend in sorted_trends:
    print(trend)