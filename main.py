from Collectors.twitter_collector import fetch_twitter
from Collectors.reddit_collector import fetch_reddit
from Collectors.telegram_collector import fetch_telegram
from Collectors.mastadon_collector import fetch_mastodon
from Collectors.linkedin_collector import fetch_linkedin

from Utils.cleaner import clean_text, filter_english
from Utils.sentiment import add_sentiment
from Utils.database import save_to_db

import asyncio  # Needed for Telegram async call

def run_pipeline():
    data = []

    # Collect from each platform
    data.extend(fetch_twitter("AI", 10))
    data.extend(fetch_reddit("technology", 10))
    data.extend(fetch_mastodon("osint", 10))
    data.extend(fetch_linkedin("cybersecurity", 10))
    # Telegram is async, so we run it separately
    telegram_data = asyncio.run(fetch_telegram("osint_channel", 10))
    data.extend(telegram_data)

    # Clean and enrich
    for d in data:
        d["text"] = clean_text(d["text"])
    data = filter_english(data)
    data = add_sentiment(data)

    # Store in database
    save_to_db(data)
    print(f"Collected and stored {len(data)} OSINT records.")

if __name__ == "__main__":
    run_pipeline()