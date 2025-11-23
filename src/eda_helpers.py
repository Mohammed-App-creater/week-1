import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def plot_headline_length(df, save_path=None):
    plt.figure(figsize=(8,4))
    sns.histplot(df['headline_len'], bins=50)
    plt.title("Headline length distribution")
    plt.xlabel("length (chars)")
    plt.ylabel("count")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()

def plot_top_publishers(df, top_k=30, save_path=None):
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

def plot_articles_over_time(daily_counts, save_path=None):
    plt.figure(figsize=(12,4))
    plt.plot(daily_counts['date'], daily_counts['n_articles'])
    plt.title("Articles per day (time series)")
    plt.xlabel("date")
    plt.ylabel("n_articles")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()

def plot_weekday_distribution(df, save_path=None):
    plt.figure(figsize=(8,4))
    order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    sns.countplot(x='weekday', data=df, order=order)
    plt.title("Articles by weekday")
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()
