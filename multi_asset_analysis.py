import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df_AAPL = pd.read_csv("data/AAPL_daily_data.csv", index_col=0, parse_dates=True)
df_GLD = pd.read_csv("data/GLD_daily_data.csv", index_col=0, parse_dates=True)
df_JPM = pd.read_csv("data/JPM_daily_data.csv",index_col=0, parse_dates=True)
df_SPY = pd.read_csv("data/SPY_daily_data.csv", index_col=0, parse_dates=True)
df_XOM = pd.read_csv("data/XOM_daily_data.csv", index_col=0, parse_dates=True)

df_AAPL = df_AAPL.drop(columns=['1. open', '2. high', '3. low', '5. volume'])
df_GLD = df_GLD.drop(columns=['1. open', '2. high', '3. low', '5. volume'])
df_JPM = df_JPM.drop(columns=['1. open', '2. high', '3. low', '5. volume'])
df_SPY = df_SPY.drop(columns=['1. open', '2. high', '3. low', '5. volume'])
df_XOM = df_XOM.drop(columns=['1. open', '2. high', '3. low', '5. volume'])

df_all = pd.concat([df_AAPL, df_GLD, df_JPM, df_SPY, df_XOM], axis=1, keys=['AAPL', 'GLD', 'JPM', 'SPY', 'XOM'])
df_all.columns = df_all.columns.get_level_values(0)



def individual_info(prices, returns, asset):
    annualised_mean_return = returns[asset].mean() * 252
    annualised_volatlilty = returns[asset].std() * 252**0.5
    drawdown_max = ((prices[asset] / prices[asset].cummax()) - 1).min()
    return annualised_mean_return, annualised_volatlilty, drawdown_max



daily_returns = df_all.pct_change()
daily_returns = daily_returns.dropna()
print(daily_returns.head())

analysis = {}

for asset in df_all.columns:
    analysis[asset] = individual_info(df_all, daily_returns, asset)

for asset in df_all.columns:
    print(f'Annualised mean return for {asset}: {analysis[asset][0]:.2%}')
    print(f'Annualised volatility for {asset}: {analysis[asset][1]:.2%}')
    print(f'Max drawdown for {asset}: {analysis[asset][2]:.2%}')
    print('-----------------------------')

correlation_matrix = daily_returns.corr()
print(correlation_matrix)

covariance_matrix = daily_returns.cov()
print(covariance_matrix)

normalised_prices = df_all / df_all.iloc[0]



fig, axs = plt.subplots(2, 1, figsize=(12, 6))

for asset in normalised_prices.columns:
    axs[0].plot(normalised_prices.index, normalised_prices[asset], label=asset)
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Normalised Price')
axs[0].set_title('Multi-Asset Price Analysis')
axs[0].legend(loc='best')
axs[0].set_xlim(normalised_prices.index[0], normalised_prices.index[-1])

for asset in daily_returns.columns:
    axs[1].plot(analysis[asset][1], analysis[asset][0], 'o', label=asset)
axs[1].set_xlabel('Annualised Volatility')
axs[1].set_ylabel('Annualised Mean Return')
axs[1].set_title('Risk-Return Analysis')
axs[1].legend()
axs[1].set_xlim(0, daily_returns.std().max() * 252**0.5 + 0.05)
axs[1].set_ylim(daily_returns.mean().min() * 252 - 0.05, daily_returns.mean().max() * 252 + 0.05)

plt.tight_layout()
plt.savefig('multi_asset_price_analysis.png', dpi=300)
plt.show()