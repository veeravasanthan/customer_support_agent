def assess_priority(ticket_text, sentiment):
    text = ticket_text.lower()

    if "urgent" in text or "immediately" in text:
        return "Critical"

    if sentiment == "Frustrated":
        return "High"

    if "failed" in text or "locked" in text:
        return "High"

    return "Medium"
