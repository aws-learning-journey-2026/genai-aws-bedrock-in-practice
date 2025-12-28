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
**Deliverable**: Decision checklist for model selection + risk notes

> **Artifact Template**: Use [`../../templates/session02-model-selection-template.md`](../../templates/session02-model-selection-template.md) to create your checklist.

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

### Mini-Experiment: Model Comparison

**Objective**: Compare 2–3 models using the same prompt and observe differences.

#### Step 1: Prepare Your Test Prompt

Use this sample prompt (or create your own):

```text
You are a helpful assistant. Explain what Amazon Bedrock is in 2-3 sentences, focusing on what it enables for developers.
```

**Record your prompt**: Add it to your artifact template.

#### Step 2: Test Models in Bedrock Console

**Models to Test** (select 2-3):

- `anthropic.claude-v2` (Claude 2)
- `anthropic.claude-v2:1` (Claude 2.1)
- `amazon.titan-text-lite-v1` (Titan Lite)
- `amazon.titan-text-express-v1` (Titan Express)

**Where to Test**: AWS Bedrock Console → Playground → Text or Chat

#### Step 3: Vary Parameters

Test with different `temperature` values:

- **Temperature 0.0**: Deterministic, focused
- **Temperature 0.7**: Balanced (default)
- **Temperature 1.0**: More creative, varied

#### Step 4: Capture Observations

Record in your artifact:

- **Output differences**: How do responses differ?
- **Latency "feel"**: Which models respond faster?
- **Policy/safety differences**: Any content filtering differences?
- **Cost indicators**: Token counts (input + output)

#### Common Console Gotchas

**Before Starting**:

- [ ] Bedrock enabled in your region? (Check: Bedrock Console → Model access)
- [ ] Model access granted? (Some models require explicit enablement)
- [ ] IAM permissions? (Need `bedrock:InvokeModel` permission)
- [ ] Region selection? (Not all models available in all regions)

**If You Hit Issues**:

- **"Model not available"**: Check region and model access settings
- **"Access denied"**: Verify IAM permissions
- **"Quota exceeded"**: Check service quotas in AWS Console

#### Step 5: Record Results

Use the comparison table in your artifact template to record:

- Model IDs tested
- Latency observations
- Quality assessment
- Cost estimates (token counts)
- Any notable differences

---

## 4. Output Artifact + Recap (2–5 minutes)

### Deliverable

**Artifact**: Model Selection Checklist + Risk Notes

**Location**: Use template at [`../../templates/session02-model-selection-template.md`](../../templates/session02-model-selection-template.md)

**What to Include**:

- ✅ Use case and success criteria
- ✅ Candidate models and rationale
- ✅ Constraints (region, latency, budget, safety)
- ✅ Test prompt + parameter defaults
- ✅ Test results comparison table
- ✅ Risks (hallucination, cost spikes, instability) + mitigations
- ✅ Final model selection with rationale

**Acceptance Criteria**:

- [ ] Checklist is complete (all sections filled)
- [ ] At least 2 models compared
- [ ] Test results recorded
- [ ] Risks identified with mitigations
- [ ] Model selection justified

### Next Steps

Continue to Session 03 (planned): model exploration and prompt behavior.

---

**Session Status**: Draft
