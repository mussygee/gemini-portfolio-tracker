# Gemini Portfolio Tracker
A Python-based command-line tool that fetches **live cryptocurrency prices** from Gemini’s public API and computes the real-time value of a crypto portfolio.
The project emphasizes API integration, error handling, data normalization, and clean, readable output.

## 🚀 Project Overview
Gemini Portfolio Tracker allows users to define crypto holdings using human-friendly tickers (e.g., btc, eth, sol) and calculates the total portfolio value using live market data from Gemini.

The script demonstrates how to:
- Interact with a real-world REST API
- Normalize user input to API-specific requirements
- Handle network and data errors safely
- Present financial data in a clean, formatted CLI output
- 
## 💻 Features
- Live price fetching using Gemini’s public /v1/pubticker endpoint
- Ticker normalization (maps btc → btcusd, eth → ethusd, etc.)
- Graceful error handling for unsupported coins and failed API calls
- Formatted portfolio breakdown with per-asset and total value
- Simple, extensible design for future features

## 🧠 Design & Implementation Details
**API Integration**
- Uses the requests library to fetch live price data
- Implements timeouts and HTTP status checks to avoid hanging or invalid responses
- Parses JSON responses and converts numeric strings into floats for calculations

**Symbbol Mapping**
Gemini’s API requires explicit trading pairs (e.g., btcusd) rather than shorthand tickers (btc).
To solve this, the project uses a centralized mapping dictionary that:
- Normalizes user input
- Prevents invalid API requests
- Makes it easy to extend support for additional assets

**Error Handling**
- Unsupported tickers are skipped with a clear message.
- Network or API errors are caught and reported without crashing the program.


## 🛠️ Tech Stack
- **Python 3.10+**
- **Requests** (HTTP client)
- Public Gemini REST API
- Standard library (typing, formatting utilities)

## 🧠 How to Run
1. Clone this repository:
   git clone https://github.com/yourusername/gemini-portfolio-tracker
   cd gemini-portfolio-tracker

3. Install dependencies:
   pip install requests
   
5. Edit holdings inside PORTFOLIO in gemini_portfolio.py
   portfolio = {
    "btc": 0.10,
    "eth": 0.50,
    "sol": 3.00
}

7. Run the script: 
   python gemini_portfolio.py

🧾 Example Output:

Your Crypto Portfolio (Gemini)
--------------------------------
- BTC    0.1 × $114,656.37 = $11,465.64
- ETH    0.5 × $4,172.41   = $2,086.20
- SOL    3.0 × $202.01     = $606.04
--------------------------------
Total value: $14,157.88

## 📈 Future Improvements
- Command-line input for dynamic portfolio entries
- Export portfolio data to CSV or JSON
- Flask or Streamlit dashboard for visualization
- Support for additional exchanges

## 👩‍💻 Author

Chaya M. Goldstein
Computer Science Major @ Touro University
