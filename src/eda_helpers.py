import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, List
import pandas as pd

class Visualizer:
    """
    A class to handle various plotting and visualization tasks for EDA.
    """

    @staticmethod
    def plot_headline_length(df: pd.DataFrame, save_path: Optional[str] = None) -> None:
        """
        Plots the distribution of headline lengths.

        Args:
            df (pd.DataFrame): DataFrame containing a 'headline_len' column.
            save_path (str, optional): Path to save the figure.
        """
        plt.figure(figsize=(8,4))
        sns.histplot(df['headline_len'], bins=50)
        plt.title("Headline length distribution")
        plt.xlabel("length (chars)")
        plt.ylabel("count")
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=150)
        plt.show()

    @staticmethod
    def plot_top_publishers(df: pd.DataFrame, top_k: int = 30, save_path: Optional[str] = None) -> pd.Series:
        """
        Plots the top K publishers by article count.

        Args:
            df (pd.DataFrame): DataFrame containing a 'publisher' column.
            top_k (int, optional): Number of top publishers to show. Defaults to 30.
            save_path (str, optional): Path to save the figure.

        Returns:
            pd.Series: The counts of the top publishers.
        """
        publisher_counts = df['publisher'].value_counts(dropna=True)
        plt.figure(figsize=(8,10))
        publisher_counts.head(top_k).sort_values().plot(kind='barh')
        plt.title(f"Top {top_k} publishers by article count")
        plt.xlabel("count")
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=150)
        plt.show()
        return publisher_counts

    @staticmethod
    def plot_articles_over_time(daily_counts: pd.DataFrame, save_path: Optional[str] = None) -> None:
        """
        Plots the number of articles over time.

        Args:
            daily_counts (pd.DataFrame): DataFrame with 'date' and 'n_articles' columns.
            save_path (str, optional): Path to save the figure.
        """
        plt.figure(figsize=(12,4))
        plt.plot(daily_counts['date'], daily_counts['n_articles'])
        plt.title("Articles per day (time series)")
        plt.xlabel("date")
        plt.ylabel("n_articles")
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=150)
        plt.show()

    @staticmethod
    def plot_weekday_distribution(df: pd.DataFrame, save_path: Optional[str] = None) -> None:
        """
        Plots the distribution of articles by weekday.

        Args:
            df (pd.DataFrame): DataFrame containing a 'weekday' column.
            save_path (str, optional): Path to save the figure.
        """
        plt.figure(figsize=(8,4))
        order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        sns.countplot(x='weekday', data=df, order=order)
        plt.title("Articles by weekday")
        if save_path:
            plt.savefig(save_path, dpi=150)
        plt.show()

