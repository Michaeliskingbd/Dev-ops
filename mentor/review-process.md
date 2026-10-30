# Pull Request Review & Grading Protocol

This document outlines the standard operating procedure for reviewing learner submissions on GitHub.

---

## 1. Automated Checks (Must Pass First)
Before inspecting code, verify that GitHub Actions CI checks have completed:
- `validate-submissions`: Confirms required files, reports, and absence of plain-text credentials.
- `validate-markdown`: Confirms documentation structure.

*If CI checks fail, reject the PR immediately with instructions to review CI logs.*

---

## 2. Code Review Checklist

### Bash & Automation
- [ ] Has strict mode enabled (`set -euo pipefail`).
- [ ] Variables quoted appropriately (`"$VAR"`).
- [ ] Clean exit codes on error paths (`exit 1`).
- [ ] No hardcoded passwords or API keys.

### Docker & Containers
- [ ] Base images pinned to specific version tags (not `:latest`).
- [ ] Runs as a non-root user (`USER nonroot` or `USER 1001`).
- [ ] Multi-stage builds used to separate build tooling from runtime artifact.
- [ ] Clean `.dockerignore` file present.

### Terraform & Cloud
- [ ] Formatted with `terraform fmt`.
- [ ] Variables parameterized with descriptive comments and validation.
- [ ] Zero committed `.tfstate` files or `.tfvars` containing secrets.
- [ ] Sensitive outputs marked `sensitive = true`.

---

## 3. PR Rejection Protocol

Use standard constructive rejection comments:

> **PR Status: Changes Requested**
> 
> Thank you for your submission. Your PR cannot be approved in its current state due to the following items:
> 1. **Assignment A03-04:** Missing terminal evidence logs showing packet inspection with `tcpdump`.
> 2. **Security:** Dockerfile for assignment A10-02 runs as root user. Update to run as an unprivileged user.
> 3. **Weekly Report:** Section 4 ("What Remains Unclear") is incomplete.
> 
> Please push revisions to this branch. We will re-evaluate during the Saturday session.
