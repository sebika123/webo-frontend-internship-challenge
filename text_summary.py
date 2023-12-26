
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
import requests

import requests
from bs4 import BeautifulSoup

def get_text_from_link(link):
    try:
       
        response = requests.get(link)
        response.raise_for_status() 

        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content from the parsed HTML
        text_content = soup.get_text(separator=' ', strip=True)
        
        return text_content
    except requests.RequestException as e:
        # Handle request errors (e.g., link not accessible)
        return f"Error fetching content from link: {e}"


def textrank_summarizer(rawdocs, percentage=30):
    nlp = spacy.load('en_core_web_sm')
    stop_words = set(STOP_WORDS)
    doc = nlp(rawdocs)
    sentences = [sent.text.lower() for sent in doc.sents if sent.text.lower() not in stop_words]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    similarity_matrix = (X * X.T).toarray()

    G = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(G)

    ranked_sentences = sorted(((scores[i], sent) for i, sent in enumerate(sentences)), reverse=True)
    select_len = int(len(ranked_sentences) * (percentage / 100))
    selected_sentences = [sent for _, sent in ranked_sentences[:select_len]]

    summary = ' '.join(selected_sentences)

    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))


