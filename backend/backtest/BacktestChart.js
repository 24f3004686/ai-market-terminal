import { Line } from "react-chartjs-2";
import { useEffect, useState } from "react";

export default function BacktestChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/backtest/BTC")
      .then(r => r.json())
      .then(d => setData(d.equity));
  }, []);

  return (
    <Line
      data={{
        labels: data.map((_, i) => i),
        datasets: [{
          label: "Equity Curve",
          data,
          borderColor: "#00ff99"
        }]
      }}
    />
  );
}
