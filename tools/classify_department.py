def classify_department(ticket_text):
    text = ticket_text.lower()
    if any(word in text for word in ["payment", "refund", "charge", "invoice", "billing"]):
        return "Billing"
    elif any(word in text for word in ["error", "crash", "bug", "not working", "locked", "issue"]):
        return "Technical"
    elif any(word in text for word in ["pricing", "cost", "plan", "enterprise"]):
        return "Sales"
    else:
        return "General"
