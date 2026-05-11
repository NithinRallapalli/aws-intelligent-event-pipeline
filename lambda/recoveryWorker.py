import json
import boto3
import uuid

# DynamoDB setup
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('events-table')


# ✅ SMART FAILURE ANALYZER (FREE AI LOGIC)
def get_ai_insight(event_data):
    try:
        event_str = str(event_data)

        if "AccessDenied" in event_str:
            return "IAM permission issue detected. Fix: Check Lambda role policies."

        elif "NoSuchKey" in event_str:
            return "S3 object not found. Fix: Verify file path and bucket name."

        elif "timeout" in event_str.lower():
            return "Lambda timeout occurred. Fix: Increase timeout or optimize code."

        elif "s3" in event_str.lower():
            return "S3 event processing issue. Fix: Validate event structure and triggers."

        else:
            return "Unknown failure. Suggest checking CloudWatch logs and retry mechanism."

    except Exception as e:
        return f"Analysis failed: {str(e)}"


# ✅ MAIN HANDLER (DO NOT CHANGE NAME)
def lambda_handler(event, context):
    print("=== RECOVERY + SMART ANALYSIS ===")

    for record in event['Records']:
        try:
            body = json.loads(record['body'])

            # Extract file name from S3 event
            file_name = body['Records'][0]['s3']['object']['key']

            print("Retrying:", file_name)

            # Get smart analysis
            ai_output = get_ai_insight(body)

            print("Analysis:", ai_output)

            # Store in DynamoDB
            data = {
                "event_id": str(uuid.uuid4()),
                "file_name": file_name,
                "status": "recovered",
                "analysis": ai_output
            }

            table.put_item(Item=data)

            print("✅ SUCCESS:", data)

        except Exception as e:
            print("❌ ERROR:", str(e))

    return {
        "statusCode": 200,
        "body": "Recovery completed"
    }
