# Parsing and Chunking using RegEx and spaCy

import nltk
import spacy

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.chunk import RegexpParser


sentence = "The intelligent student solved the difficult problem quickly."

# Tokenization
words = word_tokenize(sentence)

# POS Tagging
pos_tags = pos_tag(words)

print("========== POS TAGGING ==========")

for word, tag in pos_tags:
    print(word, "->", tag)


# ---------------- REGEX CHUNKING ----------------

print("\n========== REGEX CHUNKING ==========")

grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>}
"""

chunk_parser = RegexpParser(grammar)

tree = chunk_parser.parse(pos_tags)

print(tree)

print("\nNoun Phrases:")

for subtree in tree.subtrees():
    if subtree.label() == "NP":
        print(" ".join(word for word, tag in subtree.leaves()))


# ---------------- SPACY PARSING ----------------

print("\n========== SPACY DEPENDENCY PARSING ==========")

nlp = spacy.load("en_core_web_sm")

doc = nlp(sentence)

for token in doc:
    print(
        f"{token.text:12} "
        f"POS={token.pos_:8} "
        f"DEP={token.dep_:10} "
        f"HEAD={token.head.text}"
    )