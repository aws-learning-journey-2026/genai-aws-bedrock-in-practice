# Session 01: Bedrock Mental Models & GenAI Foundations

* **Event URL:** <https://www.meetup.com/dot-net-learners-house-hyderabad/events/312511436>
* **Duration:** ~30 minutes
* **Type:** Conceptual (mental models first, tooling later)
* **Deliverable:** One-page *Bedrock Mental Model* note + glossary
* **Part of:** `genai-aws-bedrock-in-practice`
* **Organization:** aws-learning-journey-2026

---

## 1. Objective

By the end of this session, you should be able to:

* Explain what **Generative AI** is in practical terms
* Describe what a **foundation model** is and why it matters
* Clearly articulate **what Amazon Bedrock is and is not**
* Place **Amazon Bedrock correctly within the AWS AI/ML ecosystem**

### Why This Matters

> **These are very common assumptions — I’ve made them myself.**

Many challenges with Generative AI on AWS begin **before any code is written**:

* Amazon Bedrock is frequently misunderstood in relation to SageMaker
* LLMs are often approached as deterministic APIs rather than probabilistic systems
* System designs may overlook token-based cost and variability in outputs

Without the right mental model, early design decisions can lead to unnecessary complexity, higher costs, or fragile systems. This session exists to establish that foundation before moving into tools and implementation.

---

## 2. Core Mental Models

### 2.1 The Minimal AI Hierarchy (For Bedrock Users)

For **using Amazon Bedrock**, you only need the following conceptual hierarchy.
This is an **orientation model**, not a training guide.

#### The AI Hierarchy (Minimal Mental Model)

```mermaid
graph LR
    A[Artificial Intelligence<br/>Systems that perceive, reason, and act] --> B[Machine Learning<br/>Learn patterns from data]
    B --> C[Neural Networks<br/>Function approximators]
    C --> D[Deep Learning<br/>Large networks, complex representations]
    D --> E[Generative AI<br/>Generate new content]
    E --> F[Foundation Models<br/>Pre-trained, reusable]
    F --> G[Amazon Bedrock<br/>Managed inference platform]
    
    style A fill:#E3F2FD,stroke:#1976D2,stroke-width:2px
    style G fill:#E8F5E9,stroke:#388E3C,stroke-width:3px
    style E fill:#FFF3E0,stroke:#F57C00,stroke-width:2px
```

**Text Hierarchy (ASCII fallback):**

```text
Artificial Intelligence
   └── Machine Learning
         └── Neural Networks
               └── Deep Learning
                     └── Generative AI
                           └── Foundation Models (via Amazon Bedrock)
```

> Everything below **Generative AI** is intentionally **abstracted away** by Amazon Bedrock.

As Bedrock users, we design **systems and workflows**, not **models or training pipelines**.

---

### 2.2 What Is a Model? (Practically Defined)

> A **model** is a mathematical function that has learned patterns from data and can use those patterns to produce outputs for new inputs.

**Key point:** Humans write code. Models learn behavior.

#### Model as a "Learned Mapping"

Think of a model as:

```text
Input  ──► Learned Mapping ──► Output
```

**Examples:**

* Text → next likely words
* Question → answer
* Image prompt → image
* Document → summary
* Text → vector (embedding)

The "mapping" is learned during training, not programmed.

#### What a Model Is NOT

Clarifying this avoids confusion later:

* ❌ Not an API
* ❌ Not a chatbot
* ❌ Not a database
* ❌ Not a rules engine
* ❌ Not deterministic logic

A model produces **probabilistic outputs**, not guaranteed results.

> **Architect-level framing:** "A model is not software logic — it's learned behavior. That's why we design guardrails around it."

---

### 2.3 Essential Concepts (Orientation Only)

These definitions are intentionally concise.
They exist to **align vocabulary**, not to teach internals.

| Concept                          | One-line Definition                                                                 |
| -------------------------------- | ----------------------------------------------------------------------------------- |
| **Model**                        | A trained function that maps inputs to outputs based on patterns learned from data  |
| **Artificial Intelligence (AI)** | The broad goal of building systems that can perceive, reason, and act intelligently |
| **Machine Learning (ML)**        | Systems that learn patterns from data instead of being explicitly programmed        |
| **Neural Networks**              | Function approximators that learn complex mappings between inputs and outputs       |
| **Deep Learning**                | Uses large neural networks to learn rich representations from massive data          |
| **Generative AI**                | Models that generate new content such as text, images, or code                      |
| **Foundation Models**            | Large, pre-trained models reused across many tasks without training from scratch    |
| **Amazon Bedrock**               | A managed AWS service for running foundation models via APIs                        |

