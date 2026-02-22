import websocket
import json
import time

paused = False

def stream_crypto(symbols, on_message):
    streams = "/".join([f"{s.lower()}@ticker" for s in symbols])
    url = f"wss://stream.binance.com:9443/stream?streams={streams}"

    def _on_message(ws, message):
        if paused:
            return
        msg = json.loads(message)
        if "data" in msg:
            on_message(msg["data"])

    while True:
        try:
            ws = websocket.WebSocketApp(url, on_message=_on_message)
            ws.run_forever()
        except Exception as e:
            print("WebSocket error, reconnecting...", e)
            time.sleep(5)
