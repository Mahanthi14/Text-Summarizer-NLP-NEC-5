import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def summarize_text(text, num_sentences=3):

    if not text.strip():
        return "Please enter some text."

    # Pandas DataFrame
    df = pd.DataFrame({
        "text": [text]
    })

    # Split into sentences
    sentences = text.replace("\n", " ").split(".")

    sentences = [s.strip() for s in sentences if s.strip()]

    if len(sentences) <= num_sentences:
        return text

    # Scikit-learn TF-IDF
    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(sentences)

    # NumPy scores
    sentence_scores = np.array(
        tfidf_matrix.sum(axis=1)
    ).flatten()

    # Top sentences
    top_indices = sentence_scores.argsort()[-num_sentences:]

    top_indices = sorted(top_indices)

    summary = ". ".join(
        [sentences[i] for i in top_indices]
    )

    return summary + "."