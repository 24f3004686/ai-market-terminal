import json

def load_portfolio():
    with open("backend/portfolio/portfolio.json") as f:
        return json.load(f)

def calculate_pnl(prices):
    portfolio = load_portfolio()
    results = {}
    total_pnl = 0.0

    for symbol, pos in portfolio.items():
        if symbol not in prices:
            continue

        current_price = prices[symbol]["price"]
        pnl = (current_price - pos["avg_price"]) * pos["quantity"]

        results[symbol] = {
            "pnl": round(pnl, 2),
            "current_price": current_price
        }

        total_pnl += pnl

    return results, round(total_pnl, 2)
