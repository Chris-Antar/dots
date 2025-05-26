import yfinance as yf

tickers = ["PLTR","COF","GOOGL","COST","AAPL", "JNJ", "TSLA"]

def get_stock_data():
    """
    Fetches stock data for a list of tickers and returns the percentage changes.
    """
    pcts = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.info
        pcts.append(round(data['regularMarketChangePercent'], 2))
    
    if len(tickers) != len(pcts):
        print("Error: Lists must have the same length.")
        return None
    else:
        return dict(zip(tickers, pcts))



