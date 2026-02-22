import { useEffect, useState } from "react";

export default function Movers() {
  const [m, setM] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/movers")
      .then(r => r.json())
      .then(setM);
  }, []);

  return (
    <div className="panel">
      <h3>Top Movers</h3>
      {m.map(x =>
        <div key={x.symbol}>
          {x.symbol} {x.priceChangePercent}%
        </div>
      )}
    </div>
  );
}
