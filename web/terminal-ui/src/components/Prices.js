import { useEffect, useState } from "react";

export default function Prices() {
  const [data, setData] = useState({});

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://localhost:8000/prices")
        .then(res => res.json())
        .then(json => setData(json))
        .catch(() => {}); // ignore transient fetch errors
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="panel">
      <h3>Live Crypto Prices</h3>

      {Object.keys(data).length === 0 && (
        <div>Waiting for prices...</div>
      )}

      {Object.entries(data).map(([symbol, v]) => {
        // ✅ DEFENSIVE CHECKS
        const price =
          typeof v?.price === "number" ? v.price.toFixed(2) : "--";

        const change =
          typeof v?.change === "number" ? v.change.toFixed(2) : "--";

        const color =
          typeof v?.change === "number"
            ? v.change > 0
              ? "lime"
              : v.change < 0
              ? "red"
              : "white"
            : "white";

        const arrow =
          typeof v?.change === "number"
            ? v.change > 0
              ? "▲"
              : v.change < 0
              ? "▼"
              : ""
            : "";

        return (
          <div key={symbol} style={{ color }}>
            {symbol} {price} {arrow} {change}%
          </div>
        );
      })}
    </div>
  );
}
