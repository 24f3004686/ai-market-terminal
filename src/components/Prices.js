import { useEffect, useState } from "react";

export default function Prices() {
  const [data, setData] = useState({});

  useEffect(() => {
    const i = setInterval(() => {
      fetch("http://localhost:8000/prices")
        .then(r => r.json())
        .then(setData);
    }, 1000);
    return () => clearInterval(i);
  }, []);

  return (
    <div className="panel">
      <h3>Live Crypto</h3>
      {Object.entries(data).map(([k,v]) =>
        <div key={k}>{k} {v.price.toFixed(2)} ({v.change.toFixed(2)}%)</div>
      )}
    </div>
  );
}
