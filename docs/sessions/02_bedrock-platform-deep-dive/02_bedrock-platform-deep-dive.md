---
learning_level: "Beginner"
prerequisites:
  - "../01_bedrock-mental-models/01_overview.md"
estimated_time: "30 minutes"
learning_objectives:
  - "Navigate the Bedrock console and model catalog with a clear purpose"
  - "Explain key model selection trade-offs (cost, latency, quality, region availability)"
  - "Produce a simple model-selection checklist + risk notes for a use case"
related_topics:
  prerequisites:
    - "../01_bedrock-mental-models/01_overview.md"
  builds_upon: []
  enables: []
  cross_refs: []
---

# Session 02: Bedrock Platform Deep Dive (Console-First)

**Duration**: ~30 minutes  
**Date**: [Set date]  
**Deliverable**: Decision checklist for model selection + risk notes

---

## 1. Objective (1–2 minutes)

**What you'll learn:**

- How to navigate the Bedrock console with “architecture intent”
- What constraints matter early (regions, quotas, permissions, model availability)
- How to compare models using a small, repeatable evaluation checklist

**Why it matters:**

Most downstream failures happen when teams pick models “by vibe” (or by headline benchmarks) without matching constraints and trade-offs.

---

## 2. Core Concepts (10–12 minutes)

### Console mental model

- Bedrock as “inference platform + governance surface”
- Model catalog: model families and capability differences
- Where parameters live (temperature/top-p/max tokens) and what they affect

### Model selection trade-offs

- Cost vs quality
- Latency vs throughput
- Safety controls vs flexibility
- Regional availability vs compliance needs

---

## 3. Hands-on / Applied Reasoning (12–15 minutes)

### Mini-experiment

Run the same prompt across 2–3 models (text/chat) and vary one parameter (temperature).

Capture:

- Output differences
- Latency “feel”
- Any policy/safety differences you notice

---

## 4. Output Artifact + Recap (2–5 minutes)

### Deliverable

Create a one-page checklist:

- Use case and success criteria
- Candidate models and why
- Constraints (region, latency, budget, safety)
- Prompt + parameter defaults
- Risks (hallucination, cost spikes, instability) + mitigations

### Next Steps

Continue to Session 03 (planned): model exploration and prompt behavior.

---

**Session Status**: Draft
