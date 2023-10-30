import json


def handler(event, context):
    # TODO implement
    #Grab and process incoming payload
        
    body = {"message": "Hello from Lambda."}
    response = {"statusCode": 200, "body":json.dumps(body, default=str)}
    return response
