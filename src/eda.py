import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF


# -------------------------------
# Data Loading
# -------------------------------
def load_data(path: str) -> pd.DataFrame:
    """
    Load CSV data with publication_date parsed into datetime.
    """
    return pd.read_csv(path, parse_dates=['publication_date'])


# -------------------------------
# Descriptive Statistics
# -------------------------------
def add_headline_length(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds column 'headline_length' based on string length of the headline.
    """
    df['headline_length'] = df['headline'].astype(str).str.len()
    return df


def headline_length_stats(df: pd.DataFrame) -> pd.Series:
    """
    Returns descriptive statistics for headline lengths.
    """
    return df['headline_length'].describe()


def publisher_counts(df: pd.DataFrame) -> pd.Series:
    """
    Returns number of articles per publisher.
    """
    return df['publisher'].value_counts()


# -------------------------------
# Time Series Analysis
# -------------------------------
def daily_publication_counts(df: pd.DataFrame) -> pd.Series:
    """
    Returns article counts per day.
    """
    df = df.set_index('publication_date')
    return df.resample('D').size()


def hourly_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Returns number of articles published each hour.
    """
    df['hour'] = df['publication_date'].dt.hour
    return df['hour'].value_counts().sort_index()


# -------------------------------
# Topic Modeling
# -------------------------------
def topic_modeling(
    df: pd.DataFrame,
    text_column: str = "headline",
    n_topics: int = 5,
    n_words: int = 10
):
    """
    Perform topic modeling using TF-IDF + NMF.

    Returns:
        dict: {topic_index: [top_words]}
    """
    docs = df[text_column].astype(str).tolist()

    vectorizer = TfidfVectorizer(
        stop_words='english',
        max_df=0.95,
        min_df=2
    )
    tfidf_matrix = vectorizer.fit_transform(docs)

    nmf = NMF(n_components=n_topics, random_state=42)
    nmf.fit(tfidf_matrix)

    words = vectorizer.get_feature_names_out()
    topics = {}

    for idx, component in enumerate(nmf.components_):
        top_indices = component.argsort()[-n_words:]
        top_words = [words[i] for i in top_indices]
        topics[idx] = top_words

    return topics

