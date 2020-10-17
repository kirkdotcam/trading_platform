import pandas as pd
import libs.signals as signals
import libs.stock as stock
import matplotlib.pyplot as plt


class SignalPlot():

    def __init__(self, ticker=None, data=None):
        if data:
            self.data = data
            self.ticker = "unknown"
        else:
            self.ticker = ticker
            self.data = stock.get_stock(ticker, close=True)
            
    def bollinger_plot(self):
        df = signals.bollinger(self.data)
        return df[["bol_mid","bol_up", "bol_low"]].plot(title=f"{self.ticker} Bollinger bands")

    def macd_plot(self):
        df = signals.MACD(self.data)
        return df[["macd","macd_sig"]].plot(title=f"{self.ticker} MACD")

    def generate_plots(self):

        bollinger_plot()
        macd_plot()
        return plt.show()
