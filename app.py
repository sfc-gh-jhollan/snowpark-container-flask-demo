from flask import Flask, request, Response
from flask_caching import Cache
import json

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)

COUNT = 0
RES = None

@app.route("/", methods=["POST"])
def hello_world():
    global COUNT, RES
    COUNT += 1
    print(f"COUNT: {COUNT}")
    response: dict = {}
    response["headers"] = dict(request.headers)
    response["body"] = request.get_json()
    RES = dict({"data": [[0, json.dumps(response)]]})
    return Response(status=202)

@app.route("/", methods=["GET"])
def poll():
    global COUNT, RES
    COUNT += 1
    print(f"COUNT: {COUNT}")
    if COUNT < 10:
        return Response(status=202)
    else:
        COUNT = 0
        return Response(json.dumps(RES), content_type="application/json", status=200)

