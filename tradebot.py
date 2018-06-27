#needs to have a constant flow of data
def _streamed_quotes(args):
    #do somethings to format data
    pass

def _share_price(ticker):
        #test value to see if working, would need to fetch price
        ticker = 100
        return ticker

class Bot:

    def __init__(self, cash):
        self.cash = cash #gives the bot a starting amount of money
        self.positions = {} #initially has no positions

    def buy(self, ticker, shares):
        price = shares * _share_price(ticker) #gets current price
        if self.cash >= price: #checks if bot has enough cash
            self.cash = self.cash - price
            if ticker in self.positions: #checks if postion already exists
                self.positions[ticker] = self.positions[ticker] + shares
            else:
                self.positions[ticker] = shares #creates new dict entry if DNE
        else:
            print("Not enough capital!")
        return self.cash, self.positions

    def sell(self, ticker, shares):
        price = shares * _share_price(ticker) #gets current price
        if ticker in self.positions:
            self.cash = self.cash + price
            self.positions[ticker] = self.positions[ticker] - shares
        else:
            pass #FOR SHORTING
        return self.cash, self.positions

    def market_value(self):
        TOTAL_VALUE = 0
        for key in self.positions.values():
            print(key)
            TOTAL_VALUE = TOTAL_VALUE + key * _share_price(key)
        return TOTAL_VALUE


#bot = Bot(1000)

#bot.buy("AAPL", 2)
#bot.buy("AAPL", 4)
#bot.buy("AMD", 4)
#bot.sell("AMD", 1)


#print(bot.positions, bot.cash, bot.market_value())
