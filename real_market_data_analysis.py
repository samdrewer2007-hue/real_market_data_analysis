import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

asset = 'AAPL'

df = pd.read_csv("data/" + asset + "_daily_data.csv", index_col=0, parse_dates=True)


#analysis ---------------------------------------------------------------------------


daily_returns = df['4. close'].pct_change()
annualised_mean_return = daily_returns.mean() * 252
annualised_std_return = daily_returns.std() * 252**0.5
print(f"Annualised Mean Return: {annualised_mean_return:.2%}")
print(f"Annualised Standard Deviation of Return: {annualised_std_return:.2%}")

rolling_volatility = daily_returns.rolling(window=20).std() * (252**0.5)

drawdown = (df['4. close'] / df['4. close'].cummax()) - 1
max_drawdown = drawdown.min()
print(f"Maximum Drawdown: {max_drawdown:.2%}")  

cumulative_returns = (1 + daily_returns).cumprod() - 1

log_returns = np.log(df['4. close'] / df['4. close'].shift(1))

# plots ---------------------------------------------------------------------------

fig, axs = plt.subplots(6, 1, figsize=(10, 10))

def lineplot(ax_num, x, y, xlabel, ylabel, title):
    axs[ax_num].plot(x, y)
    axs[ax_num].set_xlabel(xlabel)
    axs[ax_num].set_ylabel(ylabel)
    axs[ax_num].set_title(title)

lineplot(0, df.index, df['4. close'], 'Date', 'Closing Price', asset + ' Closing Price')

axs[1].hist(daily_returns.dropna(), bins=100, edgecolor='black')
axs[1].set_xlabel('Daily Returns')
axs[1].set_ylabel('Frequency')
axs[1].set_title(asset + ' Daily Returns Distribution')

lineplot(2, df.index, rolling_volatility, 'Date', 'Rolling Volatility', asset + ' Rolling Volatility')
lineplot(3, df.index, drawdown, 'Date', 'Drawdown', asset + ' Drawdown')
lineplot(4, df.index, cumulative_returns, 'Date', 'Cumulative Returns', asset + ' Cumulative Returns')
lineplot(5, df.index, log_returns, 'Date', 'Log Returns', asset + ' Log Returns')

plt.tight_layout()
plt.show()

