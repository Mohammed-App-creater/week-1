from src.eda import add_headline_length, headline_length_stats
import pandas as pd


def test_headline_length_stats_basic():
    data = {
        'headline': ['short', 'much longer headline'],
        'publisher': ['A', 'B'],
        'publication_date': ['2024-01-01', '2024-01-02']
    }
    df = pd.DataFrame(data)
    df['publication_date'] = pd.to_datetime(df['publication_date'])

    df = add_headline_length(df)
    stats = headline_length_stats(df)

    # basic assertions
    assert stats['count'] == 2
    assert stats['min'] == len('short')
