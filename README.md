# NLP Unit 1 Programs

A collection of basic **Natural Language Processing (NLP)** practical programs implemented using **Python, NLTK, and spaCy**.

This repository contains six practical programs covering fundamental NLP techniques such as tokenization, stemming, lemmatization, stop-word removal, Part-of-Speech (POS) tagging, parsing, chunking, and Named Entity Recognition (NER).

---

## 📚 Programs Included

### 1. Tokenization

**Folder:** `01_Tokenization`

Tokenization is the process of breaking text into smaller units called tokens, such as sentences and words.

**Technologies Used:**

- Python
- NLTK
- spaCy

**Concepts Covered:**

- Sentence Tokenization
- Word Tokenization

**File:**

`tokenization.ipynb`

---

### 2. Stemming and Lemmatization

**Folder:** `02_Stemming_Lemmatization`

This program demonstrates two techniques used to obtain the base or root form of words.

**Stemming** removes word endings to obtain a root form. It may sometimes produce a non-dictionary word.

**Lemmatization** converts a word into its meaningful dictionary base form.

**Technologies Used:**

- Python
- NLTK Porter Stemmer
- NLTK WordNet Lemmatizer

**Concepts Covered:**

- Porter Stemming
- WordNet Lemmatization

**File:**

`stemming_lemmatization.ipynb`

---

### 3. Stop-word Removal

**Folder:** `03_Stopword_Removal`

Stop words are commonly occurring words that may provide little useful information for certain NLP tasks.

Examples include:

`the`, `is`, `a`, `an`, `and`, `of`

This program removes stop words from a given document using NLTK.

**Technologies Used:**

- Python
- NLTK

**Concepts Covered:**

- Word Tokenization
- Stop-word Identification
- Stop-word Removal

**File:**

`stopword_removal.ipynb`

---

### 4. Part-of-Speech (POS) Tagging

**Folder:** `04_POS_Tagging`

Part-of-Speech (POS) tagging assigns a grammatical category to each word in a sentence.

**Examples:**

- Noun
- Verb
- Adjective
- Adverb
- Preposition
- Determiner

**Technologies Used:**

- Python
- NLTK

**Concepts Covered:**

- Word Tokenization
- POS Tagging
- Grammatical Categories

**File:**

`pos_tagging.ipynb`

---

### 5. Parsing and Chunking

**Folder:** `05_Parsing_Chunking`

This program demonstrates syntactic analysis using regular-expression-based chunking and dependency parsing.

**Concepts Covered:**

- POS Tagging
- Regular Expression Chunking
- Noun Phrase Chunking
- Dependency Parsing
- Grammatical Relationships

**Technologies Used:**

- Python
- NLTK
- spaCy

**File:**

`parsing_chunking.ipynb`

---

### 6. Named Entity Recognition (NER)

**Folder:** `06_Named_Entity_Recognition`

Named Entity Recognition (NER) identifies and classifies important named entities from text.

**Examples of Entities:**

- Person
- Organization
- Location
- Date
- Money
- Geopolitical Entity

**Technologies Used:**

- Python
- spaCy

**Concepts Covered:**

- Named Entity Recognition
- Entity Classification
- Entity Labels

**File:**

`ner.ipynb`

---

## 🛠️ Technologies Used

- Python 3
- NLTK
- spaCy
- Jupyter Notebook
- Natural Language Processing

---

## ⚙️ Installation

Make sure Python is installed on your system.

### Install Required Libraries

```bash
pip install nltk spacy
```

### Download the spaCy English Language Model

```bash
python -m spacy download en_core_web_sm
```

### NLTK Resources

The required NLTK resources are downloaded by the respective notebooks.

These include:

- `punkt`
- `punkt_tab`
- `stopwords`
- `averaged_perceptron_tagger_eng`
- `wordnet`
- `omw-1.4`

---

## ▶️ How to Run

These programs are implemented as **Jupyter Notebooks (`.ipynb`)**.

You can run them using:

- Jupyter Notebook
- JupyterLab
- Google Colab
- VS Code with the Jupyter extension

### Start Jupyter Notebook

```bash
jupyter notebook
```

Then open the required notebook and execute the cells sequentially.

For example:

```text
01_Tokenization/tokenization.ipynb
```

Similarly, open the notebooks for the other NLP practicals.

---

## 📂 Repository Structure

```text
NLP-Unit-1-Programs/
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
└── README.md
```

---

## 🎯 Learning Objectives

Through these programs, the following fundamental NLP concepts are demonstrated:

1. Sentence Tokenization
2. Word Tokenization
3. Stemming
4. Lemmatization
5. Stop-word Removal
6. Part-of-Speech (POS) Tagging
7. Parsing
8. Chunking
9. Named Entity Recognition (NER)

---

## 🎓 Course Outcome

These practical programs provide hands-on understanding of fundamental Natural Language Processing techniques and their implementation using popular Python NLP libraries.

The programs demonstrate how raw text can be processed, transformed, and analyzed using different NLP techniques.

---

## 👨‍💻 Author

**Amit Pandey**

GitHub: [Amit27181](https://github.com/Amit27181)

---

## 📌 Note

This repository is created for academic and practical learning purposes and demonstrates basic NLP concepts using Python, NLTK, and spaCy.