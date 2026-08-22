import requests
import pandas as pd
import os
import matplotlib.pyplot as plt

# setup ---------------------------------------------------------------------------
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
url = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "SPY",
    "apikey": api_key
}

response = requests.get(url, params=params)

data = response.json()

daily_data = data["Time Series (Daily)"]

df = pd.DataFrame(daily_data)
df = df.transpose()
df.index = pd.to_datetime(df.index, errors='coerce')
df = df.apply(pd.to_numeric, errors='coerce')
df = df.sort_index(ascending=True)
df.to_csv('SPY_daily_data.csv')