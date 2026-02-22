import requests
import pandas as pd

def get_crypto_df(asset):
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": asset.upper() + "USDT",
        "interval": "1d",
        "limit": 365
    }

    data = requests.get(url, params=params).json()

    df = pd.DataFrame(
        data,
        columns=[
            "time", "open", "high", "low", "close",
            "volume", "_", "_", "_", "_", "_", "_"
        ]
    )

    df["Close"] = df["close"].astype(float)
    return df
