from rich.table import Table
from rich.text import Text

prices = {}

def update_price(data):
    symbol = data["s"]
    prices[symbol] = {
        "price": float(data["c"]),
        "change": float(data["P"])
    }

def render_table():
    table = Table(title="Live Crypto Prices", expand=True)
    table.add_column("Symbol")
    table.add_column("Price", justify="right")
    table.add_column("Change %", justify="right")

    if not prices:
        table.add_row("Waiting...", "-", "-")
        return table

    for s, v in list(prices.items()):
        change = v["change"]

        if change > 0:
            arrow = "▲"
            style = "green"
        elif change < 0:
            arrow = "▼"
            style = "red"
        else:
            arrow = ""
            style = "white"

        change_text = Text(f"{arrow} {change:.2f}%", style=style)

        table.add_row(
            s,
            f"{v['price']:.2f}",
            change_text
        )

    return table
