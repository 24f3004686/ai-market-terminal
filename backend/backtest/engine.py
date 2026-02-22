def backtest(df):
    df["returns"] = df["Close"].pct_change()
    df["strategy"] = df["signal"].shift(1) * df["returns"]
    df["equity"] = (1 + df["strategy"]).cumprod()
    return df
