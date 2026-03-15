from pytrends.request import TrendReq
import pandas as pd

# connect to google trends
pytrends = TrendReq(hl='en-US', tz=330)

keywords = [
    "cargo pants",
    "oversized blazer",
    "linen shirts",
    "streetwear",
    "y2k fashion"
]

# build request
pytrends.build_payload(keywords, timeframe='today 12-m', geo='')

# fetch trend data
data = pytrends.interest_over_time()

# remove 'isPartial' column if it exists
if 'isPartial' in data.columns:
    data = data.drop(columns=['isPartial'])

# save data
data.to_csv("data/fashion_trends.csv")

print("Trend data collected successfully!")