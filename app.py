from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def udf():
    try:
        req = request.get_json(force=True)
        return_set = []
        for(i, column1_raw) in req['data']:
            print(column1_raw)
            column1 = json.loads(column1_raw)
            print(column1)
            return_set.append([i, column1])
        return jsonify({"data": return_set})
    except Exception as e:
        print(e)
        return Response(status=500)