> Clarifying **"Model"** early is critical—everything in Bedrock ultimately revolves around *using models safely and effectively*.

---

### 2.4 Understanding Tokens

Tokens are the **basic unit of text processing** in language models. Understanding tokens is essential for:

* **Cost estimation** — Bedrock pricing is token-based
* **Prompt design** — Token limits affect what you can send
* **Performance** — Token count impacts latency and throughput

#### How Tokenization Works

![Tokenizer Process](../images/S1/Tokenizer.PNG)

#### What a Tokenizer Actually Is

A tokenizer is **not just a splitter**. It is a learned encoding system that:

* Breaks text into units (tokens)
* Maps those tokens to numerical IDs
* Is tightly coupled to how the model was trained

> **Tokenizer + Model are a pair.** You cannot mix and match them.

#### Key Points

* Tokens are not always words — they can be subwords, parts of words, or even characters
* **Tokenization is model-specific, not universal** — there is no global standard for tokens
* Different models use different tokenizers, vocabularies, and encoding rules
* The same text may have different token counts across models
* Token count directly impacts cost in Bedrock

#### Why Tokens Differ Across Models

Each foundation model in Bedrock:

* Uses its **own tokenizer** (trained with the model)
* Has its **own vocabulary**
* Was trained with **different text corpora**
* May use different subword strategies (BPE, WordPiece, Unigram, etc.)

This means the same sentence can be tokenized differently by different models.

**Practical Example:**

The phrase "Hello, world!" might be tokenized as:

* `["Hello", ",", " world", "!"]` (4 tokens) in one model
* `["Hello", ",", "world", "!"]` (4 tokens) in another model
* Or even `["Hello", ",", " world", "!"]` (3 tokens) in yet another

Same text. Same meaning. **Different tokens.**

#### Architect-Level Implication

> **Token count is always model-specific.**

Therefore:

* You **cannot** estimate cost generically across models
* You **must** test token counts with the target model
* You **must** design prompts defensively
* You **must not** assume token counts are universal

This is why production systems:

* Measure tokens dynamically
* Use truncation and summarization
* Rely on RAG to control prompt size

> **Architect-level insight:** When designing systems with Bedrock, always consider token costs. Longer prompts = higher costs. Token counts vary by model, so always test with your target model. This is why prompt engineering and RAG (Retrieval-Augmented Generation) matter for production systems.

---

## 3. Terminology Clarification

### Foundation Models vs Base Models vs Language Models vs Large Language Models

These terms are often used interchangeably, but they describe **different dimensions of a model**, not different products.

Each term answers a **different question**:

* **Base Model** → *What training state is the model in?*
* **Foundation Model** → *How broadly can the model be reused?*
* **Language Model (LM)** → *What type of data does the model work with?*
* **Large Language Model (LLM)** → *How large and capable is the language model?*

Understanding these distinctions is critical to using **Amazon Bedrock correctly and confidently**.

---

### Practical Definitions

| Term                           | One-liner                                                                     | What It Describes  |
| ------------------------------ | ----------------------------------------------------------------------------- | ------------------ |
| **Base Model**                 | A raw, pre-trained model before task-specific tuning or alignment             | Training state     |
| **Foundation Model**           | A large, reusable model designed to support many downstream tasks             | Reusability        |
| **Language Model (LM)**        | A model that understands and generates human language                         | Text modality      |
| **Large Language Model (LLM)** | A large-scale language model with strong generalization and reasoning ability | Scale & capability |

---

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

---

### Architect Takeaway

When designing systems with Amazon Bedrock:

* You **consume foundation models** via a managed service
* You do **not manage base models or training pipelines**
* You may use **LLMs**, but also non-language models (embeddings, images)
* Design decisions should focus on **capabilities, cost, latency, and constraints**, not training internals

> In Bedrock, the question is not *"How is the model trained?"*
> It is *"Is this the right capability for my system design?"*

---

### Why This Matters for Bedrock

This terminology clarity prevents common mistakes such as:

* Treating all models as chat-based LLMs
* Over-engineering with frameworks before understanding capabilities
* Choosing models based on hype instead of task fit
* Confusing training responsibilities with inference responsibilities

---

## 4. Generative AI (Practically Defined)

Generative AI refers to models that **produce new content** based on learned patterns.

### Key Characteristics

* **Probabilistic** – same input may yield different outputs
* **Context-dependent** – output quality depends on prompt and context
* **Parameter-driven** – behavior is influenced by model parameters

This is fundamentally different from deterministic APIs.

---

### 4.1 Prompt Engineering (Awareness Only)

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

#### What We Will *Not* Cover Here

This session intentionally does **not** cover prompt patterns, templates, guardrails, or RAG-specific prompt design.

