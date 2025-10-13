#Gemini Portfolio Tracker
#Author: Chaya M. Goldstein
#Description: Fetches live prices from Gemini and calculates total portfolio value.

from typing import Dict
import requests 

#Maps human-friendly coin names to the Gemini trading pairs (all lowercase):
GEMINI_SYMBOLS: Dict[str, str] = {
    "bitcoin": "btcusd",
    "btc": "btcusd",
    "ethereum": "ethusd",
    "eth": "ethusd",
    "solana": "solusd",
    "sol": "solusd",
    "dogecoin": "dogeusd",
    "doge": "dogeusd",
    "litecoin": "ltcusd",
    "ltc": "ltusd",
    "bitcoin cash": "bchusd",
    "bch": "bchusd",
    }

#Here you can edit your holdings. key = coin label you used, value = amount owned. 
portfolio: Dict[str, float] = {
    "btc": 0.10,
    "eth": 0.50,
    "sol": 3.00
    }

#Fetch price from Gemini:
def gemini_last_price(symbol: str) -> float:
    """Return the most recent USD trade price for a given Gemini trading pair."""
    url = f"https://api.gemini.com/v1/pubticker/{symbol}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json() 
    return float(data["last"]) #Gemini returns numeric fields as strings. 

#Main logic: 
def show_portfolio_value() -> None:
    """Compute and print line items and total portfolio value using Gemini prices ."""
    total = 0.0 
    print("Your Crypto Portfolio (Gemini)\n------------------------------")
    for key, amount in portfolio.items(): 
        symbol = GEMINI_SYMBOLS.get(key.lower())
        if not symbol:
            print(f"- {key}: no Gemini symbol mapped (skip)")
            continue

        try:
            price = gemini_last_price(symbol)
        except requests.RequestException as e:
            print(f"- {key}: error fetching price -> {e}")
            continue

        line_value = price * amount 
        total += line_value 
        print(f"- {key.upper():<8} {amount} x ${price:,.2f} = ${line_value:,.2f}")
    print("------------------------------")
    print(f"Total value: ${total:,.2f}")

if __name__ == "__main__":
    show_portfolio_value()


#Need mapping because Gemini's API doeesn't accept btc or eth, it wants pairs like btcusd.
#The mapping normalizes what you typed to what the API needs.

#If you type a coin that Gemini doesn't list, you'll see "no Gemini symbol mapped (skip)".
#Either add it to GEMINI_SYMBOLS (if a USD pair exists) or remove that holding.

#JSON is the test format for data (looks like Python dicts).
#r.json() converts it to a Python dicct so you can access fields like data["last"].

#rais_for_status() automatically throws an exception for non-success HTTP status code
#so we don't keep going with bad data.


    


    
