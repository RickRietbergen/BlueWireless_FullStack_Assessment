import azure.functions as func
import json

app = func.FunctionApp()

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
