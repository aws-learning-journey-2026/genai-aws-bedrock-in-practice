# Meetup Sessions - Dot Net Learners House

This document tracks meetup sessions conducted by Dot Net Learners House based on the `genai-aws-bedrock-in-practice` repository content.

---

## Session 2

**Title**: Bedrock Platform Deep Dive (Console-First)

**Date**: Thursday, January 8, 2026 · 9:00 PM to 10:00 PM IST

**Duration**: 30 minutes

**Type**: Live demo + guided experimentation

**Deliverable**: Decision checklist for model selection + risk notes

### Why This Session

You should feel model behavior before writing code. This session focuses on what the service is, how it's operated, and what constraints matter.

Understanding the Bedrock console and model catalog is essential for making informed decisions about which models to use and how to configure them for your use cases.

### Agenda

#### 1. Bedrock Console & Model Catalog

* Navigating the Bedrock console
* Understanding the model catalog
* Model categories: text, chat, image, embeddings
* Model availability and regional considerations

#### 2. Text & Chat Playground Deep Dive

* Same prompt, different models — comparing outputs
* Parameter tuning and output changes
* Temperature, top-p, and other inference parameters
* Understanding model behavior patterns

#### 3. Image Generation Playground

* Image generation models overview
* Prompt patterns for image generation
* Practical use cases and considerations
* Quality and cost trade-offs

#### 4. Responsible AI & Guardrails

* Content filtering and safety features
* Guardrails configuration
* Best practices for responsible AI usage
* Risk assessment and mitigation

#### 5. Key Takeaways & Deliverable

* Model selection decision framework
* Risk notes and constraints
* Deliverable: Create your model selection checklist + risk notes

---

## Session 1

**Title**: Amazon Bedrock — The Right Mental Model for Generative AI on AWS - Session 1

**Date**: Sunday, December 28, 2025 · 9:00 AM to 10:00 AM IST

**Duration**: 30 minutes

**Type**: Conceptual + light demo

**Deliverable**: One-page "Bedrock mental model" note + glossary

### Why This Session

Before tools, you need clarity. This session eliminates confusion about what Bedrock is and how to think about it.

Most failures with Generative AI on AWS happen **before code is written**:

* Teams confuse Bedrock with SageMaker
* Developers treat LLMs like deterministic APIs
* Architects design systems without understanding token costs or model behavior

Without the right mental model, every design decision downstream is flawed. This session establishes the conceptual foundation required for **all subsequent sessions**.

### Agenda

#### 1. Generative AI on AWS: The Big Picture

* AWS AI/ML service landscape
* Where Bedrock fits: High-level APIs → Bedrock → SageMaker
* Bedrock vs OpenAI vs Azure OpenAI vs SageMaker

#### 2. The AI Hierarchy (Minimal Mental Model)

* Artificial Intelligence → Machine Learning → Neural Networks → Deep Learning → Generative AI → Foundation Models → Amazon Bedrock
* Essential concepts and terminology
* What Bedrock abstracts away (and why it matters)

#### 3. Foundation Models & Trade-offs

* What foundation models are (and aren't)
* Text, chat, image, embeddings
* Cost, latency, quality, determinism
* Generality vs. control trade-offs

#### 4. What Amazon Bedrock Actually Is (and Isn't)

* Managed foundation model platform
* Serverless inference, model choice, enterprise controls
* What Bedrock is NOT (common misconceptions)
* The "Power Grid" analogy

#### 5. Key Vocabulary & Wrap-up

* Essential terms: Generative AI, Foundation Model, Inference, Token, Prompt, Bedrock
* Architecture considerations
* Deliverable: Create your one-page mental model note + glossary

---

**Related Session Content**: [`docs/sessions/01_bedrock-mental-models.md`](../sessions/01_bedrock-mental-models.md)

**Master Plan Reference**: [`docs/01_master-plan.md`](../01_master-plan.md) - Session 01

---

**Related Session Content**: [`docs/sessions/02_bedrock-platform-deep-dive.md`](../sessions/02_bedrock-platform-deep-dive.md) (planned)

**Master Plan Reference**: [`docs/01_master-plan.md`](../01_master-plan.md) - Session 02
