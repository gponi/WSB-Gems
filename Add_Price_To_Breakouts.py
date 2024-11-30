import yfinance as yf
import pandas as pd

def fetch_price_trends(breakout_file):
    breakout_df = pd.read_csv(breakout_file)
    price_data = []
    
    for ticker in breakout_df['Ticker']:
        stock = yf.Ticker(ticker)
        history = stock.history(period="7d")  # Get last 7 days
        price_change = (history['Close'][-1] - history['Close'][0]) / history['Close'][0] * 100
        price_data.append({"Ticker": ticker, "7-Day Price Change (%)": price_change})
    
    # Merge with breakout stocks data
    price_df = pd.DataFrame(price_data)
    final_df = pd.merge(breakout_df, price_df, on="Ticker")
    final_df.to_csv("breakout_stocks_with_trends.csv", index=False)
    print("Price trends added. Saved to breakout_stocks_with_trends.csv")

if __name__ == "__main__":
    fetch_price_trends("breakout_stocks.csv")
