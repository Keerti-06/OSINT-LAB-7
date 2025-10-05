from mastodon import Mastodon
from dotenv import load_dotenv
import os

load_dotenv()
MASTODON_TOKEN = os.getenv("Your Mastodon Token")

mastodon = Mastodon(
    access_token=MASTODON_TOKEN,
    api_base_url="https://mastodon.social"
)

def fetch_mastodon(hashtag="osint", limit=10):
    """Fetch posts from Mastodon with a hashtag"""
    results = []
    posts = mastodon.timeline_hashtag(hashtag, limit=limit)
    for p in posts:
        results.append({
            "platform": "mastodon",
            "user": p["account"]["username"],
            "timestamp": str(p["created_at"]),
            "text": p["content"],
            "url": p["url"]
        })
    return results

