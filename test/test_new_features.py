import unittest
import pandas as pd
import numpy as np
from src.technical_indicators import TechnicalIndicators
from src.sentiment_analysis import SentimentAnalyzer

class TestTechnicalIndicators(unittest.TestCase):
    def setUp(self):
        self.data = pd.Series([10, 12, 11, 13, 15, 14, 16, 18, 17, 19, 21, 20, 22, 24, 23])

    def test_sma(self):
        sma = TechnicalIndicators.calculate_sma(self.data, window=5)
        self.assertTrue(pd.isna(sma[3]))
        self.assertAlmostEqual(sma[4], 12.2)

    def test_rsi(self):
        rsi = TechnicalIndicators.calculate_rsi(self.data, period=14)
        # Not enough data for full RSI calculation with period 14, but checking structure
        self.assertEqual(len(rsi), len(self.data))

    def test_macd(self):
        macd_df = TechnicalIndicators.calculate_macd(self.data, fast=12, slow=26, signal=9)
        self.assertIn('macd', macd_df.columns)
        self.assertIn('signal_line', macd_df.columns)
        self.assertIn('histogram', macd_df.columns)

class TestSentimentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SentimentAnalyzer()

    def test_sentiment_scores(self):
        text = "This is a great day for the stock market!"
        scores = self.analyzer.get_sentiment_scores(text)
        self.assertGreater(scores['pos'], 0)
        self.assertGreater(scores['compound'], 0)

    def test_compound_score(self):
        text = "The market crashed badly."
        score = self.analyzer.get_compound_score(text)
        self.assertLess(score, 0)

if __name__ == '__main__':
    unittest.main()
