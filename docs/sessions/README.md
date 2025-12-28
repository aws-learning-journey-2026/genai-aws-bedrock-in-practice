# Session Index Dashboard

This document provides detailed information about each learning session, including modules, learning outcomes, and navigation.

**Repository**: `genai-aws-bedrock-in-practice`  
**Format**: 30-minute focused sessions  
**Approach**: Architecture-first, production-aware learning

> **📋 Session Overview**: For the complete session roadmap, status table, and progression diagram, see the [Session Overview](../04_session-overview.md) (single source of truth).

---

---

## Session Details

### Session 01: Bedrock Mental Models & GenAI Foundations ✅

**Status**: Complete  
**Location**: [`01_bedrock-mental-models/`](01_bedrock-mental-models/)  
**Overview**: [`01_overview.md`](01_bedrock-mental-models/01_overview.md)

**Modules**:

1. [Core Mental Models](01_bedrock-mental-models/02_core-mental-models.md) - AI hierarchy, model definitions
2. [Tokens](01_bedrock-mental-models/03_tokens.md) - Tokenization, cost implications
3. [Terminology & Scope](01_bedrock-mental-models/04_terminology-and-scope.md) - Foundation models, Bedrock positioning
4. [Applied Reasoning & Artifact](01_bedrock-mental-models/05_applied-reasoning-and-artifact.md) - Decision framework, output artifact

**Learning Outcomes**:
- Explain the minimal AI hierarchy relevant to Bedrock users
- Define what a model is (and is not) in practical terms
- Describe what Amazon Bedrock is and is not for system design

**Deliverable**: One-page Bedrock Mental Model note + glossary

**Prerequisites**: None (starting point)

**Enables**: Session 02

---

### Session 02: Bedrock Platform Deep Dive (Console-First) 🔄

**Status**: Draft  
**Location**: [`02_bedrock-platform-deep-dive/`](02_bedrock-platform-deep-dive/)  
**Overview**: [`02_bedrock-platform-deep-dive.md`](02_bedrock-platform-deep-dive/02_bedrock-platform-deep-dive.md)

**Learning Outcomes**:
- Navigate the Bedrock console and model catalog with a clear purpose
- Explain key model selection trade-offs (cost, latency, quality, region availability)
- Produce a simple model-selection checklist + risk notes for a use case

**Deliverable**: Decision checklist for model selection + risk notes

**Prerequisites**: Session 01

**Enables**: Session 03

---

### Session 03: Model Exploration & Prompt Behavior 📋

**Status**: Planned  
**Focus**: Prompt behavior, determinism vs creativity, prompt-as-contract

**Deliverable**: Prompt experiment log (same prompt across models + observations)

**Prerequisites**: Session 02

**Enables**: Session 04

---

### Session 04: Bedrock APIs & SDKs 📋

**Status**: Planned  
**Focus**: Request/response anatomy, errors, retries, integration patterns

**Deliverable**: Minimal "hello inference" snippets + error-handling notes

**Prerequisites**: Session 03

**Enables**: Session 05

---

### Session 05: Designing a Minimal GenAI Backend on AWS 📋

**Status**: Planned  
**Focus**: Lambda/API Gateway integration, sync vs async inference, statelessness

**Deliverable**: Architecture diagram + API contract sketch

**Prerequisites**: Session 04

**Enables**: Session 06

---

### Session 06: Embeddings & Vector Thinking 📋

**Status**: Planned  
**Focus**: Embeddings, chunking, similarity search intuition, failure modes

**Deliverable**: Chunking strategy guide (rules of thumb + pitfalls)

**Prerequisites**: Session 05

**Enables**: Session 07

---

### Session 07: Retrieval-Augmented Generation (RAG) with Bedrock 📋

**Status**: Planned  
**Focus**: Ingestion → embeddings → retrieval → generation, grounding techniques

**Deliverable**: RAG reference architecture + anti-pattern checklist

**Prerequisites**: Session 06

**Enables**: Session 08

---

### Session 08: Advanced Capabilities (Knowledge Bases / Agents) 📋

**Status**: Planned  
**Focus**: When to use managed capabilities vs custom orchestration

**Deliverable**: "Choose your orchestration" decision tree

**Prerequisites**: Session 07

**Enables**: Session 09

---

### Session 09: Production Readiness: Security, Cost, Observability 📋

**Status**: Planned  
**Focus**: IAM least privilege, networking, token/cost controls, monitoring

**Deliverable**: Production readiness checklist (security + cost + ops)

**Prerequisites**: Session 08

**Enables**: None (final session)

---

> **📋 For session roadmap, status table, and learning flow**: See [Session Overview](../04_session-overview.md)

---

## Quick Navigation

### By Status

- **Complete**: [Session 01](01_bedrock-mental-models/)
- **Draft**: [Session 02](02_bedrock-platform-deep-dive/)
- **Planned**: Sessions 03-09

### By Learning Stage

- **Foundations**: Sessions 01-03
- **Integration**: Sessions 04-06
- **Advanced**: Sessions 07-09

---

## Contributing New Sessions

When creating new sessions:

1. Follow the [Session Template](../01_session-template.md)
2. Use the naming convention: `NN_session-topic/01_overview.md`, `02_module-name.md`, etc.
3. Update this README with session details
4. Ensure all prerequisites are complete
5. Add proper YAML frontmatter with learning objectives

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for detailed guidelines.

---

## Related Resources

- **Session Overview**: [`../04_session-overview.md`](../04_session-overview.md) - **Single source of truth** for session roadmap and status
- **Master Plan**: [`../03_master-plan.md`](../03_master-plan.md)
- **Session Template**: [`../templates/session-template.md`](../templates/session-template.md)
- **Repository Structure**: [`../03_repository-structure.md`](../03_repository-structure.md)
- **Main README**: [`../../README.md`](../../README.md)

---

**Last Updated**: January 2025  
**Maintainer**: Viswanatha Swamy P K

> **Note**: For session roadmap and status, see [`../04_session-overview.md`](../04_session-overview.md) (single source of truth).
