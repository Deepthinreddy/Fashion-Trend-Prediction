import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("AI Fashion Trend Predictor")

st.write("Predicting future fashion trends using Google Trends data")

# load dataset
data = pd.read_csv("data/fashion_trends.csv")

st.subheader("Raw Trend Data")
st.dataframe(data)

# trend chart
st.subheader("Trend Visualization")

fig, ax = plt.subplots()

for column in data.columns[1:]:
    ax.plot(data[column], label=column)

ax.legend()
ax.set_title("Fashion Trends Over Time")
ax.set_xlabel("Time")
ax.set_ylabel("Search Interest")

st.pyplot(fig)

# simple prediction display
st.subheader("Predicted Top Trends")

growth = {}

for column in data.columns[1:]:
    growth[column] = data[column].iloc[-1] - data[column].iloc[0]

sorted_trends = sorted(growth.items(), key=lambda x: x[1], reverse=True)

for trend in sorted_trends:
    st.write(trend[0])