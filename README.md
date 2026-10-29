# Natural Language Processing Programs Using Python, NLTK and spaCy

A structured collection of **32 Natural Language Processing (NLP) practical programs** implemented using Python, NLTK, spaCy, Scikit-learn, and Hugging Face Transformers.

This repository covers fundamental NLP techniques, text representation, machine learning, deep learning, and transformer-based applications. The programs are organized according to **Course Outcomes CO1, CO2, and CO3**, providing a practical learning path from basic text processing to advanced NLP systems.

\<p align="center">
&#x20; \<img src="[https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)" alt="Python">
&#x20; \<img src="[https://img.shields.io/badge/NLTK-NLP-4CAF50](https://img.shields.io/badge/NLTK-NLP-4CAF50)" alt="NLTK">
&#x20; \<img src="[https://img.shields.io/badge/spaCy-NLP-09A3D5](https://img.shields.io/badge/spaCy-NLP-09A3D5)" alt="spaCy">
&#x20; \<img src="[https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikitlearn\&logoColor=white)" alt="Scikit-learn">
&#x20; \<img src="[https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?logo=pytorch&logoColor=white](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?logo=pytorch\&logoColor=white)" alt="PyTorch">
&#x20; \<img src="[https://img.shields.io/badge/Transformers-Hugging%20Face-FFD21E?logo=huggingface&logoColor=black](https://img.shields.io/badge/Transformers-Hugging%20Face-FFD21E?logo=huggingface\&logoColor=black)" alt="Hugging Face">
&#x20; \<img src="[https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter\&logoColor=white)" alt="Jupyter">
\</p>

---

## Table of Contents

