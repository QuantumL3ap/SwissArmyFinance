import json
import pandas as pd
import requests


_BASE_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&symbol={TICKER}&outputsize={OUTPUT_SIZE}&apikey={KEY}"
_API_KEY = ""

def _request(function, ticker, size="full"):

    if function == "daily":
        action = "TIME_SERIES_DAILY"
    elif function == "adaily":
        action = "TIME_SERIES_DAILY_ADJUSTED"
    else:
        print("Please idicate if you would like adjusted or non-adjusted data!")

    _completed_url = _BASE_URL.format(REQUEST_TYPE=action, KEY=_API_KEY, OUTPUT_SIZE=size, TICKER=ticker)
    r = (requests.get(_completed_url)).json()
    data = json.loads(json.dumps(r))

    stock_data = data["Time Series (Daily)"]
    for item in stock_data:
        close_price = stock_data[item]["4. close"]
        stock_data[item] = close_price

    df = pd.DataFrame.from_dict(stock_data, orient="index")
    df = df[::-1] #reversing the dataframe
    df = df.astype(float)

    return df


def daily(ticker):
    data = _request("daily", ticker)
    return data

def daily_adjusted(ticker):
    data = _request("adaily", ticker)
    return data
