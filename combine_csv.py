import pandas as pd
import glob

# Combine all CSV files into one DataFrame
def combine_csv_files():
    all_files = glob.glob("apewisdom_*.csv")
    dfs = [pd.read_csv(file) for file in all_files]
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv("apewisdom_combined.csv", index=False)
    print("Combined data saved to apewisdom_combined.csv")

if __name__ == "__main__":
    combine_csv_files()
