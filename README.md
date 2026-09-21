# NLP Programs using Python, NLTK and spaCy

A collection of practical **Natural Language Processing (NLP)** programs implemented using **Python, NLTK, spaCy, and Jupyter Notebook**.

This repository contains practical programs covering fundamental NLP concepts from **CO1 and CO2**, including tokenization, stemming, lemmatization, stop-word removal, POS tagging, parsing, chunking, Named Entity Recognition, Bag of Words, TF-IDF, N-Grams, and Cosine Similarity.

---

## 📚 Programs Included

### 🔹 CO1 – Fundamental NLP Techniques

### 1. Tokenization

**Folder:** `01_Tokenization`

Demonstrates the process of breaking text into smaller units called tokens.

**Concepts Covered:**

* Sentence Tokenization
* Word Tokenization

**Technologies:**

* Python
* NLTK
* spaCy

**File:** `tokenization.ipynb`

---

### 2. Stemming and Lemmatization

**Folder:** `02_Stemming_Lemmatization`

Demonstrates techniques used to obtain the base or root form of words.

**Concepts Covered:**

* Porter Stemming
* WordNet Lemmatization
* Difference between Stemming and Lemmatization

**Technologies:**

* Python
* NLTK

**File:** `stemming_lemmatization.ipynb`

---

### 3. Stop-word Removal

**Folder:** `03_Stopword_Removal`

Demonstrates the identification and removal of commonly occurring words that may provide limited information for certain NLP tasks.

**Examples:**

* `the`
* `is`
* `a`
* `an`
* `and`
* `of`

**Concepts Covered:**

* Word Tokenization
* Stop-word Identification
* Stop-word Removal

**Technologies:**

* Python
* NLTK

**File:** `stopword_removal.ipynb`

---

### 4. Part-of-Speech (POS) Tagging

**Folder:** `04_POS_Tagging`

Assigns grammatical categories to words in a sentence.

**Examples:**

* Noun
* Verb
* Adjective
* Adverb
* Preposition
* Determiner

**Concepts Covered:**

* Word Tokenization
* POS Tagging
* Grammatical Categories

**Technologies:**

* Python
* NLTK

**File:** `pos_tagging.ipynb`

---

### 5. Parsing and Chunking

**Folder:** `05_Parsing_Chunking`

Demonstrates syntactic analysis using chunking and dependency parsing.

**Concepts Covered:**

* POS Tagging
* Regular Expression Chunking
* Noun Phrase Chunking
* Dependency Parsing
* Grammatical Relationships

**Technologies:**

* Python
* NLTK
* spaCy

**File:** `parsing_chunking.ipynb`

---

### 6. Named Entity Recognition (NER)

**Folder:** `06_Named_Entity_Recognition`

Identifies and classifies named entities from text.

**Examples of Entities:**

* Person
* Organization
* Location
* Date
* Money
* Geopolitical Entity

**Concepts Covered:**

* Named Entity Recognition
* Entity Classification
* Entity Labels

**Technologies:**

* Python
* spaCy

**File:** `ner.ipynb`

---

# 🔹 CO2 – Text Vectorization and Similarity

### 7. Bag of Words (BoW)

**Folder:** `08_Bag_of_Words`

Demonstrates the Bag of Words model for converting text documents into numerical feature vectors.

**Concepts Covered:**

* Vocabulary Creation
* Term Frequency
* Document-Term Matrix
* Text Vectorization

**Technologies:**

* Python
* Scikit-learn

**File:** `bow.ipynb`

---

### 8. TF-IDF

**Folder:** `09_TF_IDF`

Demonstrates Term Frequency-Inverse Document Frequency (TF-IDF) for assigning importance to words in documents.

**Concepts Covered:**

* Term Frequency (TF)
* Inverse Document Frequency (IDF)
* TF-IDF Vectorization
* Document-Term Matrix

**Technologies:**

* Python
* Scikit-learn

**File:** `tfidf.ipynb`

---

### 9. N-Gram Model

**Folder:** `10_N_Gram`

Demonstrates N-Gram models for analyzing sequences of words in text.

**Concepts Covered:**

* Unigram
* Bigram
* Trigram
* N-Gram Generation

**Technologies:**

* Python
* NLTK

**File:** `ngram.ipynb`

---

### 10. Cosine Similarity

**Folder:** `11_Cosine_Similarity`

Demonstrates cosine similarity for measuring the similarity between text documents represented as numerical vectors.

**Concepts Covered:**

* Vector Representation
* Dot Product
* Vector Magnitude
* Cosine Similarity
* Text Similarity

**Technologies:**

* Python
* Scikit-learn

**File:** `cosine_similarity.ipynb`

---

## 🛠️ Technologies Used

* Python 3
* NLTK
* spaCy
* Scikit-learn
* Jupyter Notebook
* Natural Language Processing

---

## ⚙️ Installation

Make sure Python is installed on your system.

### Install Required Libraries

```bash
pip install nltk spacy scikit-learn
```

### Download the spaCy English Language Model

```bash
python -m spacy download en_core_web_sm
```

### NLTK Resources

The required NLTK resources are downloaded by the respective notebooks.

These may include:

* `punkt`
* `punkt_tab`
* `stopwords`
* `averaged_perceptron_tagger_eng`
* `wordnet`
* `omw-1.4`

---

## ▶️ How to Run

These programs are implemented as **Jupyter Notebooks (`.ipynb`)**.

You can run them using:

* Jupyter Notebook
* JupyterLab
* Google Colab
* VS Code with the Jupyter extension

### Start Jupyter Notebook

```bash
jupyter notebook
```

Then open the required notebook and execute the cells sequentially.

---

## 📂 Repository Structure

```text
NLP-programs-using-Python-NLTK-and-spaCy/
│
├── 01_Tokenization/
│   └── tokenization.ipynb
│
├── 02_Stemming_Lemmatization/
│   └── stemming_lemmatization.ipynb
│
├── 03_Stopword_Removal/
│   └── stopword_removal.ipynb
│
├── 04_POS_Tagging/
│   └── pos_tagging.ipynb
│
├── 05_Parsing_Chunking/
│   └── parsing_chunking.ipynb
│
├── 06_Named_Entity_Recognition/
│   └── ner.ipynb
│
├── 08_Bag_of_Words/
│   └── bow.ipynb
│
├── 09_TF_IDF/
│   └── tfidf.ipynb
│
├── 10_N_Gram/
│   └── ngram.ipynb
│
├── 11_Cosine_Similarity/
│   └── cosine_similarity.ipynb
│
└── README.md
```

---

## 🎯 Learning Objectives

Through these practical programs, the following NLP concepts are demonstrated:

### CO1

1. Sentence Tokenization
2. Word Tokenization
3. Stemming
4. Lemmatization
5. Stop-word Removal
6. POS Tagging
7. Parsing
8. Chunking
9. Named Entity Recognition

### CO2

10. Bag of Words
11. TF-IDF
12. N-Gram Models
13. Cosine Similarity
14. Text Vectorization
15. Text Similarity

---

## 🎓 Course Outcome

These practical programs provide hands-on understanding of fundamental **Natural Language Processing** techniques and their implementation using popular Python libraries.

The programs demonstrate how raw text can be **processed, transformed into numerical representations, and analyzed** using different NLP techniques.

---

## 👨‍💻 Author

**Amit Pandey**

GitHub: [Amit27181](https://github.com/Amit27181)

---

## 📌 Note

This repository is created for **academic and practical learning purposes** and demonstrates fundamental NLP concepts using Python, NLTK, spaCy, and Scikit-learn.
