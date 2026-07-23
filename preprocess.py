import re
import nltk 

nltk.download("stopwords") # Common English words to remove
nltk.download("wordnet") # Vocabulary for lemmatization
nltk.download("punkt") # Tokenizer Rules
nltk.download("punkt_tab")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenize
    tokens = word_tokenize(text)

    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatize: convert it back to root word
    tokens  = [lemmatizer.lemmatize(token) for token in tokens]

    # Join tokens back to string
    return " ".join(tokens)

if __name__ == "__main__":
    print(preprocess("Good direction and writing but the characters weren't a good fit!!!"))