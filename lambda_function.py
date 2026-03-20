import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')

events_table = dynamodb.Table('events')
registrations_table = dynamodb.Table('registrations')

def lambda_handler(event, context):
    
    body = event.get('body')
    
    if isinstance(body, str):
        body = json.loads(body)
    
    action = body.get('action')
    
    # CREATE EVENT
    if action == "create_event":
        event_id = str(uuid.uuid4())
        title = body.get('title', 'No Title')
        
        events_table.put_item(
            Item={
                'event_id': event_id,
                'title': title
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Event created',
                'event_id': event_idimport json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')

events_table = dynamodb.Table('events')
registrations_table = dynamodb.Table('registrations')

def lambda_handler(event, context):
    
    body = event.get('body')
    
    if isinstance(body, str):
        body = json.loads(body)
    
    action = body.get('action')
    
    # CREATE EVENT
    if action == "create_event":
        event_id = str(uuid.uuid4())
        title = body.get('title', 'No Title')
        
        events_table.put_item(
            Item={
                'event_id': event_id,
            })
        }
    
    # REGISTER USER
    elif action == "register":
        registration_id = str(uuid.uuid4())
        event_id = body.get('event_id')
        email = body.get('email')
        
        registrations_table.put_item(
            Item={
                'registration_id': registration_id,
                'event_id': event_id,
                'email': email
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Registered successfully',
                'registration_id': registration_id
            })
        }
    
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid action'})
        }