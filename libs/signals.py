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
def bollinger(close,sma=20, std=2):
    """
    returns df of bollinger band signal generation
    """

    close["bol_mid"] = close["close"].rolling(20).mean()
    band_std = close["close"].std()

    close["bol_up"] = close["bol_mid"] + std*band_std
    close["bol_low"] = close["bol_mid"] - std*band_std
    close["band_dist"] = close["bol_up"] - close["bol_low"]
    close["band_dist_delta"] = close["band_dist"].diff()
    close["percent_b"] = (close["close"]- close["bol_low"])/close["band_dist"]

    def bol_percent_sig(row):
        if row > 1:
            return 1
        elif row < 0:
            return -1
        else:
            return 0

    close["percent_b_sig"] = close["percent_b"].apply(bol_percent_sig)

    return close