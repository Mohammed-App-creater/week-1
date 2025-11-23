import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from typing import Dict, Union

# Ensure VADER lexicon is downloaded
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

class SentimentAnalyzer:
    """
    A class to perform sentiment analysis on text data.
    """

    def __init__(self):
        """
        Initializes the SentimentAnalyzer with NLTK's VADER.
        """
        self.analyzer = SentimentIntensityAnalyzer()

    def get_sentiment_scores(self, text: str) -> Dict[str, float]:
        """
        Calculates sentiment scores (neg, neu, pos, compound) for a given text.

        Args:
            text (str): The input text.

        Returns:
            Dict[str, float]: A dictionary of sentiment scores.
        """
        if not isinstance(text, str):
            return {'neg': 0.0, 'neu': 0.0, 'pos': 0.0, 'compound': 0.0}
        return self.analyzer.polarity_scores(text)

    def get_compound_score(self, text: str) -> float:
        """
        Calculates the compound sentiment score for a given text.

        Args:
            text (str): The input text.

        Returns:
            float: The compound sentiment score (-1 to 1).
        """
        return self.get_sentiment_scores(text)['compound']
