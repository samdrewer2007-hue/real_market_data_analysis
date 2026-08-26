# Real market data analysis
This project uses Pandas and Matplotlib to examine, analyse and compare past market data for AAPL, JPM, XOM, GLD and SPY.

## Overview
The data is sourced from Alpha Vantage, which allows us to find the last 100 days of stock data. From this, a free API key was generated, then stored locally. This data is requested, converted to a DataFrame and cleaned, then saved as a CSV by 'fetch_market_data.py', to avoid using up the 25 free data requests provided by Alpha Vantage. This data is then suitable to be analysed by 'single_asset_analysis.py' and 'multi_asset_analysis.py'.

## Analysis

For each asset, single_asset_analysis.py calculated:
- Daily returns
- Annualised mean return
- Annualised volatility
- 20-day rolling volatility
- Drawdown 
- Cumulative returns
- Log returns

It also plots closing price, return distribution, rolling volatility, drawdown, cumulative returns and log returns using Matplotlib.


Furthermore, multi_asset_analysis compares the five assets by calculating:
- Annualised mean return/volatility 
- Maximum drawdown 
- Normalised prices
- Correlation matrix
- Annualised covariance matrix

It also plots  their normalised prices, a risk-return scatter, and each asset's 20-day rolling volatility.

## Results
| Asset | Annualised Mean Return | Annualised Volatility | Max Drawdown |
|---|---:|---:|---:|
| AAPL | 54.62% | 28.93% | -12.71% |
| GLD | -1.19% | 24.40% | -18.16% |
| JPM | 47.65% | 21.22% | -6.72% |
| SPY | 42.45% | 13.08% | -4.49% |
| XOM | -2.70% | 29.14% | -19.80% |

![Multi-Asset Analysis](analysis%20plots/multi_asset_analysis.png)

Over the 100-day period this project analysed, AAPL showed the highest annualised mean return, but also a relatively high volatility, second only to XOM. Two of the five assets, XOM and GLD, produced negative annualised mean returns and also experienced the largest maximum drawdowns. SPY was the least volatile asset across this period and had the smallest maximum drawdown, while still showing a strong positive return.

These results are however only based on a relatively short historical sample, so all annual data should be interpreted as scaled estimates rather than accurate long-term data.