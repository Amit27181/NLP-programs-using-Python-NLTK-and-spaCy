# Named Entity Recognition using spaCy

import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

text = """
Amit is studying Computer Science at NIET in Greater Noida.
He is working on an Artificial Intelligence project.
Microsoft is one of the companies he wants to work for.
"""

doc = nlp(text)

print("========== NAMED ENTITY RECOGNITION ==========")

for entity in doc.ents:
    print(
        f"Entity: {entity.text:20} "
        f"Label: {entity.label_:10} "
        f"Description: {spacy.explain(entity.label_)}"
    )