import re

# 🎯 Clause expectations based on contract type
CLAUSE_MAP = {
    "NDA": ["confidentiality", "term", "termination"],
    "Employment Agreement": ["salary", "termination", "duties"],
    "Lease Agreement": ["rent", "duration", "termination"],
    "Acquisition Agreement": ["liability", "indemnity", "governing law"],
    "General Contract": ["termination", "liability", "governing law"]
}

# ⚠️ Risk keywords with severity
RISK_KEYWORDS = {
    "HIGH": [
        "unlimited liability",
        "irrevocable",
        "in perpetuity"
    ],
    "MEDIUM": [
        "sole discretion",
        "without notice",
        "not liable",
        "at any time"
    ]
}


def detect_anomalies(text, contract_type="General Contract"):
    text_lower = text.lower()

    report = {
        "contract_type": contract_type,
        "missing_clauses": [],
        "risks": {
            "HIGH": [],
            "MEDIUM": []
        }
    }

    # 🔍 Get expected clauses dynamically
    expected_clauses = CLAUSE_MAP.get(contract_type, CLAUSE_MAP["General Contract"])

    # 🔍 Check missing clauses
    for clause in expected_clauses:
        if clause not in text_lower:
            report["missing_clauses"].append(clause)

    # ⚠️ Detect risks with severity
    for severity, keywords in RISK_KEYWORDS.items():
        for word in keywords:
            if word in text_lower:
                report["risks"][severity].append(word)

    return report