These are intentionally deferred to later sessions.

#### Why Prompt Engineering Matters (At 10,000 Feet)

Prompt engineering becomes critical because:

* Foundation models are **probabilistic**, not deterministic
* Longer prompts increase **token cost**
* Poor prompts amplify **hallucinations**
* Prompt design determines how well **retrieved context (RAG)** is used

This is why prompt engineering is tightly coupled with:

* Cost optimization
* RAG design
* Production stability

> We will revisit prompt engineering in depth once we understand **models, tokens, and system boundaries**.
>
> **Architect-level framing:** "Prompt engineering is not a trick — it's an architectural concern. We'll treat it seriously, but not today."

---

## 5. Foundation Models

A **foundation model** is a large, pre-trained model that can be adapted to many tasks **without training from scratch**.

### Common Tasks

* Text generation and summarization
* Question answering
* Image generation
* Embedding creation

Foundation models trade **generality** for **cost and control**.

---

## 6. What Amazon Bedrock Is

Amazon Bedrock is a **fully managed AWS service** that provides:

* API access to multiple foundation models
* Serverless inference (no infrastructure to manage)
* Enterprise-grade security and governance
* Model choice without vendor lock-in

> Bedrock is about **using models**, not training them.

---

## 7. What Amazon Bedrock Is Not

Amazon Bedrock is **not**:

* A chatbot product
* A UI-first AI tool
* A replacement for SageMaker training workflows
* A framework like LangChain
* A deep learning tutorial platform

Bedrock is an **inference platform**, not an application or training service.

---

## 8. What Is Intentionally Out of Scope

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

## 9. Where Bedrock Fits in AWS

Think of AWS AI/ML services as layers:

* **High-level APIs:** Rekognition, Comprehend (task-specific)
* **Foundation model access:** Amazon Bedrock
* **Custom ML workflows:** Amazon SageMaker

Bedrock fills the gap between **fully managed AI APIs** and **full ML engineering**.

---

## 10. Architecture Mental Model

### The “Power Grid” Analogy

Think of Amazon Bedrock as a **power grid**:

* You don’t build the power plant (AWS manages models)
* You choose how much power you draw (model + parameters)
* You pay for what you consume (tokens)
* Your system determines efficiency and reliability

Bedrock gives **capability**, not **guarantees**.

---

## 11. Applied Reasoning Example

### Scenario

A team wants to build a **document summarization feature**.

### Decision Reasoning

* Foundation models handle summarization well
* Bedrock provides managed inference and multiple model choices
* No need for custom training or infrastructure

### Conclusion

**Amazon Bedrock is the correct choice**.

### When to Use Bedrock

* Standard GenAI tasks (summarization, Q&A, generation)
* AWS-native security and governance required
* Serverless, pay-per-use model preferred

### When NOT to Use Bedrock

* Need to train custom models → SageMaker
* Hard real-time or fully deterministic requirements → traditional services or precomputed responses

---

## 12. Common Failure Modes

* Treating outputs as deterministic
* Assuming one model fits all tasks
* Ignoring token-based cost implications
* Skipping retrieval (RAG) for real systems
* Deferring cost considerations

Correct mental models prevent these failures.

---

## 13. Mini Demo

### Simple Prompt Example

This demonstration shows a basic interaction with Amazon Bedrock using a simple prompt. It illustrates the concepts we've covered: models, tokens, and probabilistic outputs.

![Simple Prompt Example](../images/S1/SimplePrompt.PNG)

**Key Observations:**

* The prompt is sent to a foundation model via Bedrock
* The model processes the input tokens and generates output tokens
* The response is probabilistic — running the same prompt may yield different outputs
* Token count affects both cost and latency

**What This Demonstrates:**

* **Model behavior** — How foundation models respond to prompts
* **Token processing** — Input and output tokens are counted
* **Probabilistic nature** — Outputs vary based on model parameters
* **Bedrock abstraction** — The complexity of model internals is hidden

> This simple example sets the foundation for understanding more complex interactions in subsequent sessions.

---

## 14. Output Artifact

### Deliverable

Create a **one-page Bedrock Mental Model note** containing:

1. What Bedrock is and is not
2. The power grid analogy
3. Key vocabulary
4. Core decision principles

---

## 15. Key Takeaways

* Generative AI is probabilistic by nature
* Foundation models are powerful but not magic
* Amazon Bedrock provides managed access, not training
* Mental models matter more than tools
* Understanding precedes optimization

---

## 16. What's Next

### Session 02 – Amazon Bedrock Platform Deep Dive (Console-First)

* Bedrock architecture
* Model catalog and selection
* Inference parameters
* Pricing and cost control
* Security and governance

---

**Session Status:** Complete ✅
