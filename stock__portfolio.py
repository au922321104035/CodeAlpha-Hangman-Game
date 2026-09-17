# Stock Portfolio Tracker

portfolio = {
    "AAPL": 5,
    "TSLA": 2,
    "GOOGL": 3
}

prices = {
    "AAPL": 225,
    "TSLA": 250,
    "GOOGL": 160
}

total_value = 0

print("----- Stock Portfolio -----")

for stock, quantity in portfolio.items():
    value = quantity * prices[stock]
    total_value += value
    print(stock, "-", quantity, "shares =", "$", value)

print("---------------------------")
print("Total Portfolio Value = $", total_value)