# Master Plan — genai-aws-bedrock-in-practice

Date: 27 Dec 2025

## Purpose

Build a practical, architecture-first learning repository for creating Generative AI solutions on AWS using Amazon Bedrock.

This repo is optimized for:

* Self-study in timeboxed sessions
* Small-group meetup delivery
* “Explain and defend the design” style learning (not demo-only)

## Principles (Non-Negotiables)

* Architecture-first: start from mental models, then APIs, then systems.
* Practice-oriented: each session produces an artifact (notes, diagram, checklist, or minimal code).
* Production-aware: security, cost, observability, and failure modes are first-class.
* Original content: no course-clone structure or copied marketing text.

## Intended Audience

* Builders who can write basic code (any language) but want stronger GenAI system design skills on AWS.
* Architects/TPMs who need clarity on trade-offs, governance, and readiness.

## Session Format (30 minutes)

Each session should fit in 30 minutes and ship with a single primary artifact.

Recommended structure per session:

1. Objective (1–2 minutes)
2. Core concepts (10–12 minutes)
3. Hands-on / applied reasoning (12–15 minutes)
4. Output artifact + recap (2–5 minutes)

## Repository Layout (Current)

* `docs/` — plans, meetup material, and session write-ups
* `src/` — reserved for minimal runnable labs/examples (currently empty)
* `source-material/` — staging area for imported/raw notes (git-ignored)

## Learning Roadmap (Sessions)

### 01. Bedrock Mental Models & GenAI Foundations

Focus: vocabulary and conceptual clarity.

Deliverable: a one-page “Bedrock mental model” note + glossary.

### 02. Bedrock Platform Deep Dive (Console-First)

Focus: what the service is, how it’s operated, and what constraints matter.

Deliverable: a decision checklist for model selection + risk notes.

### 03. Model Exploration & Prompt Behavior

Focus: prompt behavior, determinism vs creativity, and prompt-as-contract.

Deliverable: a prompt experiment log (same prompt across models + observations).

### 04. Bedrock APIs & SDKs

Focus: request/response anatomy, errors, retries, and integration patterns.

Deliverable: minimal “hello inference” snippets + error-handling notes.

### 05. Designing a Minimal GenAI Backend on AWS

Focus: Lambda/API Gateway integration, sync vs async inference, statelessness.

Deliverable: an architecture diagram + API contract sketch.

### 06. Embeddings & Vector Thinking

Focus: embeddings, chunking, similarity search intuition, failure modes.

Deliverable: a chunking strategy guide (rules of thumb + pitfalls).

### 07. Retrieval-Augmented Generation (RAG) with Bedrock

Focus: ingestion → embeddings → retrieval → generation, grounding techniques.

Deliverable: RAG reference architecture + anti-pattern checklist.

### 08. Advanced Capabilities (Knowledge Bases / Agents)

Focus: when to use managed capabilities vs custom orchestration.

Deliverable: “choose your orchestration” decision tree.

### 09. Production Readiness: Security, Cost, Observability

Focus: IAM least privilege, networking, token/cost controls, monitoring.

Deliverable: production readiness checklist (security + cost + ops).

## Folder Mapping (Planned)

The simplest starting point is to keep session content under `docs/sessions/`.

Example:

* `docs/sessions/01_bedrock-mental-models/01_bedrock-mental-models.md`
* `docs/sessions/02_bedrock-platform-deep-dive/02_bedrock-platform-deep-dive.md`

## Next Steps

1. Convert Session 01 into a concrete write-up under `docs/sessions/`.
2. Add a small, consistent session template (so every session feels uniform).
3. Expand the root README once Session 01 exists (so the repo has a solid entry point).
