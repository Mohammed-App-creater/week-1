import re
import nltk
from nltk.corpus import stopwords
from typing import List, Optional

# Ensure stopwords are downloaded
try:
    STOPWORDS = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    STOPWORDS = set(stopwords.words('english'))

WORD_RE = re.compile(r'\b[a-z]{2,}\b')

class TextProcessor:
    """
    A class to handle text cleaning and preprocessing tasks.
    """

    @staticmethod
    def clean_and_tokenize(text: str) -> List[str]:
        """
        Cleans and tokenizes text:
        - Lowercase
        - Remove URLs
        - Keep words with 2+ chars
        - Remove stopwords

        Args:
            text (str): The input text to clean.

        Returns:
            List[str]: A list of tokens.
        """
        if not isinstance(text, str): return []
        text = text.lower()
        text = re.sub(r'http\S+', ' ', text)  # remove urls
        toks = WORD_RE.findall(text)
        toks = [t for t in toks if t not in STOPWORDS]
        return toks

