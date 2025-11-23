import re
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
try:
    STOPWORDS = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    STOPWORDS = set(stopwords.words('english'))

WORD_RE = re.compile(r'\b[a-z]{2,}\b')

def clean_and_tokenize(text):
    """
    Cleans and tokenizes text:
    - Lowercase
    - Remove URLs
    - Keep words with 2+ chars
    - Remove stopwords
    """
    if not isinstance(text, str): return []
    text = text.lower()
    text = re.sub(r'http\S+', ' ', text)  # remove urls
    toks = WORD_RE.findall(text)
    toks = [t for t in toks if t not in STOPWORDS]
    return toks
