import urllib.request
import json

QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&symbol={SYMBOL}&outputsize=full"
API_KEY = "GET API KEY"

#used to make API calls
def _request(symbol, req_type):
    with urllib.request.urlopen(QUERY_URL.format(REQUEST_TYPE=req_type, KEY=API_KEY, SYMBOL=symbol)) as req:
        data = req.read().decode("UTF-8")
    return data

#inputting a stock ticker as a string, it will output a dict of daily data adjusted
def _get_daily_data_adjusted(symbol):
    stock_data = json.loads(_request(symbol, 'TIME_SERIES_DAILY_ADJUSTED'))
    stock_data_format = stock_data["Time Series (Daily)"]
    daily_data_adjusted_dict = []
    for data in stock_data_format.items():
        daily_data_adjusted_dict.append(data)
    return daily_data_adjusted_dict

#inputting a stock ticker as a string, it will output a dict of daily data
def _get_daily_data(symbol):
    stock_data = json.loads(_request(symbol, 'TIME_SERIES_DAILY'))
    stock_data_format = stock_data["Time Series (Daily)"]
    daily_data_dict = []
    for data in stock_data_format.items():
        daily_data_dict.append(data)
    return daily_data_dict

#given a stock ticker, will return a dict of market dates and closing prices
def get_stock_dict(symbol, adjusted=True):
    if adjusted == True:
        requested_stock_data = _get_daily_data_adjusted(symbol)
    elif adjusted == False:
        requested_stock_data = _get_daily_data(symbol)
    else:
        print("Please indicate if you would like non-adjusted data!")
    day = []
    close_price = []
    for market_day in requested_stock_data:
        day.append(market_day[0])
        close_price.append(market_day[1]['4. close'])
    requested_stock_dict = dict(zip(day, close_price))
    return requested_stock_dict

    if __name__ == "__main__":
        pass
