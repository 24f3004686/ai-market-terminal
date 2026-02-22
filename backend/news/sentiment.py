from ai.groq_analyzer import ai_analyze

def analyze_sentiment(headlines):
    text = "\n".join(headlines)
    return ai_analyze("NEWS", text)
