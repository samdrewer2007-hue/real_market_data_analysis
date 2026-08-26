import requests
import pandas as pd
import os

# setup ---------------------------------------------------------------------------
api_key = os.getenv("ALPHAVANTAGE_API_KEY")
url = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "GLD",
    "apikey": api_key
}

response = requests.get(url, params=params)

data = response.json()

print(data)
print(data.keys())

daily_data = data["Time Series (Daily)"]

df = pd.DataFrame(daily_data)
df = df.transpose()
df.index = pd.to_datetime(df.index, errors='coerce')
df = df.apply(pd.to_numeric, errors='coerce')
df = df.sort_index(ascending=True)
df.to_csv('GLD_daily_data.csv')

#export ALPHAVANTAGE_API_KEY="your_actual_key_here" before all runs