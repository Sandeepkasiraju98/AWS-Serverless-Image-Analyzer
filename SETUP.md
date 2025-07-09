# Project Setup — AWS Serverless Image Recognition

This guide provides setup instructions for deploying the serverless image recognition pipeline using AWS services.

---

## 🛠️ Prerequisites
- AWS Account (Free Tier is sufficient for testing)
- Basic familiarity with the AWS Management Console

---

## ⚙️ AWS Services Used
- **S3:** Object storage for images and detection result reports.
- **Lambda:** Event-driven function for processing images.
- **Rekognition:** AI-powered image analysis.
- **IAM:** Role-based access permissions.
- *(Optional)* Additional integrations via DynamoDB, API Gateway, SNS.

---

## 🚀 Deployment Steps

### 1. Create S3 Bucket
- Navigate to **S3** → **Create Bucket**.
- Name the bucket (e.g., `image-upload-pipeline`).
- Default settings are sufficient for testing.

---

### 2. Create IAM Role
- Go to **IAM** → **Roles** → **Create Role**.
- Choose **Lambda** as the trusted entity.
- Attach these policies:
  - `AmazonRekognitionFullAccess`
  - `AmazonS3FullAccess`
- Name the role: `rekognition-lambda-role`.

---

### 3. Create Lambda Function
- Navigate to **Lambda** → **Create Function** → Author from scratch.
- Function name: `image-analyzer`.
- Runtime: **Python 3.12**.
- Assign the previously created IAM role (`rekognition-lambda-role`).

---

### 4. Deploy Lambda Code
- Paste the provided code from `lambda_function.py` into the Lambda console.
- Deploy the function.

---

### 5. Configure S3 Trigger
- In your S3 bucket:
  - Go to **Properties** → **Event Notifications** → **Create event notification**.
  - Select **All object create events** as the trigger.
  - Set your Lambda function as the destination.

---

### 6. Test the Pipeline
- Upload an image to the S3 bucket.
- Monitor Lambda execution logs in **CloudWatch**.
- Detection results will be:
  - Displayed in CloudWatch Logs.
  - Auto-saved as `.txt` reports in S3 alongside the image.

---

### 7. Create DynamoDB Table (For Storing Results)
- Go to **DynamoDB** → Click **Create Table**.
- Table name: `ImageAnalysisResults`
- Partition key: `ImageKey` (Type: String)
- Leave Sort key blank (optional, not needed here).
- Use default settings and click **Create Table**.

---

### 8. Grant Lambda Permission to Use DynamoDB
- Go to **IAM** → Roles → Find `rekognition-lambda-role`.
- Click **Attach policies** → Search for `AmazonDynamoDBFullAccess`.
- Select it and click **Attach Policy**.


---

## 📝 Notes
- The pipeline automatically processes uploaded images, detects objects, and stores results without manual intervention.
- Detection results are stored in two places:
  - As `.txt` files in the S3 bucket.
  - In DynamoDB for easy querying, auditing, or downstream workflows.
- The architecture is fully serverless and event-driven, requiring no server management.

---

## ⚠️ Resource Cleanup
To avoid unexpected charges, ensure all unused AWS resources are deleted after testing:
- S3 bucket
- Lambda function
- DynamoDB table (`ImageAnalysisResults`)
- IAM roles and policies (if no longer needed)


---

