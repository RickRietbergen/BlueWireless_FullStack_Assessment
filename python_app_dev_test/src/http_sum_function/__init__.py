# q4 - answer here
import json
import azure.functions as func

def http_sum_function(req: func.HttpRequest) -> func.HttpResponse:
    """
    Azure Function HTTP trigger that expects JSON payload with numeric fields 'a' and 'b'.
    Returns JSON: {"sum": <a+b>}
    """

    # Try to load JSON from the request
    try:
        data = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON"}),
            status_code=400,
            mimetype="application/json"
        )

    # Validate input
    if "a" not in data or "b" not in data:
        return func.HttpResponse(
            json.dumps({"error": "Please provide 'a' and 'b' in the JSON body"}),
            status_code=400,
            mimetype="application/json"
        )

    a = data["a"]
    b = data["b"]

    # Ensure both inputs are numeric
    try:
        result = a + b
    except TypeError:
        return func.HttpResponse(
            json.dumps({"error": "'a' and 'b' must be numbers"}),
            status_code=400,
            mimetype="application/json"
        )

    # Return result as JSON
    return func.HttpResponse(
        json.dumps({"sum": result}),
        status_code=200,
        mimetype="application/json"
    )