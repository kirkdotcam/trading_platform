#~/anaconda3/envs/zip/bin/python
from libs import plots
from libs import stock
import matplotlib.pyplot as plt
import sys

args = sys.argv[1:]
print(args)
if len(args) < 2:
    print("need more args")
    exit()


command = args[0]
tickers = args[1:]

# commands start here
if command == "research":
    ticker = tickers[0]
    plots.SignalPlot(ticker).generate_plots()
    exit()

if command == "price":
    print(stock.get_stocks(tickers, close=True).iloc[-1])
    exit()

if command == "trade":
    print("not yet implemented")
    exit()

if command == "account":
    print("not yet implemented")
    exit()

print("invalid command")
exit()
