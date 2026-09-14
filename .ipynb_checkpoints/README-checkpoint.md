# NLP Unit 1 Programs

A collection of basic Natural Language Processing (NLP) programs implemented using **Python, NLTK, and spaCy**.

This repository contains six practical programs covering fundamental NLP techniques such as tokenization, stemming, lemmatization, stop-word removal, POS tagging, parsing, chunking, and Named Entity Recognition.

---

## 📚 Programs Included

### 1. Tokenization

**Folder:** `01_Tokenization`

Tokenization is the process of breaking text into smaller units called tokens, such as sentences and words.

**Technologies Used:**

* Python
* NLTK
* spaCy

**Concepts Covered:**

* Sentence Tokenization
* Word Tokenization

**File:**
`tokenization.py`

---

### 2. Stemming and Lemmatization

**Folder:** `02_Stemming_Lemmatization`

This program demonstrates two techniques used to convert words into their base or root forms.

**Stemming** removes word endings to obtain a root form.

**Lemmatization** converts a word into its meaningful dictionary base form.

**Technologies Used:**

* Python
* NLTK Porter Stemmer
* spaCy Lemmatizer

**File:**
`stemming_lemmatization.py`

---

### 3. Stop-word Removal

**Folder:** `03_Stopword_Removal`

Stop words are commonly occurring words that may provide little useful information for certain NLP tasks.

Examples include:

`the`, `is`, `a`, `an`, `and`, `of`

This program removes stop words from a given document using NLTK.

**Technology Used:**

* Python
* NLTK

**File:**
`stopword_removal.py`

---

### 4. Part-of-Speech (POS) Tagging

**Folder:** `04_POS_Tagging`

POS tagging assigns a grammatical category to each word in a sentence.

Examples:

* Noun
* Verb
* Adjective
* Adverb
* Preposition
* Determiner

**Technology Used:**

* Python
* NLTK

**File:**
`pos_tagging.py`

---

### 5. Parsing and Chunking

**Folder:** `05_Parsing_Chunking`

This program demonstrates syntactic analysis using regular-expression-based chunking and dependency parsing.

**Concepts Covered:**

* POS Tagging
* Regular Expression Chunking
* Noun Phrase Chunking
* Dependency Parsing
* Grammatical Relationships

**Technologies Used:**

* Python
* NLTK
* spaCy

**File:**
`parsing_chunking.py`

---

### 6. Named Entity Recognition (NER)

**Folder:** `06_Named_Entity_Recognition`

Named Entity Recognition identifies important named entities from text.

Examples of entities include:

* Person
* Organization
* Location
* Date
* Money
* Geopolitical Entity

**Technology Used:**

* Python
* spaCy

**File:**
`ner.py`

---

## 🛠️ Technologies Used

* Python 3
* NLTK
* spaCy
* Natural Language Processing

---

## ⚙️ Installation

Make sure Python is installed on your system.

Install the required libraries:

```bash
pip install nltk spacy
```

Download the spaCy English language model:

```bash
python -m spacy download en_core_web_sm
```

---

## ▶️ How to Run

Navigate to the required program folder or run the Python file from the root directory.

For example:

```bash
python .\01_Tokenization\tokenization.py
```

For Stemming and Lemmatization:

```bash
python .\02_Stemming_Lemmatization\stemming_lemmatization.py
```

Similarly, the other programs can be executed using their respective file paths.

---

## 📂 Repository Structure

```text
NLP Programs/
│
├── 01_Tokenization/
│   └── tokenization.py
│
├── 02_Stemming_Lemmatization/
│   └── stemming_lemmatization.py
│
├── 03_Stopword_Removal/
│   └── stopword_removal.py
│
├── 04_POS_Tagging/
│   └── pos_tagging.py
│
├── 05_Parsing_Chunking/
│   └── parsing_chunking.py
│
├── 06_Named_Entity_Recognition/
│   └── ner.py
│
└── README.md
```

---

## 🎯 Learning Objectives

Through these programs, the following fundamental NLP concepts are demonstrated:

1. Text and word tokenization
2. Sentence tokenization
3. Stemming
4. Lemmatization
5. Stop-word removal
6. Part-of-Speech tagging
7. Parsing
8. Chunking
9. Named Entity Recognition

---

## 👨‍💻 Author

**Amit Pandey**

GitHub: [Amit27181](https://github.com/Amit27181)

---

## 📌 Course Outcome

These practical programs provide hands-on understanding of fundamental Natural Language Processing techniques and their implementation using popular Python NLP libraries.
