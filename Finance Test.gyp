import pandas as pd
import yfinance as yf
import yahoofinancials
tsla_df = yf.download('TSLA', 
                      start='2019-01-01', 
                      end='2019-12-31', 
                      progress=False)
tsla_df.head()
