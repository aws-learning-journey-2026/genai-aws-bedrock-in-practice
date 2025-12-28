---
learning_level: "Beginner"
prerequisites:
  - "01_overview.md"
estimated_time: "10 minutes"
learning_objectives:
  - "Reason about when Bedrock is the right choice (and when it isn't)"
  - "Identify common failure modes when treating LLMs like deterministic APIs"
  - "Produce the session artifact: a one-page Bedrock mental model note"
related_topics:
  prerequisites:
    - "01_overview.md"
  builds_upon:
    - "04_terminology-and-scope.md"
  enables: []
  cross_refs: []
---

# Session 01 (Module): Applied Reasoning + Output Artifact

## Applied Reasoning Example

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

## Common Failure Modes

* Treating outputs as deterministic
* Assuming one model fits all tasks
* Ignoring token-based cost implications
* Skipping retrieval (RAG) for real systems
* Deferring cost considerations

Correct mental models prevent these failures.

---

## Mini Demo

This demonstration shows a basic interaction with Amazon Bedrock using a simple prompt. It illustrates the concepts we've covered: models, tokens, and probabilistic outputs.

![Simple Prompt Example](../../images/S1/SimplePrompt.PNG)

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

---

## Output Artifact

**Artifact**: One-Page Bedrock Mental Model Note + Glossary

**Template**: [`../../templates/session01-mental-model-template.md`](../../templates/session01-mental-model-template.md)

**What to Include**:

1. What Bedrock is and is not
2. The power grid analogy
3. Key vocabulary (model, prompt, tokens, inference, foundation model)
4. Core decision principles
5. When to use Bedrock (and when not to)

**Acceptance Criteria**:

* [ ] All sections completed
* [ ] Definitions in your own words (not copied)
* [ ] Power grid analogy explained
* [ ] Decision principles clearly stated

---

## Key Takeaways

* Generative AI is probabilistic by nature
* Foundation models are powerful but not magic
* Amazon Bedrock provides managed access, not training
* Mental models matter more than tools
* Understanding precedes optimization

---

## What's Next

### Session 02 – Amazon Bedrock Platform Deep Dive (Console-First)

* Bedrock console mental model
* Model catalog and selection
* Inference parameters
* Pricing and cost control
* Security and governance
