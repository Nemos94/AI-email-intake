# Salesforce – AI Case Intake Integration

## Overview
This folder documents the **Salesforce side** of the AI-powered email intake solution.

Salesforce is responsible for:
- Receiving AI-generated data from the automation layer
- Creating Cases automatically
- Exposing AI-generated draft responses to support agents


No custom Apex or LWC components are required.

---

## Objects Used

### Case (Standard Object)
The Case object is used to represent incoming customer requests classified by AI.

Cases are automatically created by the n8n workflow based on AI output.

---

## Custom Fields

### `AI_Draft_Response__c`
- Type: Long Text Area
- Object: Case
- Purpose:
  Stores the AI-generated draft response suggested for the support agent.

This field is populated during Case creation and later consumed by a Salesforce Flow.

---

## Salesforce Flow

A **Record-Triggered Flow** is used to surface the AI-generated response to the agent.

### Flow Characteristics
- Triggered when a Case is created
- Runs only if `AI_Draft_Response__c` is populated
- Displays the AI draft to the agent
- Allows review and editing before sending any response

### Design Principles
- Declarative (Flow only)
- No Apex
- No LWC
- Low maintenance
- Enterprise-friendly

---
