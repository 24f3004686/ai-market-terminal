# backend/engine/router.py

from backend.data.crypto import get_crypto_df
from backend.data.stocks import get_stock_data
from backend.indicators.technicals import compute_indicators
from backend.ai.groq_analyzer import ai_analyze

from backend.portfolio.pnl import calculate_pnl
from backend.scanners.top_movers import scan

from backend.backtest.engine import backtest
from backend.backtest.strategies import ma_strategy


# =========================
# ASSET VIEWS
# =========================

def technical_view(cmd):
    """
    Handles:
    BTC USDT TECH
    AAPL US TECH
    """
    asset = cmd["asset"]

    if cmd["market"] == "USDT":
        df = get_crypto_df(asset)
    else:
        df = get_stock_data(asset)

    indicators = compute_indicators(df)
    return ai_analyze(asset, indicators)


def fundamental_view(cmd):
    """
    Placeholder for future fundamental analysis
    """
    return f"Fundamental analysis not implemented yet for {cmd['asset']}"


def news_view(cmd):
    """
    Placeholder for future news sentiment
    """
    return f"News analysis not implemented yet for {cmd['asset']}"


# =========================
# PORTFOLIO VIEWS
# =========================

def portfolio_view(action, prices=None):
    """
    Handles:
    PORTFOLIO SHOW
    PORTFOLIO PNL
    """
    if action == "SHOW":
        return open("backend/portfolio/portfolio.json").read()

    if action == "PNL":
        if prices is None:
            return "Live prices not available for P&L calculation"

        pnl, total = calculate_pnl(prices)

        output = "PORTFOLIO P&L\n\n"
        for sym, data in pnl.items():
            output += f"{sym} : {data['pnl']} USD\n"

        output += f"\nTOTAL P&L: {total} USD"
        return output

    return "Unknown PORTFOLIO command"


# =========================
# SCANNERS
# =========================

def scan_view(cmd):
    """
    Handles:
    SCAN CRYPTO MOVERS
    """
    movers = scan()

    output = "TOP MOVERS (24H)\n\n"
    for m in movers:
        output += f"{m['symbol']} : {m['priceChangePercent']}%\n"

    return output


# =========================
# BACKTESTING
# =========================

def backtest_view(cmd):
    """
    CLI backtest command

    Example:
    BACKTEST BTC USDT MA
    """

    asset = cmd["asset"]

    # Fetch historical data
    df = get_crypto_df(asset)

    # --- Strategy 1: Moving Average ---
    ma_df = ma_strategy(df.copy())
    ma_df = backtest(ma_df)
    ma_return = (ma_df["equity"].iloc[-1] - 1) * 100

    # --- Strategy 2: RSI ---
    from backend.backtest.strategies import rsi_strategy
    rsi_df = rsi_strategy(df.copy())
    rsi_df = backtest(rsi_df)
    rsi_return = (rsi_df["equity"].iloc[-1] - 1) * 100

    return (
        "BACKTEST COMPARISON\n\n"
        f"Asset: {asset}USDT\n\n"
        f"MA Crossover Return : {ma_return:.2f}%\n"
        f"RSI Strategy Return : {rsi_return:.2f}%\n"
    )

# =========================
# MAIN ROUTER
# =========================

def route(cmd, prices=None):
    """
    Central router (Bloomberg-style)
    """

    cmd_type = cmd["type"]

    if cmd_type == "ASSET":
        if cmd["function"] == "TECH":
            return technical_view(cmd)
        if cmd["function"] == "FA":
            return fundamental_view(cmd)
        if cmd["function"] == "NEWS":
            return news_view(cmd)

    if cmd_type == "PORTFOLIO":
        return portfolio_view(cmd["action"], prices)

    if cmd_type == "SCAN":
        return scan_view(cmd)

    if cmd_type == "BACKTEST":
        return backtest_view(cmd)

    return "Invalid command"
