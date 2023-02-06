from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello_world():
    response: dict = {}
    response["headers"] = dict(request.headers)
    response["body"] = request.get_json()
    res = json.dumps(dict({"data": [[0, json.dumps(response)]]}))
    return res

