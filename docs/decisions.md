# Technical Decisions

This document explains the **key architectural and technical decisions** taken during
the design and implementation of the AI-powered email intake solution.

The goal is to highlight *why* certain choices were made, not just *what* was built.

---

## Why n8n as the Orchestration Layer

n8n was chosen as the central orchestration layer instead of implementing
direct integrations inside Salesforce.

**Reasons:**
- Clear visualization of automation logic
- Easier integration with external AI services
- Separation of concerns between orchestration and CRM
- Faster iteration during experimentation

n8n acts as the glue between email ingestion, AI reasoning, and Salesforce execution.

---

## Why FastAPI as an AI Backend

A dedicated FastAPI service is used instead of calling OpenAI directly from n8n.

**Reasons:**
- Centralized AI logic
- Strict contract enforcement using Pydantic
- Easier testing and debugging
- Future extensibility (RAG, caching, retries)

This layer ensures downstream systems never consume unvalidated AI output.

---

## Why a Strict JSON Contract

The AI output is validated against a strict JSON schema before being used.

**Reasons:**
- Prevents AI hallucinations from breaking automations
- Guarantees Salesforce-safe data
- Makes the system deterministic and reliable
- Aligns with enterprise integration patterns

This approach treats AI as an unreliable input source that must be controlled.

---

## Why Salesforce Flow Instead of Apex or LWC

Salesforce Flow was intentionally chosen as the execution layer inside Salesforce.

**Reasons:**
- Lower long-term maintenance cost
- Declarative and transparent logic
- Easier adoption by admins and consultants
- Aligned with Salesforce best practices

No Apex code or custom UI components are required.

---

## Why Human-in-the-Loop

The system is designed so that AI never communicates directly with customers.

**Reasons:**
- Governance and compliance
- Avoids accidental or incorrect outbound communication
- Matches real enterprise AI adoption patterns

AI assists agents, but humans remain in control.

---

## Why Screenshots Instead of Raw n8n JSON

The n8n workflow is documented using screenshots rather than executable JSON.

**Reasons:**
- Improved readability
- Reduced security concerns
- Clearer communication for non-technical stakeholders
- Better suited for portfolio and presentation purposes

The actual implementation details remain available during live demonstrations.

---

## Trade-offs and Limitations

- This solution prioritizes clarity and governance over full automation
- Response sending is not automated by design
- Deployment is local and demo-oriented

These trade-offs are intentional and align with the project goals.

---

## Future Improvements

- Retrieval-Augmented Generation (RAG)
- Centralized logging and monitoring
- Error handling and retry mechanisms
- Cloud deployment for the AI backend

---

## Summary

The architecture favors:
- Reliability over novelty
- Governance over full automation
- Maintainability over complexity

These decisions reflect real-world enterprise constraints.
