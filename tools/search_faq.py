FAQ_DB = {
    "payment failed": "Please verify your card details and ensure sufficient balance.",
    "account locked": "Reset your password using the forgot password link.",
    "cancel subscription": "You can cancel from your account billing section."
}

def search_faq(ticket_text):
    text = ticket_text.lower()

    for key in FAQ_DB:
        if key in text:
            return FAQ_DB[key]

    return None
