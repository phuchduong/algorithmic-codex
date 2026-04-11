# GET BTC PRICE BY YEAR USING THE YAHOO FINANCE API
# pip install yfinance
import yfinance as yf

def get_btc_yearly_closing_2025():
    # Bitcoin ticker
    btc = yf.Ticker("BTC-USD")
    
    # Define the range for the full year 2025
    # Remember: end date is exclusive, so we use Jan 1st, 2026
    start_date = "2025-01-01"
    end_date = "2026-01-01"
    
    # Fetch daily data
    data = btc.history(start=start_date, end=end_date, interval="1d")
    
    if not data.empty:
        # We only need the 'Close' column
        closing_prices = data[['Close']]
        
        # Display the first few rows
        print("First 5 days of 2025:")
        print(closing_prices.head())
        
        # Optionally save to a CSV file
        closing_prices.to_csv("btc_closing_2025.csv")
        print("\nFull year saved to btc_closing_2025.csv")
        
        return closing_prices
    else:
        print("No data found for the year 2025.")
        return None

# Run the function
btc_2025 = get_btc_yearly_closing_2025()
print(btc_2025)