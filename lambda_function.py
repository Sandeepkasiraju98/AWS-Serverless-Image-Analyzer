import boto3
import json
from datetime import datetime

rekognition = boto3.client('rekognition')
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
translate = boto3.client('translate')

table = dynamodb.Table('ImageAnalysisResults')

def lambda_handler(event, context):
    try:
        # Detect Event Source (S3 or API Gateway)
        if 'Records' in event:
            # S3 Event
            bucket = event['Records'][0]['s3']['bucket']['name']
            key = event['Records'][0]['s3']['object']['key']
        elif 'bucket' in event and 'key' in event:
            # API Gateway or POSTMAN Request
            bucket = event['bucket']
            key = event['key']
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': "Missing bucket/key. Provide valid S3 event or API payload."})
            }

        # Skip result files (Prevent infinite loop)
        if key.endswith('_results.txt') or key.endswith('_translated_results.txt'):
            print(f"Skipping {key} to avoid recursive invocation.")
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Skipped result file.'})
            }

        print(f"Processing image: {key} from bucket: {bucket}")

        # Detect objects in image
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            MaxLabels=5
        )
        labels = {label['Name']: label['Confidence'] for label in response['Labels']}

        # Translate labels (English to Spanish)
        translated_labels = {}
        for name, confidence in labels.items():
            translation = translate.translate_text(
                Text=name,
                SourceLanguageCode='en',
                TargetLanguageCode='es'
            )
            translated_labels[translation['TranslatedText']] = confidence

        # Save labels and translations to S3
        s3_client.put_object(
            Bucket=bucket,
            Key=f"{key}_results.txt",
            Body=json.dumps(labels, indent=2)
        )
        s3_client.put_object(
            Bucket=bucket,
            Key=f"{key}_translated_results.txt",
            Body=json.dumps(translated_labels, indent=2)
        )

        # Check DynamoDB for previous notification
        existing_item = table.get_item(Key={'ImageKey': key})
        notification_sent = False
        if 'Item' in existing_item and existing_item['Item'].get('NotificationSent') == 'Yes':
            notification_sent = True

        # Save results to DynamoDB
        table.put_item(
            Item={
                'ImageKey': key,
                'Labels': json.dumps(labels),
                'TranslatedLabels': json.dumps(translated_labels),
                'Timestamp': datetime.utcnow().isoformat(),
                'NotificationSent': 'Yes'
            }
        )

        # Send SNS Notification if not already sent (Optional - Currently Disabled)
        # if not notification_sent:
        #     sns.publish(
        #         TopicArn='arn:aws:sns:your-region:your-account-id:your-sns-topic-name',
        #         Message=f"Image analysis completed for {key}.",
        #         Subject='Image Detection Alert'
        #     )
        #     print("SNS notification sent.")
        # else:
        #     print("Notification already sent earlier; skipping SNS.")

        print("Processing complete.")
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Success',
                'labels': labels,
                'translated_labels': translated_labels
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
