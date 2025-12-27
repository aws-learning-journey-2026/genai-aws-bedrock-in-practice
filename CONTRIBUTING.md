# Contributing to genai-aws-bedrock-in-practice

Thank you for your interest in contributing to **genai-aws-bedrock-in-practice**! This repository is a practical, architecture-first learning resource for building Generative AI solutions on AWS using Amazon Bedrock.

## 🎯 Repository Purpose

This repository focuses on:
- **Architecture-first learning**: Mental models → APIs → systems
- **Session-based format**: 30-minute timeboxed sessions
- **Production-aware content**: Security, cost, observability, and failure modes
- **Original content**: No course-clone structure or copied marketing text

## 📋 How to Contribute

### Types of Contributions

We welcome contributions in the following areas:

1. **Session Content** (`docs/sessions/`)
   - New session write-ups following the 30-minute format
   - Improvements to existing sessions
   - Session artifacts (diagrams, checklists, notes)

2. **Documentation** (`docs/`)
   - Improvements to master plan
   - Repository structure updates
   - Meetup materials

3. **Code Examples** (`src/`)
   - Minimal, illustrative code examples
   - Small runnable labs that add learning value

4. **Documentation Improvements**
   - Fixing typos or clarifying explanations
   - Improving diagrams or visualizations
   - Updating outdated information

## 🚀 Getting Started

### Before You Begin

1. **Read the Master Plan**: Review [`docs/01_master-plan.md`](docs/01_master-plan.md) to understand the repository's structure and principles
2. **Review Repository Structure**: Check [`docs/03_repository-structure.md`](docs/03_repository-structure.md) for the single source of truth on organization
3. **Understand Session Format**: Review [`docs/sessions/_session-template.md`](docs/sessions/_session-template.md) for the standard session structure

### Contribution Workflow

1. **Fork the repository** and create a new branch for your contribution
2. **Make your changes** following our guidelines below
3. **Test your changes** (run linters, check markdown rendering)
4. **Submit a pull request** with a clear description

## 📝 Content Guidelines

### Session Content Standards

When creating or updating session content:

- ✅ **Follow the 30-minute format**: Objective → Core Concepts → Hands-on → Artifact
- ✅ **Use the session template**: Start from `docs/sessions/_session-template.md`
- ✅ **Architecture-first approach**: Emphasize mental models before APIs
- ✅ **Production-aware**: Include security, cost, and observability considerations
- ✅ **Original content**: Transform, don't copy from sources
- ✅ **Clear deliverables**: Each session should produce a specific artifact

### Code Examples

- ✅ **Minimal and illustrative**: Focus on teaching concepts, not complete implementations
- ✅ **Well-commented**: Explain what the code demonstrates
- ✅ **Language-agnostic when possible**: Focus on concepts over syntax
- ✅ **Production considerations**: Include error handling, security, and cost notes

### Documentation Standards

- ✅ **Markdown formatting**: Follow markdownlint rules
- ✅ **Clear structure**: Use headings, lists, and code blocks appropriately
- ✅ **Diagrams**: Use Mermaid-first with ASCII fallback
- ✅ **Links**: Ensure all links work and point to existing files

## ✅ Quality Checklist

Before submitting your contribution, ensure:

### Content Quality
- [ ] Content follows the repository's principles (architecture-first, production-aware)
- [ ] Session format is correct (30-minute structure)
- [ ] Content is original and transformative (not copied)
- [ ] Learning objectives are clear and measurable
- [ ] Examples are relevant and practical

### Technical Quality
- [ ] Markdown linting passes (no errors)
- [ ] All file references point to existing files
- [ ] Code examples are minimal and illustrative
- [ ] Diagrams render correctly (Mermaid + ASCII fallback)
- [ ] No placeholder text or TODOs remain

### Documentation
- [ ] README updated if structure changed
- [ ] Repository structure document updated if needed
- [ ] Related documentation cross-referenced

## 🔍 Review Process

1. **Automated Checks**: Your PR will be checked for markdown linting and basic validation
2. **Content Review**: Maintainers will review for alignment with repository principles
3. **Feedback**: We may request changes to better align with the repository's purpose
4. **Approval**: Once approved, your contribution will be merged

## 📚 Resources

- **Master Plan**: [`docs/01_master-plan.md`](docs/01_master-plan.md)
- **Repository Structure**: [`docs/03_repository-structure.md`](docs/03_repository-structure.md)
- **Session Template**: [`docs/sessions/_session-template.md`](docs/sessions/_session-template.md)
- **Educational Content Rules**: [`.cursor/rules/01_educational-content-rules.mdc`](.cursor/rules/01_educational-content-rules.mdc)
- **File Naming Conventions**: [`.cursor/rules/07_file-naming-conventions.mdc`](.cursor/rules/07_file-naming-conventions.mdc)

## 💬 Getting Help

- **Open an issue** for questions or discussions
- **Check existing issues** to see if your question has been answered
- **Review the master plan** for repository structure and principles

## 🙏 Thank You

Your contributions help make this repository a valuable learning resource for the GenAI community. We appreciate your time and effort!

---

**Remember**: This repository focuses on **understanding how to think about GenAI systems on AWS**, not on providing complete production code. Keep contributions focused on learning and architectural reasoning.

