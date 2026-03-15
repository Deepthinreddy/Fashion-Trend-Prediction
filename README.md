#  AI Fashion Trend Predictor

A **data-driven fashion trend analysis system** that collects Google search trend data, analyzes popularity patterns, and predicts upcoming fashion trends using machine learning.

This project demonstrates a **complete data science pipeline** — from data collection to visualization and an interactive dashboard.

---

## ✨ Features

• Collects fashion trend data from Google Trends
• Analyzes popularity patterns across time
• Predicts future trends using machine learning
• Visualizes trends with graphs
• Interactive dashboard built with **Streamlit**

---

## 🧠 How It Works

The system follows a simple AI pipeline:

1. **Data Collection**
   Fashion keyword trends are fetched using the Google Trends API.

2. **Trend Analysis**
   Historical trend data is analyzed to measure growth patterns.

3. **Prediction Model**
   A regression model predicts which fashion styles are likely to trend.

4. **Visualization**
   Trend changes are visualized using graphs.

5. **Interactive Dashboard**
   Users can explore data and predictions using a Streamlit web interface.

---

## 🗂 Project Structure

```
Fashion-Trend-Prediction
│
├── analysis
│   └── trend_analysis.py
│
├── data
│   └── fashion_trends.csv
│
├── model
│   └── trend_prediction.py
│
├── scraper
│   └── google_trends_scraper.py
│
├── visualisation
│   └── trend_graph.py
│
├── dashboard.py
├── main.py
└── README.md
```

---

## 📊 Example Trend Output

Predicted future fashion trends:

```
1. Streetwear
2. Cargo Pants
3. Linen Shirts
```

Trend visualization shows how search interest changes over time.

---

## 🚀 Running the Project

### Install Dependencies

```
pip install pandas numpy matplotlib scikit-learn pytrends streamlit
```

### Run the Analysis Pipeline

```
python main.py
```

### Run the Interactive Dashboard

```
streamlit run dashboard.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Pytrends
* Streamlit

---

## 📌 Possible Improvements

• Add Instagram or Pinterest trend data
• Use deep learning for prediction
• Deploy the dashboard online
• Integrate outfit recommendation models

---

## 👩‍💻 Author

**Deepthi N Reddy**

---

## ⭐ If you like this project

Consider starring the repository!
