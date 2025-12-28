---
learning_level: "Beginner"
prerequisites:
  - "../01_bedrock-mental-models.md"
estimated_time: "10 minutes"
learning_objectives:
  - "Differentiate base models, foundation models, language models, and LLMs"
  - "Explain what Bedrock is and is not in system-design terms"
related_topics:
  prerequisites:
    - "../01_bedrock-mental-models.md"
  builds_upon:
    - "core-mental-models.md"
  enables: []
  cross_refs: []
---

# Session 01 (Module): Terminology + What Bedrock Is (and Isn’t)

## Foundation Models vs Base Models vs Language Models vs Large Language Models

These terms are often used interchangeably, but they describe **different dimensions of a model**, not different products.

Each term answers a **different question**:

* **Base Model** → *What training state is the model in?*
* **Foundation Model** → *How broadly can the model be reused?*
* **Language Model (LM)** → *What type of data does the model work with?*
* **Large Language Model (LLM)** → *How large and capable is the language model?*

### Practical Definitions

| Term                           | One-liner                                                                     | What It Describes  |
| ------------------------------ | ----------------------------------------------------------------------------- | ------------------ |
| **Base Model**                 | A raw, pre-trained model before task-specific tuning or alignment             | Training state     |
| **Foundation Model**           | A large, reusable model designed to support many downstream tasks             | Reusability        |
| **Language Model (LM)**        | A model that understands and generates human language                         | Text modality      |
| **Large Language Model (LLM)** | A large-scale language model with strong generalization and reasoning ability | Scale & capability |

### How These Terms Relate

* **Base model** describes *where the model is in its training lifecycle*
* **Foundation model** describes *how broadly the model can be applied*
* **Language model** describes *what kind of data the model works with*
* **LLM** describes *the size and capability of a language model*

Important clarifications:

* Not all foundation models are language models (some generate images or embeddings)
* Many foundation models are **aligned or fine-tuned versions** of base models
* LLMs are a **subset of language models**, not a separate category
* Amazon Bedrock uses **"Foundation Models"** as the umbrella term because it supports:

  * Text models
  * Image models
  * Embedding models
  * Multimodal models

### Architect Takeaway

When designing systems with Amazon Bedrock:

* You **consume foundation models** via a managed service
* You do **not manage base models or training pipelines**
* You may use **LLMs**, but also non-language models (embeddings, images)
* Design decisions should focus on **capabilities, cost, latency, and constraints**, not training internals

> In Bedrock, the question is not *"How is the model trained?"*
> It is *"Is this the right capability for my system design?"*

---

## Generative AI (Practically Defined)

Generative AI refers to models that **produce new content** based on learned patterns.

### Key Characteristics

* **Probabilistic** – same input may yield different outputs
* **Context-dependent** – output quality depends on prompt and context
* **Parameter-driven** – behavior is influenced by model parameters

This is fundamentally different from deterministic APIs.

---

## Prompt Engineering (Awareness Only)

Prompt engineering refers to the practice of **structuring inputs to foundation models** so that they produce useful, reliable, and cost-effective outputs.

At a high level, a prompt acts as:

* An **instruction**
* A **context boundary**
* A **behavioral constraint**

In Amazon Bedrock, prompts directly influence:

* Output quality
* Token consumption (cost)
* Consistency and variability
* Hallucination risk

Prompts are the primary control surface developers have over model behavior.

> Prompt engineering is not about clever wording — it is about **designing an interface to a probabilistic system**.

---

## Foundation Models

A **foundation model** is a large, pre-trained model that can be adapted to many tasks **without training from scratch**.

### Common Tasks

* Text generation and summarization
* Question answering
* Image generation
* Embedding creation

Foundation models trade **generality** for **cost and control**.

---

## What Amazon Bedrock Is

Amazon Bedrock is a **fully managed AWS service** that provides:

* API access to multiple foundation models
* Serverless inference (no infrastructure to manage)
* Enterprise-grade security and governance
* Model choice without vendor lock-in

> Bedrock is about **using models**, not training them.

---

## What Amazon Bedrock Is Not

Amazon Bedrock is **not**:

* A chatbot product
* A UI-first AI tool
* A replacement for SageMaker training workflows
* A framework like LangChain
* A deep learning tutorial platform

Bedrock is an **inference platform**, not an application or training service.

---

## What Is Intentionally Out of Scope

This session and repository **do not cover**:

* Neural network internals
* Backpropagation and optimizers
* CNN, RNN, LSTM architectures
* Model training pipelines
* Transfer learning mathematics

**Why:** Amazon Bedrock deliberately abstracts these away.

If asked:

> *“Don’t these models use neural networks?”*

**Answer:**

> *Yes — but Bedrock abstracts that away. As users, we design systems, not models.*

---

## Where Bedrock Fits in AWS

Think of AWS AI/ML services as layers:

* **High-level APIs:** Rekognition, Comprehend (task-specific)
* **Foundation model access:** Amazon Bedrock
* **Custom ML workflows:** Amazon SageMaker

Bedrock fills the gap between **fully managed AI APIs** and **full ML engineering**.

---

## The “Power Grid” Analogy

Think of Amazon Bedrock as a **power grid**:

* You don’t build the power plant (AWS manages models)
* You choose how much power you draw (model + parameters)
* You pay for what you consume (tokens)
* Your system determines efficiency and reliability

Bedrock gives **capability**, not **guarantees**.
