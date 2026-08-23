import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv(
    "AAPL_daily_data.csv",
    index_col=0,
    parse_dates=True
)
#analysis ---------------------------------------------------------------------------



daily_returns = df['4. close'].pct_change()
annualised_mean_return = daily_returns.mean() * 252
annualised_std_return = daily_returns.std() * 252**0.5
print(f"Annualised Mean Return: {annualised_mean_return}")
print(f"Annualised Standard Deviation of Return: {annualised_std_return}")

rolling_volatility = daily_returns.rolling(window=20).std() * (252**0.5)

drawdown = (df['4. close'] / df['4. close'].cummax()) - 1
max_drawdown = drawdown.min()
print(f"Maximum Drawdown: {max_drawdown}")  

cumulative_returns = (1 + daily_returns).cumprod() - 1

log_returns = np.log(df['4. close'] / df['4. close'].shift(1))

# plots ---------------------------------------------------------------------------

fig, axs = plt.subplots(7, 1, figsize=(10, 10))

axs[0].plot(df.index, daily_returns)
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Daily Returns')
axs[0].set_title('IBM Daily Returns')

axs[1].hist(daily_returns.dropna(), bins=100, edgecolor='black')
axs[1].set_xlabel('Daily Returns')
axs[1].set_ylabel('Frequency')

axs[2].plot(df.index, rolling_volatility)
axs[2].set_xlabel('Date')
axs[2].set_ylabel('Rolling Volatility')

axs[3].plot(df.index, df['4. close'])
axs[3].set_xlabel('Date')
axs[3].set_ylabel('Closing Price')

axs[4].plot(df.index, drawdown)
axs[4].set_xlabel('Date')
axs[4].set_ylabel('Drawdown')
axs[4].set_ylim(drawdown.min(), 0)

axs[5].plot(df.index, cumulative_returns)
axs[5].set_xlabel('Date')
axs[5].set_ylabel('Cumulative Returns')

axs[6].plot(df.index, log_returns)
axs[6].set_xlabel('Date')
axs[6].set_ylabel('Log Returns')

plt.tight_layout()
plt.show()

