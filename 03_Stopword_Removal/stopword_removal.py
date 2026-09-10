# Stop-word Removal from a Document using NLTK

import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = """
Natural Language Processing is an important field of Artificial Intelligence.
It helps computers understand and process human language.
"""

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_words = [
    word for word in words
    if word.lower() not in stop_words
]

print("========== ORIGINAL TEXT ==========")
print(text)

print("========== WORDS ==========")
print(words)

print("\n========== AFTER STOP-WORD REMOVAL ==========")
print(filtered_words)