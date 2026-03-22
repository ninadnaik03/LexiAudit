import re

def extract_parties(text):
    # Normalize text
    t = re.sub(r"\s+", " ", text)

    intro = t[:4000]

    # Extract the intro block
    match = re.search(r"by and among (.*?)(?:WHEREAS|;)", intro, re.IGNORECASE)
    if not match:
        return []

    block = match.group(1)

    parties = []

    # ✅ Extract COMPANY names (with Inc., Corp., etc.)
    company_pattern = r"[A-Z][A-Za-z&.\s]+?,\s*(?:Inc\.|Corporation|Corp\.|Ltd\.)"
    companies = re.findall(company_pattern, block)

    # ✅ Extract PERSON names (First Last format)
    person_pattern = r"[A-Z][a-z]+\s+[A-Z]\.\s+[A-Z][a-z]+"
    persons = re.findall(person_pattern, block)

    # Combine
    parties.extend([c.strip() for c in companies])
    parties.extend([p.strip() for p in persons])

    # Remove duplicates
    parties = list(dict.fromkeys(parties))

    return parties