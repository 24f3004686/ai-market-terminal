import requests

def scan():
    data = requests.get("https://api.binance.com/api/v3/ticker/24hr").json()
    movers = sorted(data, key=lambda x: float(x["priceChangePercent"]), reverse=True)
    return movers[:10]
