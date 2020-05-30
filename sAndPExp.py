#! /usr/bin/env python

import bs4 as bs
import datetime as dt
import os
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr
import pickle
import requests
from sAndP import save_sp500_tickers #pretty important
yf.pdr_override()

def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("storage/sp500tickers.pickle","rb") as f:
            tickers = pickle.load(f)
    
    if not os.path.exists('storage/stock_dfs'):
        os.makedirs('storage/stock_dfs')
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2020,5,29)

    for ticker in tickers[:10]:
        print(ticker)
        if not os.path.exists('storage/stock_dfs/{}.csv'.format(ticker)):
            df = pdr.get_data_yahoo(ticker, start, end)
            df.to_csv('storage/stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()