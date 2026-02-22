def ma_strategy(df, short=20, long=50):
    df["ma_s"] = df["Close"].rolling(short).mean()
    df["ma_l"] = df["Close"].rolling(long).mean()
    df["signal"] = (df["ma_s"] > df["ma_l"]).astype(int)
    return df

def rsi_strategy(df, period=14):
    delta = df["Close"].diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = -delta.clip(upper=0).rolling(period).mean()
    rs = gain / loss
    df["rsi"] = 100 - (100 / (1 + rs))
    df["signal"] = (df["rsi"] < 30).astype(int)
    return df
