import requests
from bs4 import BeautifulSoup
import re

def analyze_channel(channel_url):
    try:
        # Normalize URL format
        if "youtube.com/channel/" in channel_url:
            url = channel_url
        elif "youtube.com/c/" in channel_url or "youtube.com/@":
            url = channel_url
        else:
            return {"error": "Unsupported YouTube channel URL format."}

        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            return {"error": "Failed to fetch the channel page."}

        soup = BeautifulSoup(response.text, "html.parser")

        # Try to extract name, subscribers, views, videos, and description
        # Placeholder logic — replace with actual scraping logic or API call
        name = re.search(r'"title":"(.*?)"', response.text)
        name = name.group(1) if name else "Unknown Channel"

        description = re.search(r'"description":{"simpleText":"(.*?)"}', response.text)
        description = description.group(1) if description else "No description available."

        # Return mock/placeholder values for testing
        return {
            "name": name,
            "subscribers": "500K",
            "views": "25M",
            "videos": 120,
            "description": description,
            "recent_titles": ["Top 10 AI Tools", "How to Grow on YouTube", "Productivity Hacks"]
        }

    except Exception as e:
        return {"error": str(e)}
