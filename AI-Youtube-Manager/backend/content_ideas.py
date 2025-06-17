def generate_ideas(description, titles):
    import random

    themes = [
        "Top 5 tips on {}",
        "Why {} is important",
        "Behind the scenes: {}",
        "How I create content on {}",
        "Q&A on {}",
    ]

    keyword = titles[0] if titles else description.split()[0]  # Fallback
    return [idea.format(keyword) for idea in random.sample(themes, 3)]
