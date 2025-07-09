# AWS Serverless Image Recognition

A fully serverless image analysis pipeline built on AWS, leveraging S3, Lambda, Rekognition, DynamoDB, and API Gateway. The solution automatically detects objects in uploaded images, logs results, generates structured detection reports stored in S3, and enables both automatic and API-driven analysis workflows.

---

## 🏗️ Architecture Overview
- **S3** — Stores uploaded images and auto-generated detection result reports (`.txt`).
- **Lambda** — Automatically triggered on new uploads or invoked via API Gateway for image analysis.
- **Rekognition** — Performs object detection on uploaded images.
- **DynamoDB** — Stores detection results in a NoSQL table for audit and future queries.
- **API Gateway** — Provides a secure HTTP API for manual or programmatic triggering of the pipeline.
- **CloudWatch** — Logs detected labels and processing information.

---

## ⚙️ Key Features
- Fully event-driven and serverless; requires no server management.
- Supports both automatic triggering via S3 and manual triggering via secure API.
- API Key-based authentication via API Gateway for secure external API access.
- Auto-saves detection results in structured format alongside uploaded images in S3.
- Automatically stores detection results in DynamoDB for easy future access or reporting.
- Extensible design supporting additional integrations (SNS, Step Functions, etc.).

---

## 🚀 Usage Flow
1. **Automatic Mode:**  
   - Upload an image to the S3 bucket.
   - S3 triggers the Lambda function automatically.
   - Lambda invokes Rekognition for image analysis.
   - Detected objects are logged in CloudWatch and results are saved to S3 and DynamoDB.

2. **API Mode (Manual Triggering):**
   - Send a POST request via API Gateway with an API Key to analyze specific images from S3.
   - Lambda performs object detection and stores results in S3 and DynamoDB.

---

## 📂 Included
- `lambda_function.py` — Lambda handler for automated detection and result storage.
- `README.md` — Project overview, architecture, and usage details.
- `SETUP.md` — Detailed deployment and configuration guide, including API Gateway setup.

---

## 🎯 Why It Matters
- Enables scalable, automated image recognition pipelines with minimal operational overhead.
- Supports flexible use cases: fully automated workflows or manual API-triggered analysis.
- Provides audit-ready detection results, enabling traceability and reporting.
- Offers long-term, queryable storage of results via DynamoDB for downstream workflows or analytics.

---

## ✍️ Author
*Sandeep Kasiraju*

---

## ⚠️ Notes
Ensure AWS resources (S3, Lambda, DynamoDB, API Gateway, IAM roles) are decommissioned after testing to avoid unintended costs.

For detailed setup and deployment instructions, refer to [SETUP.md](./SETUP.md).
