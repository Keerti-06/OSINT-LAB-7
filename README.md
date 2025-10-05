# OSINT-LAB-7
**Description**
A modular Python-based OSINT pipeline for collecting and analyzing publicly available data from social media platforms. Includes platform-specific collectors, sentiment analysis, SQLite storage, and visualizations. Designed for scalable, cross-platform intelligence gathering and real-time insights.

**Objectives**
1. Access social media APIs for automated OSINT data collection.
2. Design a modular Python pipeline with multiple collectors.
3. Perform data cleaning, language detection, and sentiment analysis.
4. Store collected data in a structured SQLite database.
5. Visualize insights (e.g., sentiment by platform).

**Features**
1. Multi-platform data collection (Twitter, Reddit, LinkedIn, Telegram, Mastodon, Discord)
2. Text cleaning and English language filtering.
3. Sentiment analysis using TextBlob.
4. SQLite database integration (osint.db).
5. Visualization using Matplotlib.
6. Modular & reusable code structure.
7. Secure environment variable storage (.env)

**Project Structure**
osint_pipeline/
│── main.py
│── .env
│── collectors/
│    ├── twitter_collector.py
│    ├── reddit_collector.py
│    ├── linkedin_collector.py
│    ├── telegram_collector.py
│    ├── mastodon_collector.py
│    ├── discord_collector.py
│── utils/
│    ├── cleaner.py
│    ├── database.py
│    ├── sentiment.py
│    ├── visualizer.py
│── data/
│    └── osint.db

**Installation**
_Prerequisites_
-> Python 3.9+
-> pip (Python package manager)
-> Developer / API credentials for the supported platforms
-> Active internet connection

_Step-by-Step Installation_
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/osint-pipeline.git
cd osint-pipeline
2️⃣ Create a Virtual Environment
python -m venv osint_env
osint_env\Scripts\activate      # for Windows
# or
source osint_env/bin/activate   # for Mac/Linux
3️⃣ Install Dependencies
pip install -r requirements.txt
(If requirements.txt not present, create it with pip freeze > requirements.txt)

_Configuration_
Environment Variables
Create a file named .env in the root directory with your API credentials:
# Twitter API
TWITTER_KEY=your_twitter_key
TWITTER_SECRET=your_twitter_secret

# Reddit API
REDDIT_ID=your_reddit_client_id
REDDIT_SECRET=your_reddit_client_secret

# LinkedIn (Unofficial API)
LINKEDIN_EMAIL=your_email_here
LINKEDIN_PASSWORD=your_password_here

# Telegram API
TELEGRAM_API_ID=your_telegram_api_id
TELEGRAM_API_HASH=your_telegram_api_hash

# Discord Bot
DISCORD_TOKEN=your_discord_token_here

# Mastodon API
MASTODON_TOKEN=your_mastodon_token_here

**Usage**
Run the Complete Pipeline
python osint_pipeline/main.py
This will:
-> Collect posts from all configured platforms
-> Clean and filter text
-> Add sentiment analysis
-> Save everything to data/osint.db






