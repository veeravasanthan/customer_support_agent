import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(ticket_text):
    doc = nlp(ticket_text)

    entities = {}

    for ent in doc.ents:
        if ent.label_ in ["PRODUCT", "ORG"]:
            entities["product"] = ent.text
            
    error_code = re.findall(r"[A-Z]{2,5}-\d{3,4}", ticket_text)
    if error_code:
        entities["error_code"] = error_code[0]

    return entities
