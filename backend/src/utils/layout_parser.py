import re

def extract_sections(text):
    """
    Splits document into sections using layout-like heuristics
    """

    sections = []

    lines = text.split("\n")

    current_section = ""
    current_title = "UNKNOWN"

    for line in lines:
        line_clean = line.strip()

        if (
            line_clean.isupper()
            or re.match(r"^\d+(\.\d+)*\s+[A-Z]", line_clean)
        ):
            if current_section:
                sections.append({
                    "title": current_title,
                    "content": current_section.strip()
                })

            current_title = line_clean
            current_section = ""

        else:
            current_section += line_clean + " "

    if current_section:
        sections.append({
            "title": current_title,
            "content": current_section.strip()
        })

    return sections