# GenAI with AWS Bedrock — In Practice

A hands-on, session-driven learning repository focused on understanding and building **Generative AI systems on AWS using Amazon Bedrock**, with emphasis on **mental models, architecture decisions, and production readiness**.

![License](https://img.shields.io/badge/License-MIT-purple)
![Status](https://img.shields.io/badge/Status-Active-success)
![Sessions](https://img.shields.io/badge/Sessions-9%20Sessions-orange)
![Format](https://img.shields.io/badge/Format-30%20Minutes-yellow)
![Built with](https://img.shields.io/badge/Built%20with-AWS%20Bedrock-brown)
![Maintainer](https://img.shields.io/badge/Maintainer-Viswanatha%20Swamy%20P%20K-blue)

This repository is part of the **aws-learning-journey-2026** organization and documents a structured, practical exploration of Generative AI on AWS — learned in public and built incrementally.

---

## 📌 Disclaimer

This is **Swamy's personal learning** repository, knowledge-sharing repository and reference workspace, not official course material or a packaged curriculum. It is **not official AWS training material** and does not represent Amazon or its affiliates.

---

## 📘 Table of Contents

* [Disclaimer](#-disclaimer)
* [Purpose of This Repository](#-purpose-of-this-repository)
* [Who This Is For](#-who-this-is-for)
* [Learning Philosophy](#-learning-philosophy--in-practice)
* [Session Roadmap](#️-session-roadmap---9-sessions)
* [Repository Structure](#-repository-structure)
* [Principles](#-principles-non-negotiables)
* [Where to Start](#-where-to-start)
* [Organization Context](#-organization-context)
* [Contributing](#-contributing)
* [About & Community](#-about--community)
* [License](#-license)

---

## 🎯 Purpose of This Repository

This repository exists to:

* Learn **Amazon Bedrock the right way** — concept first, tooling second
* Move beyond demos to **real system design thinking**
* Understand **trade-offs**: cost, latency, security, accuracy
* Capture learnings in a **session-based, reusable format**

This is **not a packaged course** or certification guide. It is a **living learning journey**, shaped by experimentation, mistakes, and architectural reasoning.

---

## 👥 Who This Is For

* **Builders** who can write basic code (any language) but want stronger GenAI system design skills on AWS
* **Architects/TPMs** who need clarity on trade-offs, governance, and readiness
* **Cloud engineers** moving into GenAI workloads
* **Learners** who prefer **understanding over memorization**

Basic familiarity with AWS concepts is helpful, but **no prior GenAI experience is required**.

---

## 🧠 Learning Philosophy — "In Practice"

"In practice" means:

* **Mental models before APIs** — Understand concepts before diving into code
* **Architecture before frameworks** — Design thinking precedes tool selection
* **Why before how** — Reasoning drives implementation
* **Production thinking** — Security, cost, observability, and failure modes are first-class

Each session is designed to fit into **~30 minutes**, making it suitable for:

* Self-study
* Live meetups
* Team learning sessions

---

## 🗂️ Session Roadmap - 9 Sessions

The learning journey progresses through **9 focused sessions**, each building on previous concepts and producing a concrete artifact.

> **📋 Complete Session Overview**: For the full session roadmap, detailed status table, progression diagram, and session locations, see [`docs/03_session-overview.md`](docs/03_session-overview.md) (single source of truth).

**Total Duration**: ~4.5 hours of focused learning (9 sessions × 30 minutes)

> Additional sessions may be added as the platform evolves.

---

## 📁 Repository Structure

For complete repository structure details, see **[`docs/03_repository-structure.md`](docs/03_repository-structure.md)** (single source of truth).

---

## 📋 Principles (Non-Negotiables)

* **Architecture-first**: Start from mental models, then APIs, then systems
* **Practice-oriented**: Each session produces an artifact (notes, diagram, checklist, or minimal code)
* **Production-aware**: Security, cost, observability, and failure modes are first-class
* **Original content**: No course-clone structure or copied marketing text

---

## 🚀 Where to Start

Begin with:

👉 **[Session 01 Overview](src/01_bedrock-mental-models/01_overview.md)**  
   *Path: `src/01_bedrock-mental-models/01_overview.md`*

Or start from the **[Session Index Dashboard](docs/sessions/README.md)** for an overview of all sessions.

Everything else builds on that foundation.

**Recommended Learning Path**:

1. **Start with Session 01** — Build your mental model of Bedrock
2. **Follow sequentially** — Each session builds on previous concepts
3. **Complete the artifacts** — Each session produces a deliverable
4. **Review Session 09** — Production readiness ties everything together

---

## 🏢 Organization Context

This repository is part of the **aws-learning-journey-2026** GitHub organization, which hosts structured learning journeys for AWS technologies.

**Organization**: [aws-learning-journey-2026](https://github.com/aws-learning-journey-2026)

### Related Repositories

This repository focuses specifically on **Generative AI with Amazon Bedrock**. Other repositories in the organization may cover:

* AWS fundamentals and services
* Cloud architecture patterns
* DevOps and infrastructure
* Other AWS learning paths

> **Note**: This repository contains educational content and minimal code examples focused on learning, not full production implementations.

---

## 🔍 What This Repository Does *Not* Aim to Do

* ❌ Replicate official AWS documentation
* ❌ Cover every Bedrock feature exhaustively
* ❌ Provide copy-paste production code
* ❌ Be a certification study guide

Instead, it focuses on **understanding how to think about GenAI systems on AWS**.

---

## 🔄 Living Repository

This repository will evolve as:

* Amazon Bedrock adds new capabilities
* GenAI best practices mature
* Real-world lessons are learned

Expect refinement, reorganization, and occasional rewrites.

---

## 🧑‍💻 Developer Setup

### Git Configuration

For consistent commit authorship, configure your global Git identity:

```bash
git config --global user.email "yourname@youremail.com"
git config --global user.name "Your Name"
```

You only need to run these commands once per machine.

### Prerequisites

* **AWS Account** with Bedrock access (may require enablement in some regions)
* **Basic AWS CLI** knowledge (helpful but not required)
* **Text editor** or IDE for markdown files
* **Git** for version control

### Local Development

1. **Clone the repository**:

   ```bash
   git clone https://github.com/aws-learning-journey-2026/genai-aws-bedrock-in-practice.git
   cd genai-aws-bedrock-in-practice
   ```

2. **Review the master plan**:

   ```bash
   # Read the master plan to understand the structure
   cat docs/02_master-plan.md
   ```

3. **Start with Session 01**:

   ```bash
   # Navigate to sessions
   cd src
   # Open the first session (when created)
   ```

---

## 🤝 Contributing

Contributions are welcome and encouraged! You may contribute in the following ways:

* **Session content** - New sessions or improvements to existing ones
* **Documentation** - Improvements to guides and explanations
* **Code examples** - Minimal, illustrative examples that add learning value
* **Diagrams** - Visual aids and architecture diagrams
* **Bug fixes** - Corrections and clarifications

Please review [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

**Quick Checklist**:

* [ ] Review [Contributing Guidelines](CONTRIBUTING.md)
* [ ] Read the [Master Plan](docs/02_master-plan.md)
* [ ] Follow the [Session Template](docs/templates/session-template.md)
* [ ] Ensure content aligns with repository principles

---

## 📞 About & Community

### [Swamy's Tech Skills Academy](https://www.linkedin.com/company/swamy-s-tech-skills-academy) & [ShyvnTech](https://www.linkedin.com/company/shyvntech)

This repository is part of the **AWS Learning Journey 2026** initiative, stewarded and supported by `Swamy's Tech Skills Academy` and `ShyvnTech`. It is focused on helping developers and architects build practical GenAI solutions on AWS through structured, architecture-first learning.

You can connect with the community to:

* Follow structured learning journeys and deep-dive content
* Participate in knowledge-sharing discussions
* Explore mentoring, workshops, and custom training opportunities

**Related Resources**:

* [Session Overview](docs/03_session-overview.md) - **Single source of truth** for session roadmap and status
* [Session Index Dashboard](docs/sessions/README.md) - Detailed session information and navigation (sessions located in `src/`)
* [Master Plan](docs/02_master-plan.md) - Complete learning roadmap
* [Repository Structure](docs/03_repository-structure.md) - Single source of truth for structure
* [Session Template](docs/templates/session-template.md) - Standard session format
* [Style Guide](docs/STYLE_GUIDE.md) - Content creation guidelines
* [Code Examples](src/README.md) - Minimal illustrative code samples
* [CHANGELOG](CHANGELOG.md) - Version history and changes

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

---

> 🧠 **genai-aws-bedrock-in-practice** — Designed and maintained by `Viswanatha Swamy P K`. Empowering builders to design production-ready GenAI systems on AWS.  
> © 2025 Swamy's Tech Skills Academy, ShyvnTech & Srivari Software Solutions
