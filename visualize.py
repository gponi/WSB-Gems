import pandas as pd
import matplotlib.pyplot as plt

def visualize_data():
    df = pd.read_csv("breakout_stocks_with_trends.csv")
    df = df.sort_values(by="7-Day Price Change (%)", ascending=False)
    
    plt.figure(figsize=(10, 6))
    plt.bar(df['Ticker'], df['7-Day Price Change (%)'])
    plt.title("7-Day Price Change of Breakout Stocks")
    plt.xlabel("Ticker")
    plt.ylabel("Price Change (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("price_trends_chart.png")
    plt.show()

if __name__ == "__main__":
    visualize_data()
