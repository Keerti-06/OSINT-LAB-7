import tweepy, os
from dotenv import load_dotenv

# Load .env from Osint_Pipeline folder
env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=env_path)

TWITTER_BEARER = os.getenv("TWITTER_BEARER")

client = tweepy.Client(bearer_token=TWITTER_BEARER)

def fetch_twitter(query="AI", limit=10):
    limit = max(10, min(limit, 100))  # Ensure limit is between 10 and 100

    results = []
    try:
        tweets = client.search_recent_tweets(
            query=query,
            max_results=limit,
            tweet_fields=["created_at", "author_id"]
        )
        if tweets.data:
            for tweet in tweets.data:
                results.append({
                    "platform": "twitter",
                    "user": str(tweet.author_id),
                    "timestamp": str(tweet.created_at),
                    "text": tweet.text,
                    "url": f"https://twitter.com/i/web/status/{tweet.id}"
                })
        else:
            print("No tweets found.")
    except Exception as e:
        print("Error fetching tweets:", e)

    return results

print(fetch_twitter("AI", 10))