import re

def extract_entities(text):
    entities = {
        "PERSON": [],
        "ORG": [],
        "DATE": []
    }

    # PERSON (same pattern you fixed earlier)
    person_pattern = r"[A-Z][a-z]+\s+[A-Z]\.\s+[A-Z][a-z]+(?:[a-z]+)?"
    persons = re.findall(person_pattern, text)

    # ORG (companies)
    org_pattern = r"[A-Z][A-Za-z&.\s]+?(?:Inc\.|Corporation|Corp\.|Ltd\.)"
    orgs = re.findall(org_pattern, text)

    # DATE
    date_pattern = r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}"
    dates = re.findall(date_pattern, text)

    entities["PERSON"] = list(set(persons))
    entities["ORG"] = list(set(orgs))
    entities["DATE"] = list(set(dates))

    return entities