- [Overview](#overview)
- [Course Outcome Distribution](#course-outcome-distribution)
- [CO1: Fundamental NLP Techniques](#co1-fundamental-nlp-techniques)
- [CO2: Text Representation and NLP Applications](#co2-text-representation-and-nlp-applications)
- [CO3: Advanced NLP and Transformer Applications](#co3-advanced-nlp-and-transformer-applications)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Running the Notebooks](#running-the-notebooks)
- [Learning Outcomes](#learning-outcomes)
- [Repository Information](#repository-information)
- [Author](#author)

---

## Overview

Natural Language Processing is a field of Artificial Intelligence that enables computers to process, analyze, and generate human language.

This repository provides hands-on implementations of important NLP algorithms and techniques through Jupyter Notebooks. It combines linguistic processing, statistical text representation, machine learning, and pretrained language models to demonstrate how NLP concepts are applied in practice.

### Key Features

- 32 practical NLP programs organized into three course outcomes.
- Text preprocessing and linguistic analysis using NLTK and spaCy.
- Numerical text representation using Bag of Words and TF-IDF.
- Word embeddings and semantic similarity techniques.
- Text classification, sentiment analysis, and topic modeling.
- Information extraction and information retrieval.
- Sequence modeling using RNNs and LSTMs.
- Transformer-based classification, generation, translation, and summarization.
- Document classification and sequence boundary detection.

---

## Course Outcome Distribution

| Course Outcome | Program Numbers | Programs | Coverage                                              |
| -------------- | --------------- | -------: | ----------------------------------------------------- |
| CO1            | 01–07           |        7 | Fundamental NLP and linguistic processing             |
| CO2            | 08–23           |       16 | Text representation, similarity, and NLP applications |
| CO3            | 24–32           |        9 | Advanced NLP, deep learning, and transformers         |
| **Total**      | **01–32**       |   **32** | **Complete practical collection**                     |

---

## CO1: Fundamental NLP Techniques

This section covers the essential operations used to preprocess text and analyze linguistic structures.

| No. | Program                    | Concepts                                                          |
| --: | -------------------------- | ----------------------------------------------------------------- |
|  01 | Tokenization               | Sentence tokenization and word tokenization                       |
|  02 | Stemming and Lemmatization | Porter stemming, WordNet lemmatization, and word normalization    |
|  03 | Stop-Word Removal          | Stop-word identification and text cleaning                        |
|  04 | Part-of-Speech Tagging     | Grammatical categories and POS tags                               |
|  05 | Parsing and Chunking       | Noun phrases, regular-expression chunking, and dependency parsing |
|  06 | Named Entity Recognition   | Identification and classification of named entities               |
|  07 | Coreference Resolution     | Resolving references to entities across text                      |

**Libraries:** Python, NLTK, spaCy

---

## CO2: Text Representation and NLP Applications

This section explores numerical representations of text, semantic relationships, traditional machine learning, and core NLP applications.

| No. | Program                               | Concepts                                                         |
| --: | ------------------------------------- | ---------------------------------------------------------------- |
|  08 | Bag of Words (BoW)                    | Vocabulary creation, term frequency, document-term matrix        |
|  09 | TF-IDF                                | Term frequency, inverse document frequency, weighted vectors     |
|  10 | N-Gram Model                          | Unigrams, bigrams, trigrams, and word sequences                  |
|  11 | Cosine Similarity                     | Vector magnitude, dot product, and document similarity           |
|  12 | Word2Vec                              | CBOW, Skip-gram, and distributed word representations            |
|  13 | GloVe Embeddings                      | Pretrained word vectors and semantic representations             |
|  14 | Word Mover's Distance                 | Semantic distance between documents                              |
|  15 | Text Classification                   | TF-IDF features, Naive Bayes, and SVM                            |
|  16 | Sentiment Analysis                    | Sentiment polarity using TextBlob and VADER                      |
|  17 | Topic Modeling with LDA               | Latent topics and document-topic distributions                   |
|  18 | Topic Modeling with LSA               | Latent semantic structure and dimensionality reduction           |
|  19 | Opinion Mining                        | Analysis of opinions and product or service reviews              |
|  20 | Information Extraction                | Extracting structured information from text                      |
|  21 | Information Retrieval                 | Query processing and TF-IDF document ranking                     |
|  22 | Sequence Classification with RNN/LSTM | Sequential representations and recurrent neural networks         |
|  23 | Attention Mechanism                   | Attention scores, context vectors, and encoder-decoder attention |

**Libraries:** Python, NLTK, Scikit-learn, Gensim, NumPy, Pandas, TextBlob, VADER, PyTorch

---

## CO3: Advanced NLP and Transformer Applications

This section introduces pretrained language models, deep learning, text generation, and advanced document-processing techniques.

| No. | Program                                                        | Concepts                                                                 |
| --: | -------------------------------------------------------------- | ------------------------------------------------------------------------ |
|  24 | BERT for Text Classification                                   | Tokenization, pretrained models, fine-tuning, evaluation                 |
|  25 | Sentence Embeddings Using BERT and GPT-2                       | Contextual representations and semantic similarity                       |
|  26 | Text Generation Using GPT-2                                    | Autoregressive generation and next-token prediction                      |
|  27 | Transformer-Based Named Entity Recognition                     | Contextual representations and token classification                      |
|  28 | Machine Translation Using MarianMT or T5                       | Sequence-to-sequence translation                                         |
|  29 | Text Summarization Using BART                                  | Abstractive summarization and encoder-decoder models                     |
|  30 | Transformer-Based Chatbot Using DialoGPT                       | Conversational context and response generation                           |
|  31 | Automatic Document Classification and Separation               | TF-IDF, machine learning, and category-based organization                |
|  32 | Hybrid Probabilistic and FSM-Based Document Boundary Detection | Probability estimation, finite state machines, and sequence segmentation |

**Libraries:** Python, PyTorch, Hugging Face Transformers, Scikit-learn, BERT, GPT-2, MarianMT, BART, T5, DialoGPT

---

## Technology Stack

| Technology                | Application                                                     |
| ------------------------- | --------------------------------------------------------------- |
| Python                    | Core programming language                                       |
| NLTK                      | Tokenization, stemming, lemmatization, and text processing      |
| spaCy                     | Linguistic analysis, dependency parsing, and entity recognition |
| Scikit-learn              | Feature extraction, machine learning, and evaluation            |
| Gensim                    | Word embeddings and topic modeling                              |
| TextBlob and VADER        | Sentiment analysis                                              |
| NumPy and Pandas          | Numerical computation and data handling                         |
| PyTorch                   | Deep learning and model inference                               |
| Hugging Face Transformers | Pretrained transformer architectures                            |
| Jupyter Notebook          | Interactive practical implementations                           |
| VS Code                   | Development environment                                         |
| Git and GitHub            | Version control and project hosting                             |

---

## Installation

### Prerequisites

- Python 3.x
- pip
- Jupyter Notebook or VS Code
- An internet connection for downloading dependencies and pretrained models

### 1. Clone the repository

```bash
git clone https://github.com/Amit27181/NLP-programs-using-Python-NLTK-and-spaCy.git
cd NLP-programs-using-Python-NLTK-and-spaCy
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the required libraries

```bash
python -m pip install --upgrade pip
python -m pip install nltk spacy scikit-learn pandas numpy matplotlib jupyter ipykernel gensim textblob vaderSentiment
```

For transformer-based programs, install the additional dependencies:

```bash
python -m pip install torch transformers sentencepiece
```

### 4. Download the spaCy English model

```bash
python -m spacy download en_core_web_sm
```

### 5. Download NLTK resources

Run this code in a notebook when required:

```python
import nltk

resources = [
    "punkt",
    "punkt_tab",
    "stopwords",
    "averaged_perceptron_tagger_eng",
    "wordnet",
    "omw-1.4"
]

for resource in resources:
    nltk.download(resource)

print("NLTK resources are ready.")
```

**Note:** Individual notebooks may require additional dependencies, datasets, or language resources. Pretrained transformer models are downloaded separately when first loaded and may require significant memory and disk space.

---

## Running the Notebooks

### VS Code

1. Open the repository folder in VS Code.
2. Install the Python and Jupyter extensions.
3. Navigate to the appropriate course-outcome folder.
4. Open the required `.ipynb` file.
5. Select the Python interpreter and Jupyter kernel.
6. Execute the cells sequentially.

### Jupyter Notebook

Start Jupyter from the project directory:

```bash
jupyter notebook
```

Open the required notebook in your browser and run its cells.

### Google Colab

Upload the required notebook, install any missing dependencies, and execute the cells in order.

---

## Learning Outcomes

After completing the practical programs, learners should be able to:

- Apply fundamental NLP preprocessing and linguistic analysis.
- Transform text into statistical and distributed numerical representations.
- Analyze document similarity and semantic relationships.
- Build traditional machine learning models for text classification.
- Perform sentiment analysis, opinion mining, and topic modeling.
- Implement information extraction and document retrieval workflows.
- Understand RNNs, LSTMs, and attention mechanisms.
- Apply pretrained transformer models to classification, translation, summarization, and text generation.
- Develop reproducible NLP experiments using Python and Jupyter Notebooks.

---

## Repository Information

**Repository:** [NLP Programs Using Python, NLTK and spaCy](https://github.com/Amit27181/NLP-programs-using-Python-NLTK-and-spaCy)

**Course coverage:** CO1, CO2, and CO3

**Total practical programs:** 32

**Format:** Jupyter Notebooks (`.ipynb`)

**Purpose:** Academic learning, practical implementation, and NLP experimentation.

---

## Author

**Amit Pandey**

- GitHub: [@Amit27181](https://github.com/Amit27181)
- Repository: [NLP Programs Using Python, NLTK and spaCy](https://github.com/Amit27181/NLP-programs-using-Python-NLTK-and-spaCy)

---

\<p align="center">
&#x20; \<strong>Learn. Implement. Experiment. Improve.\</strong>
&#x20; \<br>\<br>
&#x20; If this repository helps you learn NLP, consider giving it a star.
\</p>
