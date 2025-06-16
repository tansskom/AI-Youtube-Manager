from googleapiclient.discovery import build

API_KEY = 'AIzaSyAl4VFOx8WopcNtFZgREhqcV0Id4JOXeKc'  # <-- Replace with your actual API key

def analyze_channel(channel_url):
    # Extract channel ID from URL
    if "channel/" in channel_url:
        channel_id = channel_url.split("channel/")[1].split("/")[0]
    else:
        return {"error": "Invalid channel URL format"}

    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id
    )
    response = request.execute()

    if not response['items']:
        return {"error": "Channel not found."}

    channel = response['items'][0]
    stats = channel['statistics']
    snippet = channel['snippet']

    return {
        "channel_name": snippet.get("title"),
        "subscribers": stats.get("subscriberCount"),
        "views": stats.get("viewCount"),
        "videos": stats.get("videoCount"),
        "description": snippet.get("description"),
    }
