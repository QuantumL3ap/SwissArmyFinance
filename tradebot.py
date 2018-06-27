import random

#needs to have a constant flow of data
def _streamed_quotes(args):
    #do somethings to format data
    pass

def _share_price(ticker):
        #test value to see if working, would need to fetch price
        _spot_price = random.randint(5, 100)
        print(_spot_price)
        return _spot_price

def _average_cost(botname, ticker, price, sale=False):
    #new_total_cost = botname.avg[ticker][0] + price
    if sale == False:
        _new_total = botname.avg[ticker][0] + price
        _new_avg = _new_total / botname.positions[ticker]
        return _new_total, _new_avg
    elif sale == True:
        _new_total = botname.avg[ticker][0] - price
        _new_avg = _new_total / botname.positions[ticker]
        return _new_total, _new_avg



class Bot:

    def __init__(self, cash):
        self.cash = cash #gives the bot a starting amount of money
        self.positions = {} #initially has no positions
        #avg sturcture {'TICKER': (TOTAL_COST, AVERAGE_COST_PSHARE)}
        self.avg = {} #initially has no avg
        self.pandl = {}



    def buy(self, ticker, shares):
        price = shares * _share_price(ticker) #gets current price
        if self.cash >= price: #checks if bot has enough cash
            self.cash = self.cash - price
            if ticker in self.positions: #checks if postion already exists
                self.positions[ticker] = self.positions[ticker] + shares
                self.avg[ticker] = _average_cost(self, ticker, price)
            else:
                self.positions[ticker] = shares #creates new dict entry if DNE
                self.avg[ticker] = [price, price / shares]
        else:
            print("Not enough capital!")



    def sell(self, ticker, shares):
        price = shares * _share_price(ticker) #gets current price
        if ticker in self.positions and shares <= self.positions[ticker]:
            self.cash = self.cash + price
            self.positions[ticker] = self.positions[ticker] - shares
            _profit_loss = price - (self.avg[ticker][1] * shares) #gain or loss
            if ticker in self.pandl:
                self.pandl[ticker] = self.pandl[ticker] + _profit_loss
            else:
                self.pandl[ticker] = _profit_loss
            self.avg[ticker] = _average_cost(self, ticker, price, sale=True)
        else:
            print("You do not have enough shares to sell!")



    def market_value(self, ticker=''): #can get total value or a ticker's value
        if ticker == '':
            TOTAL_VALUE = 0
            for _key, _value in self.positions.items(): #iterates through positions
                TOTAL_VALUE = TOTAL_VALUE + (_value * _share_price(_key))
            return TOTAL_VALUE
        elif ticker in self.positions: #if ticker exists, get its current value
            TOTAL_VALUE = self.positions[ticker] * _share_price(ticker)
            return TOTAL_VALUE
        else:
            print("Please specify a ticker you own, or leave blank for total!")



    def pandl(self, ticker=''):
        pass



bot = Bot(1000) #initializes bot with starting cash

bot.buy("AAPL", 3) #examples of buying and selling
bot.buy("AAPL", 4)
bot.sell("AAPL", 2)
bot.sell("AAPL", 2)
#bot.buy("AMD", 4)
#bot.sell("AMD", 1)

print(bot.pandl)

print(bot.market_value()) #getting market value of positions
#print(bot.market_value("AMD")) #getting market value of a position

print(bot.positions) #getting all positions
#print(bot.avg["AAPL"])
#print(bot.cash) #getting available cash
#print(bot.avg)

#Have to fix gain and loss calc
