# Tokenization of Sentences and Words using NLTK and spaCy

import nltk
import spacy

# Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize, word_tokenize

text = "Natural Language Processing is a branch of Artificial Intelligence. It helps computers understand human language."

# ---------------- NLTK ----------------

print("========== NLTK TOKENIZATION ==========")

sentences = sent_tokenize(text)

print("\nSentence Tokenization:")
for sentence in sentences:
    print(sentence)

words = word_tokenize(text)

print("\nWord Tokenization:")
print(words)


# ---------------- spaCy ----------------

print("\n========== SPACY TOKENIZATION ==========")

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)

print("\nSentence Tokenization:")
for sent in doc.sents:
    print(sent.text)

print("\nWord Tokenization:")
for token in doc:
    print(token.text)