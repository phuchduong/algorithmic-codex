# GET BTC PRICE BY DATE USING THE YAHOO FINANCE API
# pip install yfinance
import yfinance as yf
from datetime import datetime, timedelta

def get_btc_price_yfinance(date_yyyy_mm_dd):
    btc = yf.Ticker("BTC-USD")
    
    # Convert string to datetime object to calculate the next day
    start_date = datetime.strptime(date_yyyy_mm_dd, "%Y-%m-%d")
    end_date = start_date + timedelta(days=1)
    
    # Use the next day as the exclusive end point
    data = btc.history(start=start_date.strftime("%Y-%m-%d"), 
                       end=end_date.strftime("%Y-%m-%d"))
    
    if not data.empty:
        price = data["Close"].iloc[0]
        print(f"BTC Price on {date_yyyy_mm_dd}: ${price:,.2f} USD")
        return price
    else:
        print(f"No data found for {date_yyyy_mm_dd}. (Check if date is in the future)")
        return None

# Usage
btc_price = get_btc_price_yfinance("2025-01-01")
