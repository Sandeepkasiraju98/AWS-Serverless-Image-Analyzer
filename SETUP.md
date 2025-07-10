
# Project Setup — AWS Serverless Image Recognition

This guide provides setup instructions for deploying the serverless image recognition pipeline using AWS services.

---

## 🛠️ Prerequisites

* AWS Account (Free Tier is sufficient for testing).
* Basic familiarity with the AWS Management Console.
* Verified email for SNS (for notifications).

---

## ⚙️ AWS Services Used

* **S3:** Object storage for images and detection result reports.
* **Lambda:** Event-driven function for image analysis.
* **Rekognition:** AI-powered image analysis.
* **Translate:** For multi-language translation of detected labels.
* **DynamoDB:** NoSQL database for storing results, translations, timestamps, and notification status.
* **API Gateway:** HTTP API to manually trigger image analysis via API calls.
* **SNS:** Notification service to send alerts after image processing.
* **IAM:** Role-based access permissions.

---

## 🚀 Deployment Steps

### 1. Create S3 Bucket

* Navigate to **S3** → **Create Bucket**.
* Name the bucket (e.g., `image-upload-pipeline`).
* Default settings are sufficient for testing.

---

### 2. Create IAM Role

* Go to **IAM** → **Roles** → **Create Role**.
* Choose **Lambda** as trusted entity.
* Attach these policies:

  * `AmazonRekognitionFullAccess`
  * `AmazonS3FullAccess`
  * `AmazonDynamoDBFullAccess`
  * `AmazonSNSFullAccess`
  * `TranslateReadOnly` *(for Amazon Translate)*
* Name the role: `rekognition-lambda-role`.

---

### 3. Create SNS Topic

* Go to **SNS** → **Topics** → **Create Topic**.
* Type: **Standard**.
* Name it (e.g., `image-detection-alerts`).
* Create the topic.
* Subscribe your email to this topic (you must confirm the subscription via email).

---

### 4. Create DynamoDB Table

* Go to **DynamoDB** → **Tables** → **Create Table**.
* Table Name: `ImageAnalysisResults`.
* Partition Key: `ImageKey` (Type: String).
* Leave Sort Key blank.
* Click **Create Table**.

---

### 5. Create Lambda Function

* Go to **Lambda** → **Create Function** → Author from scratch.
* Function Name: `image-analyzer`.
* Runtime: **Python 3.12**.
* Assign the previously created IAM role (`rekognition-lambda-role`).

---

### 6. Deploy Lambda Code

* Paste the provided `lambda_function.py` into the Lambda console.
* Replace the SNS Topic ARN in the code with your actual SNS Topic ARN.
* Deploy the function.

---

### 7. Configure S3 Trigger

* In your S3 bucket:

  * Go to **Properties** → **Event Notifications** → **Create Event Notification**.
  * Choose “All object create events”.
  * Set the destination as your Lambda function.

---

### 8. Create API Gateway (for Manual API Calls)

* Go to **API Gateway** → **Create API** → Choose **HTTP API**.
* Connect to your Lambda function using **Lambda Proxy Integration**.
* Create a **POST** route (e.g., `/analyze`).
* Deploy the API to the `dev` stage.
* Copy the Invoke URL.

---

### 9. Test

#### ✅ Automatic Mode:

* Upload an image to the S3 bucket.
* Lambda will automatically analyze the image, translate labels, save results, and send an SNS alert.

#### ✅ API Mode:

* Use Postman (or another tool) to send a `POST` request:

  * URL: Your API Gateway URL (e.g., `https://your-api-url/dev/analyze`).
  * Headers:

    * `Content-Type: application/json`
    * `x-api-key: <your-api-key>` (if enabled)
  * Body (JSON):

```json
{
  "bucket": "my-image-bucket-12879",
  "key": "Superman.jpeg"
}
```

---

## 📝 Notes

* Results are auto-saved:

  * Original labels and translated labels as `.txt` in S3.
  * All results (labels, translations, timestamp, and notification status) in DynamoDB.
* SNS notifications are only sent once per image (to prevent spam).
* Translation language can be modified by changing the target language code in the Lambda function (`es` → Spanish, others available in AWS Translate docs).
* Timestamps are stored in DynamoDB for audit and historical tracking.

---

## ⚠️ Resource Cleanup

* Delete S3 buckets, Lambda functions, DynamoDB tables, SNS topics, API Gateway APIs, and IAM roles when finished to avoid charges.

