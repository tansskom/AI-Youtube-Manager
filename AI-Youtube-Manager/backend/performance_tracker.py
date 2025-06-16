import random

def track_performance(channel_id):
    return {
        "Views Last 7 Days": random.randint(1000, 100000),
        "Watch Time": f"{random.randint(500, 5000)} hours",
        "Average CTR": f"{random.uniform(2, 10):.2f}%",
        "Subscriber Growth": random.randint(100, 1000),
        "Next Steps": [
            "Experiment with shorts",
            "Optimize thumbnails",
            "Run A/B testing on titles"
        ]
    }
