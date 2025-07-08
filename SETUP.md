# Project Setup — AWS Serverless Image Recognition

This guide walks you through setting up the serverless image recognition pipeline on AWS.

---

## 🛠️ Prerequisites:
- AWS Account (Free Tier is sufficient for this project)
- Basic familiarity with AWS Console

---

## ⚙️ Services Involved:
- S3
- Lambda
- Rekognition
- IAM
- (Optional) DynamoDB, API Gateway, SNS

---

## 🚀 Deployment Steps:

### 1. Create an S3 Bucket:
- Go to **S3** → Create Bucket → Name it (e.g., `image-upload-pipeline`).
- Default settings are fine for testing.

---

### 2. Set Up IAM Role:
- Go to **IAM** → Roles → Create Role.
- Select **Lambda** as trusted service.
- Attach the following policies:
  - `AmazonRekognitionFullAccess`
  - `AmazonS3FullAccess`
- Name the role: `rekognition-lambda-role`.

---

### 3. Deploy Lambda Function:
- Go to **Lambda** → Create Function → Author from scratch.
- Function name: `image-analyzer`.
- Runtime: **Python 3.12**.
- Assign the IAM role you created (`rekognition-lambda-role`).

---

### 4. Add Lambda Function Code:
- Paste the provided code from `lambda_function.py` into your Lambda function.
- Deploy the function.

---

### 5. Connect S3 to Lambda (Trigger Setup):
- In your S3 bucket:
  - Go to **Properties** → Event notifications → Create event.
  - Choose trigger for **All object create events**.
  - Select your Lambda function as the destination.

---

### 6. Test:
- Upload an image to your S3 bucket.
- Review logs in **CloudWatch** → Outputs will show detected objects.
- (Optional) Check S3 for the generated `.txt` file with detection results.

---

## 📝 Notes:
- The Lambda function auto-generates detection results and stores them alongside the uploaded image.
- No infrastructure management required—this is fully serverless.

---

## ⚠️ Cleanup:
- Delete unused S3 buckets, Lambda functions, and IAM roles after testing to avoid unexpected costs.

---

