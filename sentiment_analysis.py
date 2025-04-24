from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def analyze_sentiments(comments):
    analyzer = SentimentIntensityAnalyzer()
    results = []

    for c in comments:
        score = analyzer.polarity_scores(c)
        compound = score['compound']
        sentiment = 'Positive' if compound > 0.05 else 'Negative' if compound < -0.05 else 'Neutral'
        results.append({'comment': c, 'compound': compound, 'sentiment': sentiment})
    
    return pd.DataFrame(results)
print("✅ Module loaded correctly")
