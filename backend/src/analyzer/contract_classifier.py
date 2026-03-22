def classify_contract(text):
    text = text.lower()

    if "confidential" in text:
        return "NDA"
    elif "employee" in text or "employment" in text:
        return "Employment Agreement"
    elif "lease" in text:
        return "Lease Agreement"
    elif "acquisition" in text:
        return "Acquisition Agreement"
    else:
        return "General Contract"