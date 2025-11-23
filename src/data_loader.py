import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional

class DataLoader:
    """
    A class to handle data loading operations with memory optimization techniques.
    """

    @staticmethod
    def load_csv_memory_friendly(
        path: str, 
        sample_frac: Optional[float] = None, 
        nrows: Optional[int] = None, 
        chunksize: int = 200_000
    ) -> pd.DataFrame:
        """
        Loads a CSV file into a pandas DataFrame with options for sampling and chunking 
        to handle large files efficiently.

        Args:
            path (str): The file path to the CSV file.
            sample_frac (float, optional): The fraction of rows to return (0.0 to 1.0). 
                                           If provided, reads the file in chunks and samples.
            nrows (int, optional): The number of rows to read from the beginning of the file.
            chunksize (int, optional): The number of rows per chunk when reading in chunks. 
                                       Defaults to 200,000.

        Returns:
            pd.DataFrame: The loaded data.

        Raises:
            MemoryError: If the file is too large to load without sampling and no sample_frac is provided.
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

