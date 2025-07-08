# AWS Serverless Image Recognition

A serverless image analysis pipeline built on AWS, leveraging S3, Lambda, and Rekognition. Automatically detects objects in uploaded images and logs results with optional storage of detection outputs.

---

## 🏗️ Architecture Overview
- **S3** — Stores uploaded images.
- **Lambda** — Automatically triggered on new uploads; processes images.
- **Rekognition** — Performs object detection.
- **CloudWatch** — Logs detected labels.
- Auto-generates and stores detection results as structured `.txt` files within S3 (fully automated).


---

## ⚙️ Key Features
- Event-driven, fully serverless architecture.
- Minimal setup, designed for rapid deployment.
- Auto-saves detection results as structured files (optional).
- Built for extensibility (DynamoDB, API Gateway, SNS integrations ready).

---

## 🚀 Usage Flow
1. Upload an image to the S3 bucket.
2. Lambda triggers and invokes Rekognition.
3. Detected objects are logged and optionally persisted to S3.

---

## 📂 Included
- `lambda_function.py` — Lambda handler for automated detection and storage.
- `README.md` — Project summary and usage notes.

---

## 🎯 Why It Matters
- Automated, scalable image recognition pipeline.
- No infrastructure to manage—entirely serverless.
- Easy to integrate with additional AWS services for production-grade systems.

---

## ✍️ Author
*Sandeep Kasiraju*

---

## ⚠️ Notes
Ensure AWS resources are cleaned up post-testing to avoid unintended charges.


For detailed setup instructions, see [SETUP.md](./SETUP.md).
