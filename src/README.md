# Code Examples — genai-aws-bedrock-in-practice

This directory contains **minimal, illustrative code examples** that demonstrate concepts taught in the learning sessions.

## Purpose

These examples are:
- ✅ **Minimal and focused** — Show only what's needed to teach concepts
- ✅ **Illustrative** — Demonstrate principles, not complete implementations
- ✅ **Teaching-oriented** — Designed for learning, not production use

## Principles

1. **Minimal Code**: Examples should be small and focused on a single concept
2. **Well-Commented**: Code should explain what it demonstrates
3. **Production-Aware**: Include notes about error handling, security, and cost
4. **Language-Agnostic When Possible**: Focus on concepts over syntax

## Structure

```
src/
├── README.md (this file)
├── python/
│   ├── bedrock_hello_inference.py
│   └── bedrock_error_handling.py
├── javascript/
│   └── bedrock_hello_inference.js
└── typescript/
    └── bedrock_hello_inference.ts
```

## Example: Hello Inference

A minimal example showing how to invoke a Bedrock model:

```python
# Minimal example - demonstrates basic Bedrock invocation
# This is for learning, not production use

import boto3
import json

# Initialize client
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

# Prepare request
model_id = 'anthropic.claude-v2'
prompt = 'Hello, Bedrock!'

body = json.dumps({
    'prompt': prompt,
    'max_tokens_to_sample': 100
})

# Invoke model
response = bedrock.invoke_model(
    modelId=model_id,
    body=body
)

# Parse response
result = json.loads(response['body'].read())
print(result['completion'])

# Note: In production, add:
# - Error handling (try/except)
# - Input validation
# - Cost monitoring
# - Security considerations (IAM, VPC)
```

## Guidelines

### What to Include

- ✅ Minimal code that demonstrates a concept
- ✅ Comments explaining the concept
- ✅ Production considerations as comments
- ✅ Links back to relevant session content

### What NOT to Include

- ❌ Complete, production-ready applications
- ❌ Full test suites
- ❌ Complex deployment configurations
- ❌ Production secrets or credentials

## Linking from Sessions

When a session references code:

```markdown
## Example Code

See minimal example: [`bedrock_hello_inference.py`](../../src/python/bedrock_hello_inference.py)

This example demonstrates:
- Basic Bedrock client initialization
- Model invocation
- Response parsing
```

## Contributing

When adding code examples:

1. Keep examples minimal and focused
2. Add clear comments explaining concepts
3. Include production considerations as comments
4. Link from relevant session content
5. Follow language-specific conventions
6. Test examples before committing

## Status

Currently, this directory is empty. Examples will be added as sessions are developed.

**Planned Examples**:
- Basic Bedrock invocation (Session 04)
- Error handling patterns (Session 04)
- Lambda integration (Session 05)
- Embedding generation (Session 06)
- RAG implementation (Session 07)

---

**Related Resources**:
- [Session Index Dashboard](../docs/sessions/README.md)
- [Style Guide](../docs/STYLE_GUIDE.md)
- [Contributing Guidelines](../CONTRIBUTING.md)

