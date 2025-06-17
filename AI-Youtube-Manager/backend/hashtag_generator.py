def generate_hashtags(description, titles):
    from random import sample

    combined_text = description + " " + " ".join(titles)
    
    # Simulate tag generation using keyword presence (real version should use AI model)
    all_possible = ["#Shorts", "#Motivation", "#Tips", "#Viral", "#DailyContent", "#Growth", "#Strategy", "#YouTube"]
    return sample(all_possible, 5)  # Randomize output
