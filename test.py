import yfinance as yf
import pandas as pd

stocks = pd.read_csv('snp500.csv')

for ticker in stocks['ticker']:        
    data = yf.download(tickers = ticker, period = "1y", interval='1d', progress=False).reset_index().dropna()
    print(data.head())
    print(1/0)