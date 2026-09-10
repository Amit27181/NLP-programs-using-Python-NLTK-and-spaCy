# Stemming and Lemmatization on Sample Text

import nltk
import spacy

nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

text = "The students are studying and playing games. They studied different subjects yesterday."

words = word_tokenize(text)

# ---------------- Stemming ----------------

stemmer = PorterStemmer()

print("========== STEMMING ==========")

for word in words:
    print(word, "->", stemmer.stem(word))


# ---------------- Lemmatization ----------------

print("\n========== LEMMATIZATION ==========")

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)

for token in doc:
    print(token.text, "->", token.lemma_)