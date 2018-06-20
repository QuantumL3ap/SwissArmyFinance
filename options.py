from math import sqrt

#function that accepts a stock price, IV, and DTE to computer expected move
def expected_move(price, IV, DTE):
    std_dev = round((price * (IV / 100) * sqrt(DTE / 365)), 2)
    high_price = price + std_dev
    low_price = price - std_dev
    return low_price, high_price

print(expected_move(200, 40, 30))
