import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("Python is a popular programming language.")
for token in doc:
    print(token.text, token.pos_)
