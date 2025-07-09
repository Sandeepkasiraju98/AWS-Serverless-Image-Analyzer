import boto3
import json

rekognition = boto3.client('rekognition')
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageAnalysisResults')

def lambda_handler(event, context):
    try:
        # Hardcoded bucket and key (for your testing)
        bucket = "my-image-bucket-12879"
        key = "Superman.jpeg"

        # Detect objects
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            MaxLabels=5
        )
        
        labels = {label['Name']: label['Confidence'] for label in response['Labels']}
        
        # Save results to S3 as .txt file
        s3_client.put_object(
            Bucket=bucket,
            Key=f"{key}_results.txt",
            Body=json.dumps(labels, indent=2)
        )
        
        # Save results to DynamoDB
        table.put_item(
            Item={
                'ImageKey': key,
                'Labels': json.dumps(labels)
            }
        )
        
        print("Results saved to S3 and DynamoDB")
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Success', 'labels': labels})
        }
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
