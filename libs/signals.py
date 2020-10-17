import pandas as pd

#MACD
def MACD(close, fast=12, slow=26, signal_lag=9):
    """
    Calculates MACD and returns the MACD, its signal, the convergence/divergence
    """
    close["macd_fast"] = close["close"].ewm(span=fast).mean()
    close["macd_slow"] = close["close"].ewm(span=slow).mean()
    close["macd"] = close["macd_slow"] - close["macd_fast"]
    close["macd_sig"] = close["macd"].rolling(signal_lag).mean()
    close["diverge"] = close["macd"] - close["macd_sig"]
    close["macd_div_sign"] = (close["diverge"] > 0).astype(int)
    return close


#Bollinger Band
def bband():