import requests
import csv
from datetime import datetime

# API URL
API_URL = "https://apewisdom.io/api/v1.0/filter/all-stocks/"

# Function to fetch data
def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Save data to CSV
def save_to_csv(data):
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"apewisdom_{date_str}.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["Date", "Rank", "Ticker", "Name", "Mentions", "Upvotes", "Rank 24h Ago", "Mentions 24h Ago"])
        # Write rows
        for stock in data:
            writer.writerow([
                date_str,
                stock.get("rank"),
                stock.get("ticker"),
                stock.get("name"),
                stock.get("mentions"),
                stock.get("upvotes"),
                stock.get("rank_24h_ago"),
                stock.get("mentions_24h_ago")
            ])
    print(f"Data saved to {filename}")

# Main
if __name__ == "__main__":
    data = fetch_data()
    if data:
        save_to_csv(data)
