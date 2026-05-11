# 🚀 Intelligent Event-Driven Pipeline with DLQ Recovery

## 📌 Overview

This project demonstrates a fault-tolerant serverless architecture built using AWS.

It processes events, handles failures using SQS (Dead Letter Queue), and automatically recovers failed events with intelligent analysis.

---

## 🏗️ Architecture

S3 → Lambda → DynamoDB
↓
SQS (DLQ) → Recovery Lambda → DynamoDB

---

## ⚙️ Services Used

* AWS Lambda
* Amazon S3
* Amazon DynamoDB
* Amazon SQS (DLQ)
* Amazon CloudWatch

---

## 🔄 Workflow

1. File uploaded to S3
2. Lambda processes event
3. If failure occurs → sent to SQS
4. Recovery Lambda retries failed events
5. Intelligent analysis identifies possible failure causes
6. Results stored in DynamoDB

---

## 📸 Screenshots

### S3 Upload

![S3](screenshots/s3-upload.png)

### Lambda Logs

![Logs](screenshots/lambda-logs.png)

### SQS Queue

![SQS](screenshots/sqs-queue.png)

### DynamoDB

![DynamoDB](screenshots/dynamodb-table.png)

---

## 💡 Key Features

* Event-driven architecture
* Fault tolerance using DLQ
* Auto-recovery system
* Intelligent failure analysis
* Serverless design

---

## 📌 Author

Nithin Rallapalli
