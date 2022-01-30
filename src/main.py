import json

from flask import Flask
from waitress import serve
from flask import request

from src import logger


logger.setup()
log = logger.log

app = Flask(__name__)


@app.route("/", methods=["POST"])
def post_data():
    """
    Take the request, validate it, do something

    :return: HTTP Response data
    """
    success = False
    error = ""
    log.info(f"Received request: {request.data}")
    response_header = {"ContentType": "application/json"}
    try:
        request_dict = json.loads(request.data)
    except json.decoder.JSONDecodeError as e:
        error = f"Invalid JSON: {e}"
        log.error(error)
        response_dict = {"request": str(request), "error": error, "success": success}
        return_status = 400
        return json.dumps(response_dict), return_status, response_header

    response_dict = {"request": request_dict}
    if not request_dict["request"] == "test request":
        error = f"Unhandled request: {request_dict['request']}"
        log.error(error)
        return_status = 401
    else:
        # Do something with the request here
        success = True
        return_status = 200

    response_dict["error"] = error
    response_dict["success"] = success
    log.info(f'Sending response: {response_dict}')
    return json.dumps(response_dict), return_status, response_header


def serve_app():
    host = "localhost"
    port = 8081
    log.info(f"Starting web server at http://{host}:{port}")
    serve(app, host=host, port=port)


if __name__ == "__main__":
    serve_app()
