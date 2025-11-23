import sys
import os
sys.path.append(os.path.abspath("src"))

from data_loader import load_csv_memory_friendly
from text_cleaning import clean_and_tokenize
from eda_helpers import plot_top_publishers
import pandas as pd

# Load a sample
print("Loading data...")
df = load_csv_memory_friendly("data/raw/raw_analyst_ratings.csv", nrows=10000)
print(f"Loaded {len(df)} rows.")

# Check columns
print("Columns:", df.columns.tolist())

# Clean text
print("Cleaning text...")
df['tokens'] = df['headline'].astype(str).apply(clean_and_tokenize)
print("Sample tokens:", df['tokens'].iloc[0])

# Top publishers
print("Top publishers:")
print(df['publisher'].value_counts().head(5))

print("Verification complete.")
