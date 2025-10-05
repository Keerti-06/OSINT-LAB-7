import re
from langdetect import detect

def clean_text(text):
    """Removes URLs, special symbols, and extra spaces"""
    if not text:
        return ""
    text = re.sub(r"http\S+", "", text)        # remove URLs
    text = re.sub(r"[^A-Za-z0-9\s]", "", text) # remove symbols
    return text.strip()

def filter_english(records):
    """Keep only English language text"""
    filtered = []
    for r in records:
        try:
            if detect(r["text"]) == "en":
                filtered.append(r)
        except:
            pass
    return filtered

