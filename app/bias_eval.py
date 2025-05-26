def detect_bias_keywords(text):
    bias_keywords = [
        "all men are", "all women are",
        "black people", "white people",
        "Muslims are", "Jews are", "Hindus are", "Christians are",
        "Asians are", "Indians are", "Americans are",
        "poor people", "rich people", "immigrants",
    ]

    found = [kw for kw in bias_keywords if kw.lower() in text.lower()]
    score = len(found) / len(bias_keywords)  # normalize
    return round(score, 4), found
