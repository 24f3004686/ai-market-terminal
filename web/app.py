from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import threading

from backend.data.crypto_stream import stream_crypto
from backend.engine.live_view import update_price, prices

app = FastAPI(title="AI Market Terminal API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- START WEBSOCKET ON SERVER START ----------------
@app.on_event("startup")
def start_price_stream():
    def run_stream():
        symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
        stream_crypto(symbols, update_price)

    thread = threading.Thread(target=run_stream, daemon=True)
    thread.start()

# ---------------- ROUTES ----------------

@app.get("/")
def root():
    return {"status": "API running"}

@app.get("/prices")
def get_prices():
    return prices

@app.get("/movers")
def movers():
    from backend.scanners.top_movers import scan
    return scan()

@app.get("/backtest/{asset}")
def backtest_api(asset: str):
    from backend.data.crypto import get_crypto_df
    from backend.backtest.strategies import ma_strategy
    from backend.backtest.engine import backtest

    df = get_crypto_df(asset)
    df = ma_strategy(df)
    df = backtest(df)

    return {
        "equity": df["equity"].fillna(1).tolist()
    }
