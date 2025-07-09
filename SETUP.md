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
- **DynamoDB:** NoSQL database for storing detection results.
- **API Gateway:** Provides a secure HTTP API for manual triggering of the pipeline.
- *(Optional)* Additional integrations via SNS, Step Functions, etc.

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

### 5. Configure S3 Trigger (Automatic Mode)
- In your S3 bucket:
  - Go to **Properties** → **Event Notifications** → **Create event notification**.
  - Select **All object create events** as the trigger.
  - Set your Lambda function as the destination.

---

### 6. Create DynamoDB Table (For Storing Results)
- Go to **DynamoDB** → Click **Create Table**.
- Table name: `ImageAnalysisResults`
- Partition key: `ImageKey` (Type: String)
- Leave Sort key blank (optional, not needed here).
- Use default settings and click **Create Table**.

---

### 7. Grant Lambda Permission to Use DynamoDB
- Go to **IAM** → Roles → Find `rekognition-lambda-role`.
- Click **Attach policies** → Search for `AmazonDynamoDBFullAccess`.
- Select it and click **Attach Policy**.

---

### 8. Set Up API Gateway (API Mode - Manual Triggering)
#### a. Create REST API:
- Go to **API Gateway** → Create API → Select **REST API (Build)** → Regional.
- Provide a name (e.g., `ImageAnalysisAPI`) → Click **Create API**.

#### b. Create Resource and Method:
- Click **Actions** → **Create Resource** → Resource Name: `analyze` → Resource Path: `/analyze`.
- Select the resource → Click **Actions** → **Create Method** → Choose **POST**.
- Integrate with Lambda function (`image-analyzer`).

#### c. Deploy API:
- Click **Actions** → **Deploy API** → Create a new stage (e.g., `dev`) → Deploy.

#### d. Require API Key:
- Under **Resources** → Select the **POST** method → Go to **Method Request**.
- Set **API Key Required** to **true** → Save.

---

### 9. Create API Key & Usage Plan
- Go to **API Gateway** → API Keys → Create API Key → Name and Generate Key → Save the key securely.
- Create a **Usage Plan** → Link the API and Stage (`dev`).
- Attach the API Key to the Usage Plan.

---

### 10. Test API with Postman (Optional)
- Method: `POST`
- URL: `https://your-api-id.execute-api.region.amazonaws.com/dev/analyze`
- Headers:
  - `x-api-key`: Your API Key
  - `Content-Type`: `application/json`
- Body (JSON):
```json
{
  "bucket": "your-bucket-name",
  "key": "your-image.jpg"
}
