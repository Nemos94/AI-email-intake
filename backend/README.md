# AI-Powered Email Intake for Salesforce

## Overview
This project implements an **end-to-end AI-powered email intake system** that processes real customer emails and automatically creates Salesforce Cases with AI-generated draft responses.

The solution is designed with **enterprise-grade patterns**, keeping the **human agent in the loop** while reducing manual effort and response time.

---

## Problem
Customer support teams spend a large amount of time:
- Reading incoming emails
- Understanding intent and urgency
- Creating Salesforce Cases manually
- Drafting repetitive responses

This process is slow, error-prone, and difficult to scale.

---

## Solution
An automated pipeline that:
1. Receives **real emails** via Gmail  
2. Uses **AI (OpenAI GPT)** to analyze content, sentiment, and urgency  
3. Returns a **strictly validated JSON contract**  
4. Routes requests using **n8n**  
5. Creates **Salesforce Cases automatically**  
6. Generates an **AI-assisted draft response** using Salesforce Flow  
7. Keeps a **human-in-the-loop** for governance and quality control  

---

## Architecture

```
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
```

---

## Technology Stack
- **OpenAI GPT** – AI reasoning and response generation
- **Python + FastAPI** – Backend API
- **Pydantic** – Strict schema validation
- **n8n** – Automation and orchestration
- **Salesforce Service Cloud**
- **Salesforce Flow** – Declarative automation (no Apex / no LWC)
- **Gmail API** – Real email ingestion

---

## Backend API

### Endpoint
`POST /intake`

### Request
```json
{
  "message": "Bom dia, estou extremamente insatisfeito. Já contactei várias vezes e ninguém responde.",
  "source": "email"
}
```

### Response
```json
{
  "objectType": "Case",
  "category": "Technical Issue",
  "priority": "High",
  "sentiment": "Negative",
  "summary": "Cliente expressa forte insatisfação devido à falta de resposta e a um problema técnico não resolvido.",
  "suggestedResponse": "Lamentamos a situação. Vamos tratar do seu caso com prioridade máxima e entraremos em contacto o mais rapidamente possível."
}
```

---

## Key Design Decisions

### Why n8n?
- Clear orchestration and routing logic
- Easy integration with external services
- Decouples automation from CRM logic

### Why FastAPI?
- Centralized AI logic
- Enforces strict contracts
- Easy to extend (RAG, caching, retries)

### Why strict JSON validation?
- Prevents AI hallucinations from breaking downstream systems
- Ensures Salesforce-safe data
- Enterprise-grade reliability

### Why Salesforce Flow instead of Apex or LWC?
- Lower maintenance cost
- Declarative and transparent
- Aligned with Salesforce best practices

### Why Human-in-the-Loop?
- Compliance and governance
- Avoids automatic external communication
- Matches real enterprise AI adoption patterns

---

## Project Status
✅ Fully functional end-to-end  
📧 Real email ingestion  
🤖 AI-powered classification  
☁️ Salesforce Case creation  
✉️ AI draft response via Flow  

🔜 Planned: Retrieval-Augmented Generation (RAG)

---

## Running Locally (Backend)

```bash
export OPENAI_API_KEY=your_api_key_here
uvicorn main:app --reload
```

Open:
```
http://localhost:****/docs
```

---

## Notes
- No credentials are stored in the repository
- API keys are injected via environment variables
- This repository is intended as a **portfolio and reference project**, not a turnkey product
