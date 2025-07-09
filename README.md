# AWS Serverless Image Recognition

A fully serverless image analysis pipeline built on AWS, leveraging S3, Lambda, and Rekognition. The solution automatically detects objects in uploaded images, logs results, and generates structured detection reports stored in S3 enabling automated analysis workflows.

---

## 🏗️ Architecture Overview
- **S3** — Stores uploaded images and auto-generated detection result reports (`.txt`).
- **Lambda** — Automatically triggered on new uploads; processes images and invokes Rekognition.
- **Rekognition** — Performs object detection on uploaded images.
- **DynamoDB** — Stores detection results in a NoSQL table for audit and future queries.
- **CloudWatch** — Logs detected labels and processing information.

---

## ⚙️ Key Features
- Fully event-driven and serverless; requires no server management.
- Minimal deployment steps with rapid automation.
- Auto-saves detection results in structured format alongside uploaded images.
- Automatically stores detection results in DynamoDB for easy future access or reporting.
- Extensible design supporting additional integrations (API Gateway, SNS).

---

## 🚀 Usage Flow
1. Upload an image to the S3 bucket.
2. S3 triggers the Lambda function automatically.
3. Lambda invokes Rekognition for image analysis.
4. Detected objects are logged in CloudWatch and optionally stored in S3.

---

## 📂 Included
- `lambda_function.py` — Lambda handler for automated detection and result storage.
- `README.md` — Project overview and architecture details.
- `SETUP.md` — Deployment and configuration instructions.

---

## 🎯 Why It Matters
- Enables scalable, automated image recognition pipelines with minimal operational overhead.
- Designed for easy integration with additional AWS services for production environments.
- Provides audit-ready detection results, enabling traceability and reporting.
- Supports long-term, queryable storage of results via DynamoDB for downstream workflows or analytics.

---

## ✍️ Author
*Sandeep Kasiraju*

---

## ⚠️ Notes
Ensure AWS resources are decommissioned after testing to avoid unnecessary costs.


For detailed setup and deployment instructions, refer to [SETUP.md](./SETUP.md).
