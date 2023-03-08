import os
import json
import boto3

client = boto3.client('ec2')

def lambda_handler(event, context):
    source_check(event, context)
    
def extract_body(event):
    body = json.loads((event["body"]))
    return body

def source_check(event, context):
    body = extract_body(event)
    if os.environ['Pingdom'] in event['headers']['user-agent']:
        extract_status(event, body)
    else:
        print("No known source")

def extract_status(event, body):
    state = body['current_state']
    if state == "DOWN":
        print("site is down")
        reboot_instance()
    elif state == "UP":
        print("site is up")
    else:
        pass
    
def reboot_instance():
    response = client.reboot_instances(
        InstanceIds = [
            os.environ['InstanceID'],    
        ],
    )
    print(response)
    return response
