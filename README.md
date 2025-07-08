# AWS Serverless Image Recognition

This is a simple serverless project using AWS services to automatically detect objects in images uploaded to an S3 bucket.

Whenever an image is uploaded, a Lambda function automatically triggers and uses **AWS Rekognition** to analyze the image and detect objects.

---

## 🚀 Project Workflow:
1. Upload an image to the S3 bucket.
2. S3 triggers the Lambda function.
3. Lambda function sends the image to Rekognition for analysis.
4. Rekognition returns the objects found in the image.
5. Detected objects are shown in CloudWatch Logs.

---

## 📂 AWS Services Used:
- **S3:** Stores the uploaded images.
- **Lambda:** Runs the Python code automatically.
- **Rekognition:** Detects objects in the images.
- **IAM:** Provides permissions to services.
- **CloudWatch:** Shows logs and results.

---

## 📄 Files Included:
- `lambda_function.py` → The main Lambda function code.
- `README.md` → This project guide.

---

## ✅ Key Features:
- Fully serverless (no need to manage servers).
- Easy to set up and run.
- Uses powerful AWS AI services with minimal code.

---

## 📝 How to Use:
Follow this simple guide to build the project step by step:
1. Create S3 bucket and Lambda function.
2. Connect them through S3 Event Notifications.
3. Use the provided Python code in `lambda_function.py`.
4. Upload any photo to the bucket and see the magic in CloudWatch Logs!

---

## 🎉 Bonus Feature: Auto-Save Detection Results

In this project, the Lambda function also saves the detected objects into a text file inside the same S3 bucket.

### ✅ How It Works:
- Detects objects using Rekognition (like before).
- Saves a `.txt` file in the bucket with the results.
- No manual steps—everything happens automatically.

### ✅ Example:
If you upload an image called `cat.jpg`, you’ll also see a file like:

### cat.jpg_results.txt

This file will contain the detected objects and their confidence levels.

---

### ✅ Why This Is Cool:
- You automatically store detection results for future reference.
- No extra AWS services needed—it's all inside S3 and Lambda!
---

## 💡 Author:
*Sandeep Kasiraju*

---

## ✅ Notes:
- Remember to delete AWS resources after testing to avoid any charges.

---

