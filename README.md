# AWS Serverless Image Recognition

A fully serverless image analysis pipeline built on AWS, leveraging S3, Lambda, Rekognition, DynamoDB, API Gateway, and SNS. The solution automatically detects objects in uploaded images, logs results, generates structured detection reports stored in S3, and enables both automatic and API-driven analysis workflows. It also supports multilingual translation of detected labels and sends optional notifications when processing completes.

---

## 🏗️ Architecture Overview

* **S3** — Stores uploaded images and auto-generated detection result reports (`.txt`).
* **Lambda** — Automatically triggered on new uploads or invoked via API Gateway for image analysis.
* **Rekognition** — Performs object detection on uploaded images.
* **DynamoDB** — Stores detection results (including translated labels and timestamps) in a NoSQL table for audit and future queries.
* **API Gateway** — Provides a secure HTTP API for manual or programmatic triggering of the pipeline.
* **SNS** — Sends notifications (e.g., email alerts) when image analysis is completed.
* **CloudWatch** — Logs detected labels and processing information.

---

## ⚙️ Key Features

* Fully event-driven and serverless; requires no server management.
* Supports both automatic triggering via S3 and manual triggering via secure API.
* API Key-based authentication via API Gateway for secure external API access.
* Multilingual translation support for detected labels using Amazon Translate.
* Stores detection timestamps for audit and historical tracking.
* Sends SNS notifications after successful image analysis (configurable).
* Auto-saves detection results in structured format alongside uploaded images in S3.
* Automatically stores detection results in DynamoDB for easy future access or reporting.
* Extensible design supporting additional integrations (Step Functions, etc.).

---

## 🚀 Usage Flow

1. **Automatic Mode:**

   * Upload an image to the S3 bucket.
   * S3 triggers the Lambda function automatically.
   * Lambda invokes Rekognition for image analysis and optionally translates detected labels.
   * Detection results are logged in CloudWatch and saved to:

     * S3 as `.txt` reports (original and translated).
     * DynamoDB with timestamp and notification tracking.
   * An SNS notification is sent (only once per image).

2. **API Mode (Manual Triggering):**

   * Send a POST request via API Gateway with an API Key to analyze specific images from S3.
   * Lambda performs detection, translation, saves results, and sends notifications (same as automatic mode).

---

## 📂 Included

* `lambda_function.py` — Lambda handler for automated detection, translation, storage, and notification.
* `README.md` — Project overview, architecture, and usage details.
* `SETUP.md` — Detailed deployment and configuration guide, including API Gateway, DynamoDB, SNS, and translation setup.
* `AWS_Image_Analyzer_API_Test.postman_collection.json` — Pre-configured Postman API Collection for testing the API Gateway endpoint. It sends a POST request with the required payload (S3 bucket and image key)   along with the API Key, allowing you to easily trigger the Lambda function from Postman for testing and debugging purposes.

---

## 🎯 Why It Matters

* Enables scalable, automated image recognition pipelines with minimal operational overhead.
* Supports flexible use cases: fully automated workflows or manual API-triggered analysis.
* Multilingual-ready pipeline, enabling better accessibility and internationalization.
* Provides audit-ready detection results with timestamps for traceability and reporting.
* Sends alerts after successful processing, useful for monitoring workflows.
* Long-term, queryable storage of results via DynamoDB for downstream workflows or analytics.

---

## ✍️ Author

*Sandeep Kasiraju*

---

## ⚠️ Notes

Ensure AWS resources (S3, Lambda, DynamoDB, API Gateway, SNS, IAM roles) are decommissioned after testing to avoid unintended costs.

For detailed setup and deployment instructions, refer to [SETUP.md](./SETUP.md).

---

