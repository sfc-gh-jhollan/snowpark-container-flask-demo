from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def udf():
    try:
        req = request.get_json(force=True)
        return_set = []
        for(i, column1) in req['data']:
            print(column1)
            row = json.loads(column1)
            print(row)
            return_set.append([i, row])
        return jsonify({"data": return_set})
    except Exception as e:
        print(e)
        return Response(status=500)

