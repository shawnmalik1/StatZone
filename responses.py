def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "ping":
        return "Pong!"

    if p_message == "!help":
        return "help message"

    else:
        return "hello!"