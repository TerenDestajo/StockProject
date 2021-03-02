import requests

demo = 'your_api'

tickers = requests.get(f'https://fmpcloud.io/api/v3/symbol/available-nasdaq?apikey={demo}')

tickers = tickers.json()
symbols = []
for ticker in tickers:
    symbols.append(ticker['symbol'])
#print(symbols)