# RAG – Retrieval-Augmented Generation Layer

This folder contains the **Retrieval-Augmented Generation (RAG)** implementation used by the AI-powered email intake system.

The goal of this layer is to ensure that AI-generated responses are **grounded in internal company knowledge**, avoiding hallucinations and improving accuracy, consistency, and governance.

---

## 📌 Purpose

The RAG layer allows the AI to:

- Search internal documentation (policies, FAQs, SLAs)
- Retrieve the most relevant content
- Inject that context into the AI prompt
- Generate responses **only based on retrieved knowledge**

If the required information is not found, the AI explicitly escalates instead of guessing.

---

## 🧱 Architecture Overview

```
Customer Email
      ↓
FastAPI (/intake)
      ↓
Vector Database (Chroma)
      ↓
Relevant Document Chunks
      ↓
OpenAI GPT (with context)
      ↓
Structured JSON Response
```

The RAG layer is fully contained within the FastAPI service and is **decoupled from orchestration (n8n) and Salesforce**.

---

## 📂 Folder Structure

```
rag/
├── ingest.py          # One-time (or on-change) document ingestion
├── knowledge/         # Internal documentation (Markdown / TXT)
│   ├── support_faq.md
│   ├── billing_policy.md
│   └── sla.md
├── vectorstore/       # Persisted embeddings (generated)
└── README.md          # This file
```

---

## 📄 Knowledge Documents

Documents should be:

- Written in Markdown or plain text
- Clear and factual
- Short and well-structured
- Free of speculative or ambiguous language

Example document types:
- Support FAQs
- Billing & refund policies
- SLAs
- Troubleshooting guides

---

## 🔄 Ingestion Process

The ingestion process is executed **manually** and **offline**.

### Run ingestion:
```bash
python ingest.py
```

This process:
1. Loads documents from `knowledge/`
2. Splits them into chunks
3. Creates embeddings
4. Stores them in a local Chroma vector database

⚠️ Embeddings are **not** created at runtime.

---

## 🧠 Runtime Retrieval

At runtime, the FastAPI service:

1. Receives the customer message
2. Queries the vector database
3. Retrieves the most relevant chunks
4. Injects them into the AI prompt
5. Generates a response grounded in documentation

No documents → no assumptions.

---

## 🧪 Validation

The RAG implementation was validated using **contrast testing**:

- With vectorstore enabled → responses reference internal rules
- With vectorstore removed → responses degrade gracefully
- Out-of-scope questions → explicit escalation (no hallucination)

---

## 🏗️ Design Principles

- Contract-first AI
- Human-in-the-loop by design
- No fine-tuning required
- Low operational cost
- Enterprise-ready patterns

---

## 🚀 Status

✅ Fully implemented  
✅ Tested with real emails  
✅ Integrated with Salesforce via Flow  

---

## 📎 Notes

This RAG implementation is intentionally simple and maintainable.
More advanced features (dynamic ingestion, UI management, multi-source retrieval) can be added incrementally if required.
