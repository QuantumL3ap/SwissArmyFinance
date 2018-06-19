from historical_data import get_stock_dict
import matplotlib
import numpy as np
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
from math import floor, ceil

#helper function that takes a list produce list of dates
def _date_handling(list):
    dates = [matplotlib.dates.datestr2num(str(key)) for key in list]
    return dates

#helper function that takes a list to produce list of prices
def _price_handling(list):
    prices = [round(float(value),2) for value in list]
    return prices

#helper function that takes a ticker and returns stock data
def _chart_data(ticker):
    #use ticker to grab historical data from historical_data.py function
    stock_data = get_stock_dict(ticker)
    dates = np.asarray(_date_handling(stock_data.keys()))
    prices = np.asarray(_price_handling(stock_data.values()))
    #flipping order of array, why is it reverse?
    dates = dates[::-1]
    prices = prices[::-1]
    return dates, prices

def draw_graph(ticker, past_trading_days=100):
    dates, prices = _chart_data(ticker)
    #grabs data for the defined amount of trading days
    dates = dates[-(past_trading_days):]
    prices = prices[-(past_trading_days):]
    fig, ax = plt.subplots()
    ax.plot_date(x=dates, y=prices, fmt="r-")
    plt.yticks(np.arange(floor(min(prices)), ceil((max(prices)) + 2), 1.0))
    formatter = DateFormatter("%d-%m-%y")
    ax.xaxis.set_major_formatter(formatter)
    fig.autofmt_xdate()
    plt.title(ticker)
    fig.canvas.set_window_title(ticker)
    plt.xlabel("Price")
    plt.ylabel("Date")
    plt.show()

#FOR TESTING:
#draw_graph("AAPL")
