import pandas as pd
import matplotlib.pyplot as plt


#df = pd.read_csv(
   # "SPY_daily_data.csv",
   # index_col=0,
   # parse_dates=True
#)
#analysis ---------------------------------------------------------------------------



daily_returns = df['4. close'].pct_change()
print(daily_returns)
annualised_mean_return = daily_returns.mean() * 252
annualised_std_return = daily_returns.std() * 252**0.5

rolling_volatility = daily_returns.rolling(window=20).std() * (252**0.5)


# plots ---------------------------------------------------------------------------

pls, axs = plt.subplots(3, 1, figsize=(10, 8))
plt.tight_layout()
axs[0].plot(df.index, daily_returns)
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Daily Returns')
axs[0].set_title('SPY Daily Returns')

axs[1].hist(daily_returns.dropna(), bins=100, edgecolor='black')
axs[1].set_xlabel('Daily Returns')
axs[1].set_ylabel('Frequency')

axs[2].plot(df.index, rolling_volatility)
axs[2].set_xlabel('Date')
axs[2].set_ylabel('Rolling Volatility')


plt.show()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
print(f"API Key: {api_key}")