# 🚀 Serverless Event Management System

## 📌 Overview
A cloud-based serverless backend system to manage events and user registrations.  
Built using AWS services, this project demonstrates REST API development, serverless architecture, and NoSQL database integration.

---

## 🏗️ Architecture
Client → API Gateway → AWS Lambda → DynamoDB

---

## 🚀 Features
- Create events via API
- Register users for events
- Store data in DynamoDB
- Fully serverless (no servers required)
- Scalable and cost-efficient design

---

## 🛠️ Tech Stack
- AWS Lambda (Backend logic)
- API Gateway (REST API)
- DynamoDB (NoSQL database)
- Python (Runtime)

---

## 📡 API Endpoints
### Base URL
https://your-api-url.execute-api.ap-south-1.amazonaws.com/default/helloEvent

### 🔹 Create Event
**POST**

Request:

```json
{
  "action": "create_event",
  "title": "Tech Talk"
}

Response:

```json
{
  "message": "Event created",
  "event_id": "uuid"
}

🔹 Register User

POST

Request:

```json
{
  "action": "register",
  "event_id": "EVENT_ID",
  "email": "user@gmail.com"
}

Response:

```json
{
  "message": "Registered successfully",
  "registration_id": "uuid"
}

🔹 Get Events (Optional)

POST

Request:

```json
{
  "action": "get_events"
}


## 🧪 Testing

Tested using Postman

Sent POST requests with JSON body

Verified responses and database entries


## 🗂️ Project Structure

event-system/
│
├── lambda_function.py
├── README.md

## 📷 Screenshots

![Postman Output](screenshot.png)

## 🧠 Key Learnings

Implemented serverless architecture using AWS

Integrated API Gateway with Lambda functions

Designed NoSQL schema using DynamoDB

Managed IAM roles and permissions

Handled JSON-based API requests


🔮 Future Improvements

Add email notifications (AWS SES)

Generate QR codes for event registration

Build frontend (React / HTML)

Add authentication (AWS Cognito)



👨‍💻 Author

Surya P