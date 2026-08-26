import pandas as pd
import matplotlib.pyplot as plt

assets = ['AAPL', 'GLD', 'JPM', 'SPY', 'XOM'] # desired asset symbols

dataframes = {}
for asset in assets:
    dataframes[asset] = pd.read_csv(f'data/{asset}_daily_data.csv', index_col=0, parse_dates=True)
    dataframes[asset] = dataframes[asset].drop(columns=['1. open', '2. high', '3. low', '5. volume'])

df_all = pd.concat(dataframes.values(), axis=1, keys=dataframes.keys())

df_all.columns = df_all.columns.get_level_values(0)



def individual_info(prices, returns, asset):
    annualised_mean_return = returns[asset].mean() * 252
    annualised_volatility = returns[asset].std() * 252**0.5
    drawdown_max = ((prices[asset] / prices[asset].cummax()) - 1).min()
    return annualised_mean_return, annualised_volatility, drawdown_max



daily_returns = df_all.pct_change().dropna()


analysis = {}

for asset in df_all.columns:
    analysis[asset] = individual_info(df_all, daily_returns, asset)

results = pd.DataFrame.from_dict(analysis, orient='index', columns=['Annualised Mean Return', 'Annualised Volatility', 'Max Drawdown'])
print(f'Analysis Results:\n{results}\n')


correlation_matrix = daily_returns.corr()
print(f'Correlation Matrix:\n{correlation_matrix}\n')

covariance_matrix = daily_returns.cov()*252
print(f'Yearly Covariance Matrix:\n{covariance_matrix}\n')

normalised_prices = df_all / df_all.iloc[0]

rolling_volatility = daily_returns.rolling(window=20).std() * (252**0.5)

fig, axs = plt.subplots(3, 1, figsize=(12, 6))

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

for asset in rolling_volatility.columns:
    axs[2].plot(rolling_volatility.index, rolling_volatility[asset], label = asset)
axs[2].set_xlabel('Date')
axs[2].set_ylabel('Rolling Volatility')
axs[2].set_title('Rolling Volatility Analysis')
axs[2].legend(loc='best')
axs[2].set_xlim(rolling_volatility.index[20], rolling_volatility.index[-1])

plt.tight_layout()
plt.savefig('analysis plots/multi_asset_analysis.png', dpi=300)
plt.show()