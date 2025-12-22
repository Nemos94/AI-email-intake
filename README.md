# AI_email_intake

Overview
This project implements an end-to-end AI-powered email intake system that processes real customer emails and automatically creates Salesforce Cases with AI-generated draft responses.

The solution is designed with enterprise-grade patterns, keeping the human agent in the loop while reducing manual effort and response time.

Problem
Customer support teams spend a large amount of time:

Reading incoming emails
Understanding intent and urgency
Creating Salesforce Cases manually
Drafting repetitive responses
This process is slow, error-prone, and difficult to scale.

Solution
An automated pipeline that:

Receives real emails via Gmail
Uses AI (OpenAI GPT) to analyze content, sentiment, and urgency
Returns a strictly validated JSON contract
Routes requests using n8n
Creates Salesforce Cases automatically
Generates an AI-assisted draft response using Salesforce Flow
Keeps a human-in-the-loop for governance and quality control
Architecture
Customer Email
      ↓
Gmail Inbox
      ↓
n8n (Email Trigger & Routing)
      ↓
FastAPI Backend
  - JSON Contract
  - Validation
      ↓
OpenAI (GPT)
      ↓
n8n (Decision Logic)
      ↓
Salesforce
  - Case Creation
  - Record-Triggered Flow
  - AI Draft Response
Technology Stack
OpenAI GPT – AI reasoning and response generation
Python + FastAPI – Backend API
Pydantic – Strict schema validation
n8n – Automation and orchestration
Salesforce Service Cloud
Salesforce Flow – Declarative automation (no Apex / no LWC)
Gmail API – Real email ingestion
