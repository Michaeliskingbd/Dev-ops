# Learner and Contributor Guide

Welcome to the 180-Day DevOps Engineering Mentorship Programme. This document defines the engineering standards, pull request workflows, and repository contribution rules.

---

## 1. Branching Strategy

Learners must never push directly to `main`. All work must be conducted in dedicated weekly branches:

- **Branch Naming Standard:** `submissions/week-XX` (e.g., `submissions/week-01`, `submissions/week-14`)
- **Fixes/Corrections:** `corrections/week-XX-issue-title`
- **Mini-Projects:** `projects/mini-project-X`
- **Capstone Project:** `projects/capstone-infrastructure`

```bash
# Example: Starting Week 03
git checkout main
git pull origin main
git checkout -b submissions/week-03
```

---

## 2. Directory Submission Structure

All weekly deliverables must be placed strictly within the designated subfolder:

```text
submissions/
└── week-XX/
    ├── assignment-01/
    │   ├── solution.sh (or .py / .tf / .yaml)
    │   └── evidence.md (commands executed and terminal output)
    ├── assignment-02/
    ├── assignment-03/
    ├── assignment-04/
    ├── assignment-05/
    ├── challenge/
    │   └── challenge-solution.md
    └── screenshots/ (optional terminal or console screenshots)
```

And weekly reports must be placed in:
```text
weekly-reports/
└── week-XX-report.md
```

---

## 3. Pull Request Submission Protocol

When you complete a week's assignments:

1. **Run Local Validation:**
   ```bash
   python scripts/validate_submission.py --week XX
   ```
   Ensure all checks pass with zero fatal errors.

2. **Commit with Meaningful Conventional Commits:**
   ```bash
   git add submissions/week-XX/ weekly-reports/week-XX-report.md
   git commit -m "feat(week-XX): complete assignments 01-05 and weekly report"
   ```

3. **Push to Remote:**
   ```bash
   git push -u origin submissions/week-XX
   ```

4. **Open a Pull Request:**
   - Target branch: `main`
   - Title: `[Submission] Week XX: <Topic Name> - <Learner Name>`
   - Fill out every section of the [PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md).
   - Link any corresponding GitHub Issue (`Closes #123`).

---

## 4. Code Quality & Formatting Standards

- **Bash Scripts:**
  - Must include `#!/usr/bin/env bash` shebang.
  - Must set strict mode: `set -euo pipefail`.
  - Must pass `shellcheck` without warnings.
- **Python Scripts:**
  - Must target Python 3.12+.
  - Must follow PEP 8 standards.
  - Must include docstrings and type hints for functions.
- **Terraform:**
  - Must be formatted using `terraform fmt -check`.
  - Must validate clean using `terraform validate`.
  - Must never contain hardcoded AWS access keys or secrets.
- **Dockerfiles:**
  - Must pass `hadolint` checks.
  - Must use multi-stage builds and non-root users for production images.
- **Kubernetes Manifests:**
  - Must specify explicit resource requests and limits.
  - Must include liveness and readiness health probes.

---

## 5. Review & Merging Process

1. **Automated CI Validation:** GitHub Actions runs submission validators and markdown checks.
2. **Mentor Review:** A mentor inspects code quality, architecture choices, and documentation depth.
3. **Live Demonstration:** The learner may be requested to explain or demonstrate the implementation.
4. **Revisions:** If changes are requested, commit additional fixes to the same branch.
5. **Approval & Merge:** Once passing (score >= 80), the mentor merges the PR into `main`.
