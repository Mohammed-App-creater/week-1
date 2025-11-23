import pandas as pd
import numpy as np
from typing import Optional

class TechnicalIndicators:
    """
    A class to calculate various technical indicators for financial time series data.
    """

    @staticmethod
    def calculate_rsi(series: pd.Series, period: int = 14) -> pd.Series:
        """
        Calculates the Relative Strength Index (RSI).

        Args:
            series (pd.Series): Time series data (e.g., closing prices).
            period (int, optional): The lookback period. Defaults to 14.

        Returns:
            pd.Series: The RSI values.
        """
        delta = series.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    @staticmethod
    def calculate_sma(series: pd.Series, window: int = 20) -> pd.Series:
        """
        Calculates the Simple Moving Average (SMA).

        Args:
            series (pd.Series): Time series data.
            window (int, optional): The rolling window size. Defaults to 20.

        Returns:
            pd.Series: The SMA values.
        """
        return series.rolling(window=window).mean()

    @staticmethod
    def calculate_macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> pd.DataFrame:
        """
        Calculates the Moving Average Convergence Divergence (MACD).

        Args:
            series (pd.Series): Time series data.
            fast (int, optional): Fast EMA period. Defaults to 12.
            slow (int, optional): Slow EMA period. Defaults to 26.
            signal (int, optional): Signal line EMA period. Defaults to 9.

        Returns:
            pd.DataFrame: DataFrame containing 'macd', 'signal_line', and 'histogram'.
        """
        ema_fast = series.ewm(span=fast, adjust=False).mean()
        ema_slow = series.ewm(span=slow, adjust=False).mean()
        macd = ema_fast - ema_slow
        signal_line = macd.ewm(span=signal, adjust=False).mean()
        histogram = macd - signal_line
        
        return pd.DataFrame({
            'macd': macd,
            'signal_line': signal_line,
            'histogram': histogram
        })
