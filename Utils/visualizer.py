import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

def plot_sentiment(db_path="C:/Users/Kirti/PycharmProjects/OSINT_LAB 7/Osint_Pipeline/data/osint.db"):
    """Visualize average sentiment by platform from OSINT DB"""

    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql("SELECT * FROM osint_data", conn)
        conn.close()
    except Exception as e:
        print(f"Error reading database: {e}")
        return

    if df.empty or "text" not in df.columns:
        print("No data or missing 'text' column.")
        return

    # Clean and compute sentiment
    df["text"] = df["text"].fillna("")
    df["sentiment"] = df["text"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

    # Summary print
    print("Sentiment calculated for", len(df), "records.")
    print(df.groupby("platform")["sentiment"].describe())

    # Plot
    sentiment_by_platform = df.groupby("platform")["sentiment"].mean().sort_values()
    plt.figure(figsize=(10, 5))
    bars = plt.bar(sentiment_by_platform.index, sentiment_by_platform.values, color='mediumseagreen')
    plt.title("Average Sentiment by Platform", fontsize=14)
    plt.ylabel("Sentiment Score (-1 to 1)")
    plt.xlabel("Platform")
    plt.grid(axis='y', linestyle='--', alpha=0.5)

    # Annotate bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}", ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_sentiment()