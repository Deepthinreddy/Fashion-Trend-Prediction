import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv("data/fashion_trends.csv")

results = {}

for column in data.columns[1:-1]:

    y = data[column].values
    X = np.arange(len(y)).reshape(-1,1)

    model = LinearRegression()
    model.fit(X, y)

    future = np.array([[len(y)+3]])
    prediction = model.predict(future)

    results[column] = prediction[0]

sorted_predictions = sorted(results.items(), key=lambda x: x[1], reverse=True)

print("\nPredicted Future Trends")

for item in sorted_predictions:
    print(item)