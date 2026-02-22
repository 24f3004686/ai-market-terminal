# AI Market Terminal

A Bloomberg-style market terminal built with **FastAPI** and **React**.

## Features
- Real-time crypto prices (Binance WebSocket)
- Live market movers scanner
- Strategy backtesting (MA, RSI)
- Equity curve visualization
- Dark terminal-style UI
- Clean backend–frontend architecture

## Tech Stack
- Python (FastAPI)
- WebSockets
- React (Create React App)
- Chart.js
- Binance API

## How to Run

### Backend
bash
source venv/Scripts/activate
pip install -r requirements.txt
uvicorn web.app:app

## Frontend
cd web/terminal-ui
npm install
npm start

## Create a .env file in the project root:
GROQ_API_KEY=your_api_key_here
