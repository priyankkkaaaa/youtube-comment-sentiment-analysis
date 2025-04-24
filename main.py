from fetch_comments import get_comments
from sentiment_analysis import analyze_sentiments
from visualize import plot_sentiments

import pandas as pd  # Needed for saving CSV

# Replace these with your actual key and video ID
API_KEY = 'AIzaSyCznsYfQkRx48vHf_-d4N9Z4PaYzMfWD1g'
VIDEO_ID = '5URefVYaJrA'

def main():
    print("Fetching comments...")
    comments = get_comments(VIDEO_ID, API_KEY)

    print(f"Fetched {len(comments)} comments.")
    
    print("Analyzing sentiments...")
    df = analyze_sentiments(comments)
    
    print(df.head())

    print("Visualizing...")
    plot_sentiments(df)

    # ✅ Saving to CSV for Power BI
    output_file = "sentiment_results.csv"
    df.to_csv(output_file, index=False)
    print(f"✅ Results saved to {output_file}")

if __name__ == "__main__":
    main()
