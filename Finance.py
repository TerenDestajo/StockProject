import pandas as pd
import yfinance as yf
import yahoofinancials
import yfinance as yf
import datetime as dt 
from datetime import date

#define the ticker symbol
tickerSymbol = input("Give a ticker symbol")

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2019-1-1', end = date.today())

#see your data
tickerDf
tickerData.calendar
tickerData.recommendations
tickerDf.describe()
tickerDf.plot()