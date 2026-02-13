def generate_response(name, department, solution, priority):
    response = f"Dear {name},\n\n"

    response += "Thank you for contacting our support team.\n\n"

    if solution:
        response += f"Suggested Solution:\n{solution}\n\n"

    if priority in ["High", "Critical"]:
        response += "We are prioritizing your request and will get back to you shortly.\n\n"

    response += f"This ticket has been routed to our {department} team.\n\n"
    response += "Best regards,\nSupport Team"

    return response
