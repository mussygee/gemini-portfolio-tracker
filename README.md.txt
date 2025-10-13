# Gemini Portfolio Tracker

A lightweight Python script that fetches **live crypto prices** from Gemini’s public API and calculates total portfolio value.

## 💻 Features
- Maps friendly tickers (e.g., `btc`, `eth`) to Gemini trading pairs (e.g., `btcusd`, `ethusd`)
- Fetches real-time prices with Gemini’s `/v1/pubticker/<symbol>` endpoint
- Handles network errors gracefully
- Displays holdings and total value in clean, formatted output

## ⚙️ Tech Used
- **Python 3.10+**
- **Requests** library

## 🧠 How to Run
1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install requests
3. Edit holdings inside PORTFOLIO in gemini_portfolio.py
4. Run: 
   python gemini_portfolio.py

🧾 Example Output:

Your Crypto Portfolio (Gemini)
--------------------------------
- BTC    0.1 × $114,656.37 = $11,465.64
- ETH    0.5 × $4,172.41   = $2,086.20
- SOL    3.0 × $202.01     = $606.04
--------------------------------
Total value: $14,157.88

📈 Future Improvements

Command-line input for dynamic holdings

Export to CSV or JSON

Flask dashboard or chart visualization

👩‍💻 Author

Chaya M. Goldstein
Computer Science Major @ Touro University

