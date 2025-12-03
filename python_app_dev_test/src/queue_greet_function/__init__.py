# q5 - answer here
import logging
import azure.functions as func

def queue_greet_function(msg: func.QueueMessage) -> None:
    """
    Azure Function Queue trigger that processes messages containing usernames.
    Message may be plain text (username) or JSON {"username": "..."}.
    Logs a greeting message for each username.
    """
    username = None
    try:
        body = msg.get_json()
        # If message is a JSON object, try common fields
        if isinstance(body, dict):
            username = body.get("username") or body.get("name")
        else:
            # If the JSON is just a string, use it directly
            username = str(body)
    except ValueError:
        # Not JSON; fall back to raw bytes
        try:
            username = msg.get_body().decode('utf-8')
        except Exception:
            username = None

    if not username:
        logging.warning("Queue message did not contain a username")
    else:
        logging.info(f"Hello, {username}!")
