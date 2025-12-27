# Security Policy

## Supported Versions

We actively support the following versions of this repository:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| Previous | :white_check_mark: |

## Reporting a Vulnerability

We take the security of this repository seriously. If you discover a security vulnerability, please report it responsibly.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of the following methods:

1. **Email**: Contact the repository maintainers directly
2. **Private Security Advisory**: Use GitHub's [Private Vulnerability Reporting](https://github.com/aws-learning-journey-2026/genai-aws-bedrock-in-practice/security/advisories/new) feature

### What to Include

When reporting a security vulnerability, please include:

- **Description**: A clear description of the vulnerability
- **Impact**: The potential impact if exploited
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Suggested Fix**: If you have ideas for how to fix it (optional but appreciated)

### Response Timeline

- **Initial Response**: We will acknowledge your report within 48 hours
- **Status Update**: We will provide a status update within 7 days
- **Resolution**: We will work to resolve the issue as quickly as possible

### Security Best Practices for Contributors

When contributing to this repository:

#### Code Examples
- ✅ **Never include real API keys, secrets, or credentials** in code examples
- ✅ **Use environment variables** or placeholder values for sensitive data
- ✅ **Include security notes** in examples that handle authentication
- ✅ **Document security considerations** in session content

#### Documentation
- ✅ **Sanitize any logs or outputs** shown in documentation
- ✅ **Use placeholder values** for account IDs, region names, etc.
- ✅ **Include security warnings** where appropriate

#### AWS-Specific Security
- ✅ **Follow AWS security best practices** in examples
- ✅ **Document IAM least privilege principles**
- ✅ **Include cost considerations** in examples
- ✅ **Mention security implications** of architectural decisions

### Security Considerations in Content

This repository focuses on GenAI system design on AWS. Security considerations should be included in:

- **Session 05**: GenAI Backend Architecture (IAM, VPC, security groups)
- **Session 09**: Production Readiness (security, cost, observability)
- **All sessions**: When discussing production deployment considerations

### Known Security Considerations

When working with Amazon Bedrock and GenAI systems:

1. **IAM Permissions**: Always follow least privilege principles
2. **Data Privacy**: Be aware of data sent to Bedrock models
3. **Network Security**: Consider VPC endpoints for private access
4. **Cost Controls**: Implement usage limits and monitoring
5. **Input Validation**: Validate and sanitize inputs to models
6. **Output Filtering**: Consider content filtering for model outputs

### Updates and Patches

Security updates will be:
- Documented in release notes
- Applied to supported versions
- Communicated to users when necessary

---

**Thank you for helping keep this repository secure!**

