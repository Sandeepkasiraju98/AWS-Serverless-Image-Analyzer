import boto3
import json

rekognition = boto3.client('rekognition')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Detect labels using Rekognition
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=5
    )
    
    labels = {label['Name']: label['Confidence'] for label in response['Labels']}
    
    # Save detection results to S3 as a text file
    result_key = f"{key}_results.txt"  # Creates a text file with results
    s3_client.put_object(
        Bucket=bucket,
        Key=result_key,
        Body=json.dumps(labels, indent=2)
    )
    
    print(f"Detection results saved to {result_key}")
