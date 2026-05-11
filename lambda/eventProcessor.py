import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
sqs = boto3.client('sqs')

table = dynamodb.Table('events-table')

QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/268174827936/failed-processing-queue"

def lambda_handler(event, context):
    print("==== EVENT RECEIVED ====")
    print(json.dumps(event))

    try:
        # Get file name from S3 event
        record = event['Records'][0]
        file_name = record['s3']['object']['key']

        print("Processing file:", file_name)

        # 🔥 Force failure for testing
        if "fail" in file_name:
            raise Exception("Simulated failure triggered")

        # Normal processing
        data = {
            "event_id": str(uuid.uuid4()),
            "file_name": file_name,
            "status": "processed"
        }

        table.put_item(Item=data)

        print("SUCCESS: Data saved to DynamoDB:", data)

        return {"statusCode": 200}

    except Exception as e:
        print("❌ ERROR OCCURRED:", str(e))

        try:
            print("➡️ Sending message to SQS...")

            response = sqs.send_message(
                QueueUrl=QUEUE_URL,
                MessageBody=json.dumps(event)
            )

            print("✅ SQS MESSAGE SENT SUCCESSFULLY")
            print("SQS RESPONSE:", response)

        except Exception as sqs_error:
            print("🚨 SQS ERROR:", str(sqs_error))

        return {"statusCode": 500}
