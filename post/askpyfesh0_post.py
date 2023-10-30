import json

def payloader(event):
    if not event:
        body = {"message": "Empty payload."}
        response = {"statusCode": 400, "body":json.dumps(body, default=str)}
        return False, response
    
    event_body = event.get('body')
    if not event_body:
        body = {"message": "No payload to process."}
        response = {"statusCode": 400, "body":json.dumps(body, default=str)}
        return False, response

    payload = json.loads(event['body'])

    return True, payload

def handler(event, context):
    # TODO implement
    #Grab and process incoming payload
    ok, payload = payloader(event)

    if not ok:
        return payload
    
    required_params = ["name", "position"]
    received_params = [line for line in payload.keys()]
    for item in required_params:
        if item not in received_params:
            body = {"message":f"Please supply {item}"}
            response = {"statusCode": 400, "body":json.dumps(body, default=str)}
            return response
        
    body = {"message": "family member added."}
    response = {"statusCode": 200, "body":json.dumps(body, default=str)}
    return response
