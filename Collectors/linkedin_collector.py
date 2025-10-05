from serpapi import GoogleSearch

def fetch_linkedin(query="cybersecurity", limit=10):
    params = {
        "engine": "google",
        "q": f"site:linkedin.com/posts {query}",
        "api_key": "Your SerpAPI Key"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    linkedin_data = []
    for i, result in enumerate(results.get("organic_results", [])[:limit]):
        linkedin_data.append({
            "platform": "linkedin",
            "user": result.get("title", "unknown"),
            "timestamp": "2025-10-04T21:50:00",
            "text": result.get("snippet", ""),
            "url": result.get("link", "")
        })


    return linkedin_data
