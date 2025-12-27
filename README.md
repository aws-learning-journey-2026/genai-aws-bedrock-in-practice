# GenAI with AWS Bedrock — In Practice

A hands-on, session-driven learning repository focused on understanding and building **Generative AI systems on AWS using Amazon Bedrock**, with emphasis on **mental models, architecture decisions, and production readiness**.

This repository is part of the **aws-learning-journey-2026** organization and documents a structured, practical exploration of Generative AI on AWS — learned in public and built incrementally.

---

## 🎯 Purpose of This Repository

This repository exists to:

* Learn **Amazon Bedrock the right way** — concept first, tooling second
* Move beyond demos to **real system design thinking**
* Understand **trade-offs**: cost, latency, security, accuracy
* Capture learnings in a **session-based, reusable format**

This is **not a packaged course** or certification guide.
It is a **living learning journey**, shaped by experimentation, mistakes, and architectural reasoning.

---

## 👥 Who This Is For

* Developers exploring Generative AI on AWS
* Cloud engineers moving into GenAI workloads
* Software architects designing GenAI systems
* Learners who prefer **understanding over memorization**

Basic familiarity with AWS concepts is helpful, but **no prior GenAI experience is required**.

---

## 🧠 Learning Philosophy — “In Practice”

“In practice” means:

* Mental models before APIs
* Architecture before frameworks
* Why before how
* Production thinking, even in small examples

Each session is designed to fit into **~30 minutes**, making it suitable for:

* Self-study
* Live meetups
* Team learning sessions

---

## 🗂️ Session Structure (30 Minutes Each)

| Session | Topic                                                   | Deliverable                                    |
| ------- | ------------------------------------------------------- | ---------------------------------------------- |
| 01      | Bedrock Mental Models & GenAI Foundations               | One-page mental model note + glossary          |
| 02      | Bedrock Platform Deep Dive (Console-First)              | Model selection checklist + risk notes         |
| 03      | Model Exploration & Prompt Behavior                     | Prompt experiment log                          |
| 04      | Bedrock APIs & SDKs                                     | Minimal "hello inference" snippets + error handling |
| 05      | Designing a Minimal GenAI Backend on AWS               | Architecture diagram + API contract sketch    |
| 06      | Embeddings & Vector Thinking                            | Chunking strategy guide                        |
| 07      | Retrieval-Augmented Generation (RAG) with Bedrock       | RAG reference architecture + anti-pattern checklist |
| 08      | Advanced Capabilities (Knowledge Bases / Agents)        | "Choose your orchestration" decision tree      |
| 09      | Production Readiness: Security, Cost, Observability      | Production readiness checklist                 |

> Additional sessions may be added as the platform evolves.

---

## 📁 Repository Structure

```text
genai-aws-bedrock-in-practice/
├── docs/
│   ├── 01_master-plan.md          # Master plan and roadmap
│   ├── sessions/                   # Session content (30-min format)
│   │   ├── 01_bedrock-mental-models.md
│   │   ├── 02_bedrock-platform-deep-dive.md
│   │   └── ... (additional sessions)
│   ├── meetup/                     # Meetup materials and slides
│   └── images/                     # Diagrams and visual assets
├── src/                            # Minimal runnable labs/examples
├── source-material/                # Staging area for imported content (git-ignored)
└── README.md
```

Session content is organized under `docs/sessions/` as individual markdown files. Each session follows a consistent 30-minute format and includes:

* Core concepts and mental models
* Hands-on reasoning and applied examples
* Deliverable artifacts (notes, diagrams, checklists, or minimal code)

---

## 🔍 What This Repository Does *Not* Aim to Do

* ❌ Replicate Udemy or official AWS documentation
* ❌ Cover every Bedrock feature exhaustively
* ❌ Provide copy-paste production code

Instead, it focuses on **understanding how to think about GenAI systems on AWS**.

---

## 🔄 Living Repository

This repository will evolve as:

* Amazon Bedrock adds new capabilities
* GenAI best practices mature
* Real-world lessons are learned

Expect refinement, reorganization, and occasional rewrites.

---

## 📌 Disclaimer

This is a **personal learning and knowledge-sharing repository**.
It is **not official AWS training material** and does not represent Amazon or its affiliates.

---

## 🚀 Where to Start

Begin with:

👉 **`docs/sessions/01_bedrock-mental-models.md`**

Everything else builds on that foundation.

---

## 📋 Principles (Non-Negotiables)

* **Architecture-first**: Start from mental models, then APIs, then systems
* **Practice-oriented**: Each session produces an artifact (notes, diagram, checklist, or minimal code)
* **Production-aware**: Security, cost, observability, and failure modes are first-class
* **Original content**: No course-clone structure or copied marketing text

---

## 📚 Learning Roadmap

See `docs/01_master-plan.md` for the complete learning roadmap and session details.
