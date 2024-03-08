def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "ping":
        return "Pong!"
    else:
        return "Invalid command!"