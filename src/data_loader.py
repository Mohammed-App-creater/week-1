import pandas as pd
import numpy as np
from pathlib import Path

def load_csv_memory_friendly(path, sample_frac=None, nrows=None, chunksize=200_000):
    """
    - If sample_frac provided, returns a random sample (read in chunks).
    - If nrows provided, reads only first nrows.
    - Otherwise attempts fast full read.
    """
    path = Path(path)
    if nrows is not None:
        df = pd.read_csv(path, nrows=nrows)
        return df

    # quick attempt to read full file (fast path)
    try:
        df = pd.read_csv(path)
        return df
    except MemoryError:
        # fallback: sample rows streaming
        if sample_frac is None:
            raise MemoryError("File too large to load in memory; provide sample_frac.")
        rng = np.random.default_rng(0)
        chunks = []
        for chunk in pd.read_csv(path, chunksize=chunksize):
            mask = rng.random(chunk.shape[0]) < sample_frac
            if mask.any():
                chunks.append(chunk.loc[mask])
        if chunks:
            return pd.concat(chunks, ignore_index=True)
        else:
            return pd.DataFrame(columns=chunk.columns)
