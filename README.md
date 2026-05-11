# 🚀 Intelligent Event Pipeline with AI-Based Failure Analysis

## 📌 Overview

This project demonstrates a **fault-tolerant, AI-enhanced serverless pipeline** built using AWS.

It not only processes events and recovers failures, but also **analyzes failures intelligently** to suggest possible fixes.

---

## 🧠 What Makes This Different?

Most pipelines only retry failures.
This system **understands failures** and gives insights like:

* “S3 event structure issue”
* “Missing fields in payload”
* “Trigger misconfiguration”

---

## 🏗️ Architecture

S3 → Lambda (Event Processor) → DynamoDB
↓
SQS (DLQ) → Recovery Lambda → DynamoDB (+ AI Analysis)

---

## ⚙️ Services Used

* AWS Lambda
* Amazon S3
* Amazon DynamoDB
* Amazon SQS (Dead Letter Queue)
* Amazon CloudWatch
* AI Logic (rule-based / API-ready design)

---

## 🔄 Workflow

1. Upload JSON file to S3
2. Lambda processes event
3. If failure occurs → message sent to SQS
4. Recovery Lambda retries failed event
5. AI module analyzes failure reason
6. Result + analysis stored in DynamoDB

---

## 🤖 AI Integration

The recovery system includes an **AI-inspired analysis engine** that:

* Detects common failure patterns
* Suggests possible fixes
* Stores insights alongside recovered data

Example output:

```json
{
  "status": "recovered",
  "analysis": "S3 event processing issue. Fix: Validate event structure and triggers."
}
```

---

## 📸 Screenshots

### 🔹 Event Processor (S3 Trigger)

![EventProcessor] <img width="897" height="256" alt="screenshots:lambda-1-logs" src="https://github.com/user-attachments/assets/b28a4f15-788f-4a75-98bd-10cd8fbf4f2b" /> 


### 🔹 Recovery Worker (SQS Trigger)
![RecoveryWorker] <img width="897" height="256" alt="screenshots:lambda-1-logs" src="https://github.com/user-attachments/assets/df1fbcf4-79dd-4356-8722-f9e200b9b6bc" />



### 🔹 CloudWatch Logs (AI Analysis)

![Logs] <img width="1680" height="832" alt="Screenshot 2026-05-11 at 7 22 38 AM" src="https://github.com/user-attachments/assets/b3c2f5d4-150e-49a9-b4ae-40f69f477349" />


### 🔹 SQS Queue (Failed Messages)

![SQS] <img width="1680" height="381" alt="screenshots:sqs-queue" src="https://github.com/user-attachments/assets/aef0a3d9-bdc5-4eac-b68e-1a622658e61c" />


### 🔹 DynamoDB (Recovered + AI Analysis)

![DynamoDB] <img width="1680" height="835" alt="screenshots:dynamodb-table" src="https://github.com/user-attachments/assets/ca8f6176-b24d-4d8d-96c7-1c0595e7ba5d" />


### 🔹 S3 Upload (Input Files)

![S3] <img width="1680" height="880" alt="screenshots:s3-upload" src="https://github.com/user-attachments/assets/411c38ad-a431-47b3-94e7-c9ef49f2f9c9" />

---

## 💡 Key Features

* Event-driven architecture
* Dead-letter queue (DLQ) handling
* Automatic failure recovery
* AI-based failure analysis
* Serverless and scalable

---

## 🚀 Outcome

Built a **production-style resilient system** that not only prevents data loss but also **helps debug failures automatically**.

---

## 👨‍💻 Author

Nithin Rallapalli
