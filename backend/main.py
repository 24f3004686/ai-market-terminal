import threading
import time
from rich.live import Live
from rich.console import Console

from backend.data.crypto_stream import stream_crypto
from backend.engine.live_view import update_price, render_table

console = Console()
paused = False

def start_stream():
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
    stream_crypto(symbols, update_price)

thread = threading.Thread(target=start_stream, daemon=True)
thread.start()

with Live(render_table(), refresh_per_second=2, console=console) as live:
    while True:
        if console.is_terminal:
            time.sleep(0.1)
        live.update(render_table())
