import json

def handler(event, context):
    # Log the event
    print("EVENT\n" + json.dumps(event))

    # Check if the event contains records
    if 'Records' in event and len(event['Records']) > 0:
        # Iterate over each record
        for record in event['Records']:
            # Log the type of record
            print(type(record))
            
            # Parse the SQS message body to JSON
            sns_notification = json.loads(record['body'])
            
            # Extract the actual message from the SNS notification
            message = sns_notification.get('Message', '').upper()
            
            # Log the actual message
            print("Message:", message)
    else:
        print("No records found in the event.")

    return {'success': True}