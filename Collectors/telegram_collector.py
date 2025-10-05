from telethon import TelegramClient
from dotenv import load_dotenv
import os, asyncio

load_dotenv()
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")

client = TelegramClient("osint_session", api_id, api_hash)

async def fetch_telegram(channel="osint_updates", limit=10):
    """Fetch messages from a Telegram channel"""
    results = []
    async with client:
        async for msg in client.iter_messages(channel, limit=limit):
            if msg.text:
                results.append({
                    "platform": "telegram",
                    "user": str(msg.sender_id),
                    "timestamp": str(msg.date),
                    "text": msg.text,
                    "url": f"https://t.me/{channel}/{msg.id}"
                })
    return results
