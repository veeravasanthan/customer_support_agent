from textblob import TextBlob

def analyze_sentiment(ticket_text):
    polarity = TextBlob(ticket_text).sentiment.polarity

    if polarity < -0.3:
        return "Frustrated"
    elif polarity > 0.3:
        return "Satisfied"
    else:
        return "Neutral"
