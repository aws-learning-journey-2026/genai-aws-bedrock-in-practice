# Repository Structure

**Version**: 1.0  
**Last Updated**: December 27, 2025  
**Status**: Single Source of Truth

---

## 📁 Directory Structure

```text
genai-aws-bedrock-in-practice/
├── .copilot/                              # Copilot configuration
│   └── settings.json
├── .cursor/                               # Cursor AI configuration
│   └── rules/                             # Project rules
│       ├── 01_educational-content-rules.mdc
│       ├── 02_repository-structure.mdc
│       ├── 03_quality-assurance.mdc
│       ├── 04_markdown-standards.mdc
│       ├── 05_primary-directives.mdc
│       ├── 06_cross-domain-integration.mdc
│       ├── 07_file-naming-conventions.mdc
│       └── README.md
├── docs/                                  # Documentation hub
│   ├── 01_master-plan.md                  # Master plan and roadmap
│   ├── 02_repository-structure.md         # This file - single source of truth
│   ├── sessions/                           # Session content (30-min format)
│   │   ├── _session-template.md           # Session template for consistency
│   │   ├── 01_bedrock-mental-models.md
│   │   ├── 02_bedrock-platform-deep-dive.md
│   │   └── ... (additional sessions as created)
│   ├── meetup/                             # Meetup materials and slides
│   └── images/                            # Diagrams and visual assets
├── src/                                    # Minimal runnable labs/examples
├── source-material/                        # Staging area for imported content (git-ignored)
├── LICENSE                                 # MIT License
├── README.md                               # Main repository documentation
├── .gitignore                             # Git ignore rules
├── .markdownlint.json                      # Markdown linting configuration
└── .markdownlint-cli2.yaml                 # Markdown lint CLI configuration
```

---

## 📂 Directory Descriptions

### `.copilot/`
**Purpose**: GitHub Copilot configuration  
**Contents**: Settings for Copilot behavior and language preferences

### `.cursor/`
**Purpose**: Cursor AI configuration and project rules  
**Contents**: Modular rule files (`.mdc` format) that guide AI assistance behavior

### `docs/`
**Purpose**: Primary documentation hub  
**Contents**:
- **`01_master-plan.md`**: Complete learning roadmap, session plans, and repository principles
- **`02_repository-structure.md`**: This file - single source of truth for repository structure
- **`sessions/`**: Individual session content files following the 30-minute format
- **`meetup/`**: Materials for live meetup delivery (slides, notes, etc.)
- **`images/`**: Visual assets, diagrams, and architecture illustrations

### `docs/sessions/`
**Purpose**: Session-based learning content  
**Structure**: Each session is a single markdown file following the naming convention `NN_session-name.md`

**Session Format** (30 minutes each):
1. Objective (1–2 minutes)
2. Core concepts (10–12 minutes)
3. Hands-on / applied reasoning (12–15 minutes)
4. Output artifact + recap (2–5 minutes)

**Template**: `_session-template.md` provides the standard structure for all sessions

**Current Sessions** (planned):
- `01_bedrock-mental-models.md` - Bedrock Mental Models & GenAI Foundations
- `02_bedrock-platform-deep-dive.md` - Bedrock Platform Deep Dive (Console-First)
- `03_model-exploration-prompt-behavior.md` - Model Exploration & Prompt Behavior
- `04_bedrock-apis-sdks.md` - Bedrock APIs & SDKs
- `05_genai-backend-architecture.md` - Designing a Minimal GenAI Backend on AWS
- `06_embeddings-vector-thinking.md` - Embeddings & Vector Thinking
- `07_rag-with-bedrock.md` - Retrieval-Augmented Generation (RAG) with Bedrock
- `08_advanced-capabilities.md` - Advanced Capabilities (Knowledge Bases / Agents)
- `09_production-readiness.md` - Production Readiness: Security, Cost, Observability

### `src/`
**Purpose**: Minimal runnable labs and examples  
**Contents**: Small code examples that add learning value (not full implementations)  
**Status**: Currently empty, reserved for future minimal examples

### `source-material/`
**Purpose**: Staging area for imported/raw content  
**Status**: Git-ignored, used for temporary storage before content migration  
**Workflow**: Content placed here → reviewed → migrated to appropriate `docs/sessions/` files

---

## 📋 File Naming Conventions

### Documentation Files
- Master documents: `NN_descriptive-name.md` (e.g., `01_master-plan.md`)
- Session files: `NN_session-name.md` (e.g., `01_bedrock-mental-models.md`)
- Template files: `_template-name.md` (leading underscore indicates template)

### Code Files
- Follow language-specific conventions
- Keep examples minimal and illustrative

---

## 🔄 Content Organization Principles

1. **Session-based**: All learning content organized as 30-minute sessions
2. **Single Source of Truth**: This file (`02_repository-structure.md`) is the authoritative reference
3. **Minimal Code**: Code examples should be minimal, illustrative, and teaching-focused
4. **Production-aware**: Even small examples should consider security, cost, and observability
5. **Architecture-first**: Content emphasizes mental models before APIs

---

## 📝 Maintenance

**When to Update This File**:
- New directories are added
- Directory purposes change
- File naming conventions evolve
- Repository structure is reorganized

**After Updating**:
- Update `README.md` if it references structure details
- Update `.cursor/rules/02_repository-structure.mdc` if needed
- Ensure all references point to this file as the single source of truth

---

## 🔗 Related Documentation

- **Master Plan**: `docs/01_master-plan.md` - Complete learning roadmap
- **Session Template**: `docs/sessions/_session-template.md` - Standard session format
- **Repository README**: `README.md` - Main entry point (references this file)

---

**Note**: This file serves as the **single source of truth** for repository structure. All other documentation should reference this file rather than duplicating structure information.

