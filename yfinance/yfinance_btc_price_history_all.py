# GET BTC PRICE BY YEAR USING THE YAHOO FINANCE API
# pip install yfinance
import yfinance as yf

def get_btc_full_history():
    # Use the specific Yahoo Finance ticker for Bitcoin
    btc = yf.Ticker("BTC-USD")
    
    # "max" period gets all available historical data
    # "1d" interval ensures you get one closing price per day
    data = btc.history(period="max", interval="1d")
    
    if not data.empty:
        # Filter to only the 'Close' column
        full_history = data[['Close']]
        
        # Display summary info
        print(f"Earliest data found: {full_history.index[0].date()}")
        print(f"Most recent data: {full_history.index[-1].date()}")
        print(f"Total days recorded: {len(full_history)}")
        
        # Save to CSV for external use
        full_history.to_csv("btc_full_history_to_today.csv")
        print("\nSuccess: Data saved to 'btc_full_history_to_today.csv'")
        
        return full_history
    else:
        print("Error: Could not retrieve data.")
        return None

# Run the request
btc_data = get_btc_full_history()
