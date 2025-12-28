# Changelog

All notable changes to this repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Session overview as single source of truth (`docs/04_session-overview.md`)
- Session index dashboard (`docs/sessions/README.md`)
- Enhanced session template in `docs/templates/`
- Facilitator notes template (`docs/templates/facilitator-notes-template.md`)
- Style guide (`docs/STYLE_GUIDE.md`)
- CI workflow for markdown quality checks (`.github/workflows/markdown-quality.yml`)
- Structure validation checklist in CONTRIBUTING.md
- Review action items tracking (`docs/REVIEW_ACTION_ITEMS.md`)
- CHANGELOG.md
- Minimal Python code example (`src/python/bedrock_hello_inference.py`)

### Changed
- Renamed Session 01 files to new naming convention:
  - `01_bedrock-mental-models.md` → `01_overview.md`
  - `core-mental-models.md` → `02_core-mental-models.md`
  - `tokens.md` → `03_tokens.md`
  - `terminology-and-scope.md` → `04_terminology-and-scope.md`
  - `applied-reasoning-and-artifact.md` → `05_applied-reasoning-and-artifact.md`
- Updated all file references across documentation
- Made "Where to Start" link more resilient with multiple entry points
- Enhanced CONTRIBUTING.md with structure validation requirements

### Fixed
- Markdown linting issues in Session 01 files

### Moved
- `COMPREHENSIVE_REVIEW_REPORT.md` → `docs/reviews/2025-01_workspace-review.md` (archived as historical)

---

## [0.1.0] - 2025-01-XX

### Added
- Initial repository structure
- README.md with comprehensive documentation
- Master plan (`docs/02_master-plan.md`)
- Repository structure documentation (`docs/03_repository-structure.md`)
- Session template (`docs/01_session-template.md`)
- Code of Conduct
- Contributing guidelines
- Security policy
- Comprehensive .cursor rules for AI assistance

### Session Content
- **Session 01**: Bedrock Mental Models & GenAI Foundations (Complete)
  - Core mental models module
  - Tokens module
  - Terminology & scope module
  - Applied reasoning & artifact module

- **Session 02**: Bedrock Platform Deep Dive (Draft)
  - Initial structure created

### Documentation
- Meetup materials for Sessions 01 and 02
- Backup/archived content
- Image assets for Session 01

### Infrastructure
- Markdown linting configuration
- Link checking configuration (lychee)
- Git ignore rules
- MIT License

---

## [0.0.1] - 2024-12-XX

### Added
- Initial repository setup
- Basic structure planning

---

## Types of Changes

- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** for vulnerability fixes

---

**Note**: This changelog follows [Keep a Changelog](https://keepachangelog.com/) principles. All dates are in YYYY-MM-DD format.

