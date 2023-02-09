from flask import Flask, request, Response
from celery import Celery
import json
import time

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route("/", methods=["POST"])
def start():
    print('content type: ', request.content_type)
    print('data: ', request.data)
    # get the json body
    try:
        data = request.get_json(force=True) # type: ignore
        # get the first element of the data list
        print('about to transcode')
        do_work.apply_async([data], task_id=request.headers.get('Sf-External-Function-Query-Batch-Id'))
        print('transcode started')
        return Response(status=202)
    except Exception as e:
        print(e)
        return Response(status=500)
    
@app.route("/", methods=["GET"])
def get_status():
    task = do_work.AsyncResult(request.headers.get('Sf-External-Function-Query-Batch-Id'))
    if task.state == 'PENDING':
        print('Task pending...')
        return Response(status=202)
    ## else if the task is finished, return the result
    elif task.state != 'FAILURE':
        print('Task finished!')
        json_response = json.dumps({"data": task.get()})
        return Response(json_response, status=200, mimetype='application/json')
    else:
        print('Task failed!')
        return Response(status=500)

@celery.task
def do_work(data):
    # some long running task here
    return_set = []
    for(i, column1_raw) in data['data']:
        column1 = json.loads(column1_raw)
        print(column1)
        # DO WORK: sleep for 60 seconds
        time.sleep(60)

        return_set.append([i, column1])

    return return_set

