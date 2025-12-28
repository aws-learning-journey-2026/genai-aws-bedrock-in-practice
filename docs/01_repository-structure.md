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
├── .github/                               # GitHub configuration
│   ├── copilot-instructions.md            # Copilot instruction file
│   ├── ISSUE_TEMPLATE/                    # Issue templates
│   ├── prompts/                           # Reusable prompt templates
│   └── PULL_REQUEST_TEMPLATE.md           # PR template
├── docs/                                  # Documentation hub
│   ├── templates/                           # Templates for sessions and artifacts
│   ├── 03_master-plan.md                  # Master plan and roadmap
│   ├── 02_repository-structure.md         # This file - single source of truth
│   ├── images/                            # Diagrams and visual assets
│   │   └── S1/                             # Session 01 images
│   ├── meetup/                             # Meetup index and materials
│   │   ├── .gitkeep
│   │   ├── 01_meetup-bedrock-mental-models.md
│   │   ├── 02_meetup-bedrock-platform-deep-dive.md
│   │   └── sessions.md                    # Index of meetup sessions
│   └── sessions/                           # Active session content (30-min format)
│       ├── .gitkeep
│       ├── 01_bedrock-mental-models/
│       │   ├── 01_overview.md
│       │   ├── 02_core-mental-models.md
│       │   ├── 03_tokens.md
│       │   ├── 04_terminology-and-scope.md
│       │   └── 05_applied-reasoning-and-artifact.md
│       └── 02_bedrock-platform-deep-dive/
│           └── 02_bedrock-platform-deep-dive.md
│       
├── src/                                    # Minimal runnable labs/examples
├── source-material/                        # Staging area for imported content (git-ignored)
├── .gitignore                             # Git ignore rules
├── .markdownlint-cli2.yaml                 # Markdownlint configuration
├── .markdownlint.json                      # Markdownlint configuration
├── .markdownlintignore                     # Markdownlint ignore rules
├── CODE_OF_CONDUCT.md                     # Code of conduct
├── CONTRIBUTING.md                        # Contribution guidelines
├── LICENSE                                 # MIT License
├── lychee.toml                             # Link checker configuration
├── README.md                               # Main repository documentation
├── SECURITY.md                            # Security policy
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

- **`templates/session-template.md`**: Standard 30-minute session template (modular format)
- **`03_master-plan.md`**: Complete learning roadmap, session plans, and repository principles
- **`04_session-overview.md`**: **Single source of truth** for session roadmap and status
- **`02_repository-structure.md`**: This file - single source of truth for repository structure
- **`04_session-overview.md`**: **Single source of truth** for session roadmap and status
- **`sessions/`**: Active session content files following the 30-minute format
- **`meetup/`**: Materials for live meetup delivery (slides, notes, etc.)
- **`images/`**: Visual assets, diagrams, and architecture illustrations

---

### `docs/sessions/`

**Purpose**: Session-based learning content  
**Structure**: Each session lives in its own folder `NN_session-name/` and contains a primary markdown file `NN_session-name.md`.

**File Types**:

1. **Learning Sessions**: `docs/sessions/NN_{session-name}/01_overview.md` (e.g., `docs/sessions/01_bedrock-mental-models/01_overview.md`)
   - Self-study content following the session template
   - Includes: Objective, Core Concepts, Hands-on, Artifact

### `docs/meetup/`

**Purpose**: Meetup delivery content and index  
**File Types**:

1. **Meetup Sessions**: `NN_meetup-{session-name}.md` (e.g., `01_meetup-bedrock-mental-models.md`)
   - Meetup delivery content with organization, date, and agenda
   - Based on learning sessions but includes meetup-specific details
   - Includes: Organization, Date, Duration, Type, Deliverable, Why This Session, Agenda

**Session Format** (30 minutes each):

1. Objective (1–2 minutes)
2. Core concepts (10–12 minutes)
3. Hands-on / applied reasoning (12–15 minutes)
4. Output artifact + recap (2–5 minutes)

**Template**: `docs/templates/session-template.md` provides the standard structure for all learning sessions

**Current Sessions**:

- `docs/sessions/01_bedrock-mental-models/01_overview.md` - Bedrock Mental Models & GenAI Foundations (overview)
- `docs/sessions/02_bedrock-platform-deep-dive/02_bedrock-platform-deep-dive.md` - Bedrock Platform Deep Dive (Console-First)

**Meetup Sessions**:

- `docs/meetup/01_meetup-bedrock-mental-models.md` - Meetup Session 01 (Dot Net Learners House)
- `docs/meetup/02_meetup-bedrock-platform-deep-dive.md` - Meetup Session 02 (Dot Net Learners House)

**Future Sessions** (planned):

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

- Master documents: `NN_descriptive-name.md` (e.g., `03_master-plan.md`)
- Session files: `01_overview.md` (overview), `02_module-name.md`, `03_module-name.md`, etc. (e.g., `01_overview.md`, `02_core-mental-models.md`)
- Session template: `templates/session-template.md` (modular format)

### Code Files

- Follow language-specific conventions
- Keep examples minimal and illustrative

---

## 🔄 Content Organization Principles

1. **Session-based**: All learning content organized as 30-minute sessions
2. **Single Source of Truth**: This file (`03_repository-structure.md`) is the authoritative reference
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

- **Master Plan**: `docs/03_master-plan.md` - Complete learning roadmap
- **Session Overview**: `docs/04_session-overview.md` - Single source of truth for session roadmap
- **Session Template**: `docs/templates/session-template.md` - Standard session format (modular)
- **Repository README**: `README.md` - Main entry point (references this file)

---

**Note**: This file serves as the **single source of truth** for repository structure. All other documentation should reference this file rather than duplicating structure information.

