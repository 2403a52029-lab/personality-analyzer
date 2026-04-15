from textblob import TextBlob

def analyze_personality(text):
    blob = TextBlob(text)

    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Personality logic
    if polarity > 0.3:
        mood = "Positive 😊"
    elif polarity < -0.3:
        mood = "Negative 😔"
    else:
        mood = "Neutral 😐"

    if subjectivity > 0.5:
        personality = "Emotional / Expressive"
    else:
        personality = "Logical / Objective"

    return {
        "mood": mood,
        "personality": personality,
        "polarity": round(polarity, 2),
        "subjectivity": round(subjectivity, 2)
    }