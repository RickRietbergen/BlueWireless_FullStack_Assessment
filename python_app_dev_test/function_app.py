import azure.functions as func
import logging
import json

app = func.FunctionApp()

# --------------------------
# HTTP SUM FUNCTION (Q4)
# --------------------------

@app.function_name(name="http_sum_function")
@app.route(route="http_sum_function", methods=["POST"])

def http_sum_function(req: func.HttpRequest) -> func.HttpResponse:

    # Try to load JSON
    try:
        data = req.get_json()
    except:
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON"}),
            status_code=400,
            mimetype="application/json",
        )

    # Check required fields
    if "a" not in data or "b" not in data:
        return func.HttpResponse(
            json.dumps({"error": "Please provide 'a' and 'b' in the JSON body"}),
            status_code=400,
            mimetype="application/json",
        )

    # Attempt to sum values
    try:
        result = data["a"] + data["b"]
    except:
        return func.HttpResponse(
            json.dumps({"error": "'a' and 'b' must be numbers"}),
            status_code=400,
            mimetype="application/json",
        )

    # Return result
    return func.HttpResponse(
        json.dumps({"sum": result}),
        status_code=200,
        mimetype="application/json",
    )

# --------------------------
# QUEUE GREETING FUNCTION (Q5)
# --------------------------


@app.function_name(name="queue_greet_function")
@app.queue_trigger(
    arg_name="msg",
    queue_name="usernames",
    connection="QueueConnectionString"
)
def queue_greet_function(msg: func.QueueMessage):
    """
    Queue trigger that processes messages containing usernames.
    Logs a greeting for each username.
    Supports:
    - Plain text username
    - JSON {"username": "..."}
    """
    username = None

    # Try read as JSON
    try:
        body = msg.get_json()

        if isinstance(body, dict):
            username = body.get("username") or body.get("name")
        else:
            # JSON was a string or number
            username = str(body)

    except ValueError:
        # Fallback: raw text
        try:
            username = msg.get_body().decode("utf-8")
        except:
            username = None

    # Log result
    if not username:
        logging.warning("Queue message did not contain a username")
    else:
        logging.info(f"Hello, {username}!")