def parse_command(cmd):
    parts = cmd.strip().upper().split()

    if parts[0] == "PORTFOLIO":
        return {"type": "PORTFOLIO", "action": parts[1]}

    if parts[0] == "SCAN":
        return {"type": "SCAN", "market": parts[1], "action": parts[2]}

    if parts[0] == "BACKTEST":
        return {
            "type": "BACKTEST",
            "asset": parts[1],
            "market": parts[2],
            "strategy": parts[3]
        }

    return {
        "type": "ASSET",
        "asset": parts[0],
        "market": parts[1],
        "function": parts[2]
    }
