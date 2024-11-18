import spacy

nlp = spacy.load("en_core_web_trf")

text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."
doc = nlp(text)

for ent in doc.ents:
    if ent.label_ == 'PERSON':  # Personvārds
        print(f"Personvārds: {ent.text}")
    elif ent.label_ == 'ORG':  # Organizācija
        print(f"Organizācija: {ent.text}")
