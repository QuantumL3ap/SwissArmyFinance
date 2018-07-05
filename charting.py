import historical_data
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("ggplot")

def stockgraph(ticker, past_days=90):

    PAST_DAYS = past_days

    df = historicaldata.daily_adjusted(ticker)

    x = df.index.tolist()
    y = df.values.tolist()
    x = x[-PAST_DAYS:]
    y = y[-PAST_DAYS:]

    plt.plot(x,y)
    plt.xlabel("Date")
    plt.xticks(rotation=90)
    plt.ylabel("Price")
    plt.title(ticker)
    plt.show()


#stockgraph("AAPL", 90)
