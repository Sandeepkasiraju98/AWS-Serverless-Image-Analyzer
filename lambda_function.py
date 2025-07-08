import boto3

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=5
    )

    print("Here’s what we found in the photo:")
    for label in response['Labels']:
        print(label['Name'], label['Confidence'])
