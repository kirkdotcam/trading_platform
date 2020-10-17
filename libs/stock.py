import pandas as pd
from libs.connection import alpaca

def get_stock(ticker, timeframe="15Min", limit=300, close=False, **kwargs):
    """
    Uses Alpaca API to grab OHLCV information for ticker

    Args:
        ticker(str): stock ticker
        timeframe(str): the time interval between bars. See alpaca api for options (default of 15 mins)
        limit(int): number of bars to grab (default 300 bars)
        close(bool): return only close column
        **kwargs: other keyword arguments for the alpaca API

    Returns: 
        A Pandas Series of alpaca response for get_barset
    """

    ticker= ticker.upper()
    data = alpaca.get_barset(
        ticker,
        timeframe,
        limit,
        **kwargs).df
    

    if close:
        return pd.DataFrame(data[ticker]["close"])
    
    return data

def get_stocks(tickers, close=False,**kwargs):
    """
    Uses get_stock to grab multiple stocks' OHLCV

    Args:
        tickers(list of str): list of tickers as a list of strings
        close(bool): return only closing values
        **kwargs -- see get_stock()

    Returns:
        DataFrame of all stocks in tickers
    """

    tickers = [ticker.upper() for ticker in tickers]

    data = [get_stock(ticker, **kwargs) for ticker in tickers]
    
    df = pd.concat(data, axis="columns", join="inner")

    if close:
        return df.xs("close", axis="columns", level=1)

    return df
