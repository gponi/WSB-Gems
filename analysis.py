import pandas as pd

def analyze_breakout_stocks():
    df = pd.read_csv("apewisdom_combined.csv")
    df['Mentions Change'] = df['Mentions'] - df['Mentions 24h Ago']
    df['Mentions Change (%)'] = (df['Mentions Change'] / df['Mentions 24h Ago']) * 100
    
    # Filter breakout stocks: Mentions increase > 30% and positive sentiment
    breakout_stocks = df[(df['Mentions Change (%)'] > 30) & (df['Mentions'] > 5)]
    
    # Save to a new file
    breakout_stocks.to_csv("breakout_stocks.csv", index=False)
    print("Breakout stocks saved to breakout_stocks.csv")
    print(breakout_stocks)

if __name__ == "__main__":
    analyze_breakout_stocks()
