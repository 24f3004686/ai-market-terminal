import yfinance as yf

def get_stock_data(symbol):
    data = yf.download(symbol, period="6mo", interval="1d")
    return data
