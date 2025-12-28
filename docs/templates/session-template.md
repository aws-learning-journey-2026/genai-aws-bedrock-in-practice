# Session Template

This template follows the **new naming convention** and **30-minute session format** for creating consistent, high-quality learning sessions.

## Naming Convention

**Session Folder**: `NN_session-topic-kebab/`  
**Files Inside**:
- `01_overview.md` - Session overview and navigation
- `02_module-name.md` - First module
- `03_module-name.md` - Second module
- `04_module-name.md` - Third module
- `05_module-name.md` - Final module (if needed)

**Rules**:
- ✅ Use `01_`, `02_`, etc. (never `00_`)
- ✅ Use kebab-case for multi-word names
- ✅ Keep module names semantic and descriptive
- ✅ Overview file is always `01_overview.md`

---

## 01_overview.md Template

```markdown
---
learning_level: "Beginner"  # Beginner | Intermediate | Advanced
prerequisites: []
estimated_time: "30 minutes"
learning_objectives:
  - "Specific, measurable outcome 1"
  - "Specific, measurable outcome 2"
  - "Specific, measurable outcome 3"
related_topics:
  prerequisites: []
  builds_upon: []
  enables:
    - "../NN_next-session/01_overview.md"
  cross_refs: []
---

# Session NN: [Session Title]

This session is split into focused modules to stay within the 30-minute format and keep each concept boundary clean.

* **Event URL:** [Optional meetup link]
* **Duration:** ~30 minutes (combined)
* **Type:** [Conceptual / Hands-on / Mixed]
* **Deliverable:** [Artifact type: notes, diagram, checklist, or minimal code]

---

## Modules

1. [Module 1 Title](02_module-1-name.md)
2. [Module 2 Title](03_module-2-name.md)
3. [Module 3 Title](04_module-3-name.md)
4. [Module 4 Title](05_module-4-name.md) [if needed]

---

## Output Artifact

After completing the modules, you should have [description of artifact]:

* [Key point 1]
* [Key point 2]
* [Key point 3]
```

---

## Module File Template (02_module-name.md, etc.)

```markdown
---
learning_level: "Beginner"
prerequisites:
  - "01_overview.md"
estimated_time: "10-15 minutes"
learning_objectives:
  - "Specific learning objective for this module"
related_topics:
  prerequisites:
    - "01_overview.md"
  builds_upon:
    - "02_previous-module.md"  # if applicable
  enables: []
  cross_refs: []
---

# Session NN (Module): [Module Title]

## [Main Concept]

[Core content here - architecture-first thinking]

### Key Points

* Point 1
* Point 2
* Point 3

### Architecture Considerations

[How this fits into system design thinking]

---

## [Sub-concept if needed]

[Additional content]

---

## Architect-Level Insight

> [Key takeaway for system designers]

---

## What's Next

Continue to [next module](03_next-module.md) or return to [overview](01_overview.md).
```

---

## Content Guidelines

### Mental Models Section

- Start with **why** before **how**
- Use analogies when helpful (e.g., "Power Grid" for Bedrock)
- Emphasize **trade-offs** and **constraints**
- Include **architect-level insights**

### Code Examples

- Keep examples **minimal and illustrative**
- Focus on **concepts**, not complete implementations
- Include **error handling** considerations
- Reference full code in `src/` if applicable

### Diagrams

- Use **Mermaid-first** with ASCII fallback
- Keep diagrams **simple and focused**
- Never embed copyrighted figures

### Production Considerations

Every session should include:
- **Security** implications
- **Cost** considerations
- **Observability** needs
- **Failure modes** and mitigations

---

## Quality Checklist

Before marking a session as complete:

- [ ] All modules follow naming convention (`01_overview.md`, `02_...`, etc.)
- [ ] YAML frontmatter is complete and correct
- [ ] All file references point to existing files
- [ ] Learning objectives are specific and measurable
- [ ] Content is within 150 lines per file (split if needed)
- [ ] Diagrams use Mermaid with ASCII fallback
- [ ] Production considerations are included
- [ ] Deliverable is clearly defined
- [ ] Prerequisites and enables are correctly linked

---

## Example: Session 01 Structure

```
01_bedrock-mental-models/
├── 01_overview.md
├── 02_core-mental-models.md
├── 03_tokens.md
├── 04_terminology-and-scope.md
└── 05_applied-reasoning-and-artifact.md
```

This structure:
- ✅ Uses consistent numbering
- ✅ Has semantic module names
- ✅ Keeps overview separate
- ✅ Scales to any number of modules

---

**Related Resources**:
- [Session Overview](../03_session-overview.md) - **Single source of truth** for session roadmap
- [Session Index Dashboard](../sessions/README.md)
- [Master Plan](../02_master-plan.md)
- [Repository Structure](../01_repository-structure.md)

