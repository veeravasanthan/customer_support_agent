
from tools.classify_department import classify_department
from tools.assess_priority import assess_priority
from tools.extract_entities import extract_entities
from tools.analyze_sentiment import analyze_sentiment
from tools.search_faq import search_faq
from tools.generate_response import generate_response
from tools.log_decision import log_decision


def process_ticket(ticket):

    ticket_id = ticket["Ticket ID"]
    name = ticket["Customer Name"]
    description = ticket["Ticket Description"]
    sentiment = analyze_sentiment(description)
    department = classify_department(description)
    entities = extract_entities(description)

    priority = assess_priority(description, sentiment)

   
    solution = search_faq(description)


    escalation_required = False
    if priority == "Critical" or (sentiment == "Frustrated" and priority == "High"):
        escalation_required = True

    response = generate_response(name, department, solution, priority)

    reasoning = log_decision(
        f"Classified as {department} due to keywords. "
        f"Sentiment: {sentiment}. Priority set to {priority}."
    )

    return {
        "ticket_id": ticket_id,
        "department": department,
        "priority": priority,
        "sentiment": sentiment,
        "entities": entities,
        "suggested_response": response,
        "escalation_required": escalation_required,
        "reasoning": reasoning
    }
if __name__ == "__main__":
    sample_ticket = {
        "Ticket ID": "TICKET-1001",
        "Customer Name": "Marisa Obrien",
        "Ticket Description": "My payment failed 3 times and now my account is locked! This is urgent! Error: PAY-403"
    }

    result = process_ticket(sample_ticket)
    print(result)