import pandas as pd
import ta

def compute_indicators(df):
    df["rsi"] = ta.momentum.RSIIndicator(df["Close"]).rsi()
    df["macd"] = ta.trend.MACD(df["Close"]).macd()
    df["volatility"] = df["Close"].pct_change().std()

    return {
        "RSI": round(df["rsi"].iloc[-1], 2),
        "MACD": round(df["macd"].iloc[-1], 2),
        "Volatility": round(df["volatility"], 4)
    }
