import logging
import json
import azure.functions as func
import random
import json
import time


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    start_time = time.time()
    value = random.randint(1, 200)
    str_value = str(value)
    end_time = time.time()
    body_data = {}

    try:
        req_body = req.get_json()
        body_data = req_body
    except ValueError:
        pass

    json_return = {
        "returncode": 0,
        "stdout": "StdOut from azure",
        "stderr": "StdErr from azure",
        "start_time": start_time,
        "end_time": end_time,
        "message": "Random Value from Azure: " + str_value,
        "unit": "ms",
        "value": str_value,
        "azure": True,
        "body_data": body_data,
    }

    return func.HttpResponse(json.dumps(json_return))
