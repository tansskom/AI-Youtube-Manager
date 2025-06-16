import random

def recommend_video_ideas(niche):
    ideas = {
        "Motivation": [
            "5 Habits of Highly Successful People",
            "Morning Routine for Maximum Productivity",
            "Turn Pain into Power — Daily Mindset"
        ],
        "AI": [
            "Top AI Tools You Should Use in 2025",
            "How AI is Changing Content Creation",
            "The Future of AI: Opportunities & Risks"
        ]
    }
    return ideas.get(niche, ["More niche-specific data will be added soon."])
