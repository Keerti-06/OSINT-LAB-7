import discord
import sqlite3
import asyncio

# --- CONFIG ---
TOKEN = "Your_Token"
channel_id = Any channel id

# --- INTENTS ---
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# --- DATABASE SETUP ---
conn = sqlite3.connect('osint.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS discord_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        timestamp TEXT,
        text TEXT,
        url TEXT
    )
''')
conn.commit()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    try:
        channel = await client.fetch_channel(channel_id)
        count = 0
        async for message in channel.history(limit=100):
            if message.content and not message.author.bot:
                cursor.execute('''
                    INSERT INTO discord_messages (user, timestamp, text, url)
                    VALUES (?, ?, ?, ?)
                ''', (
                    str(message.author),
                    str(message.created_at),
                    message.content,
                    f"https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}"
                ))
                conn.commit()
                count += 1

        print(f"Fetched and stored {count} messages.")
    except Exception as e:
        print(f"Error fetching messages: {e}")
    finally:
        await client.close()

@client.event
async def on_disconnect():
    print("Disconnected cleanly")

client.run(TOKEN)
