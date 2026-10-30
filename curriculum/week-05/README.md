# Week 05: Git and GitHub

**Stage 1: Technical Foundations (Days 29-35)**

---

## 1. Week Number and Title
- **Week:** Week 05
- **Title:** Git and GitHub
- **Stage:** Stage 1 — Technical Foundations
- **Timeline:** Days 29 to 35

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master git distributed architecture and internal object model (blobs, trees, commits, tags) and articulate its operational tradeoffs.
- Master local repository initialization, staging, and commits and articulate its operational tradeoffs.
- Master branching models, pointer mechanics, and branch management and articulate its operational tradeoffs.
- Master merging strategies (fast-forward, three-way merge) versus rebasing and articulate its operational tradeoffs.
- Master pull request workflows and effective peer code reviews and articulate its operational tradeoffs.
- Master merge conflict anatomy, prevention, and manual resolution and articulate its operational tradeoffs.
- Master github issues, labels, and issue templates and articulate its operational tradeoffs.
- Master github projects, boards, and milestone tracking and articulate its operational tradeoffs.
- Master repository documentation best practices (readme, contributing, changelog) and articulate its operational tradeoffs.
- Master team collaboration, branch protection, and release tagging and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using git CLI, GitHub CLI (gh), Markdown, Git hooks.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 04.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of Git and GitHub is critical. DevOps engineers must understand git distributed architecture and internal object model (blobs, trees, commits, tags) and local repository initialization, staging, and commits to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of Git and GitHub
Git and GitHub forms a foundational pillar of Technical Foundations. When operating distributed systems at scale, engineers must manage:
- **Git distributed architecture and internal object model (blobs, trees, commits, tags):** Understanding architectural components, state management, and operational boundaries.
- **Local repository initialization, staging, and commits:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Branching models, pointer mechanics, and branch management:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, git CLI and GitHub CLI (gh) provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 29):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for git CLI.
- **Tuesday (Day 30):** Fundamental configuration, command-line interfaces, and executing Assignment A05-01 and A05-02.
- **Wednesday (Day 31):** Deep dive into Branching models, pointer mechanics, and branch management, edge cases, and completing Assignment A05-03.
- **Thursday (Day 32):** Production hardening, security controls, automated healthchecks, and completing Assignment A05-04.
- **Friday (Day 33):** Diagnostic methodology, error injection drills, completing Assignment A05-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 34):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for Git and GitHub ==="
which git || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-05
cd ~/devops-lab/week-05

# 4. Verification and telemetry capture
echo "Ready for Week 05 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in Git and GitHub**
During a high-traffic deployment, a critical failure occurred involving git distributed architecture and internal object model (blobs, trees, commits, tags). The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in Git and GitHub**
1. **Symptom:** Service fails to initialize or transitions into an error state.
2. **Diagnostic commands:**
   - Inspect status, events, and recent log traces.
   - Validate syntax and schema using official linting tools.
   - Verify network connectivity, ports, and permissions.
3. **Root Cause Analysis:** Trace configuration discrepancies between intended state and live environment.
4. **Resolution:** Rectify configuration, reload or redeploy cleanly, and verify health.

---

## 11. Required Tools and Installation Instructions
```bash
# Recommended tooling installation for Git and GitHub
# Tools required: git CLI, GitHub CLI (gh), Markdown, Git hooks
echo "Ensure git CLI is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: git CLI](https://docs.github.com/en/actions)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A05-01 through A05-05.
2. Terminal execution logs and verification evidence in `submissions/week-05/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-05-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Git distributed architecture and internal object model (blobs, trees, commits, tags).
2. What are the key operational differences between happy-path implementation and production-grade resilience in Git and GitHub?
3. How do you monitor and debug failures occurring within git CLI?
4. Describe two common security vulnerabilities or misconfigurations associated with Local repository initialization, staging, and commits and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Git distributed architecture and internal object model (blobs, trees, commits, tags) and Local repository initialization, staging, and commits. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
