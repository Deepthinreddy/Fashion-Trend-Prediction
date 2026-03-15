import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/fashion_trends.csv")

for column in data.columns[1:-1]:
    
    plt.plot(data[column], label=column)

plt.legend()
plt.title("Fashion Trends Over Time")
plt.xlabel("Time")
plt.ylabel("Search Interest")

plt.savefig("fashion_trend_plot.png")
print("Trend graph saved as fashion_trend_plot.png")