import yfinance as yf
import numpy as np
from utils import *

# Read in tickers from watchlist.txt
tickers = np.genfromtxt('watchlist.txt', dtype=str)

# Read in database
db = load_database()

# Gather option chain data
for ticker in tickers:
    
    yticker = yf.Ticker(ticker)

    ticker_dates = yticker.options
    if len(ticker_dates) == 0:
        print(f"{ticker.upper()} has no options.")
    else:
        if ticker not in db.keys():
            db[ticker] = []

        new = 0
        for date in yticker.options:
            if db is not None and date not in db[ticker]:
                print(f'New option expiry date found for {ticker}: {date}')
                db[ticker].append(date)
                new += 1
        if new == 0:
            print(f"No new option expiry dates found for {ticker}")
            

save_database(db)