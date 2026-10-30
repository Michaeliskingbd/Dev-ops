# Week 11: CI/CD Fundamentals

**Stage 2: DevOps Engineering Tools (Days 71-77)**

---

## 1. Week Number and Title
- **Week:** Week 11
- **Title:** CI/CD Fundamentals
- **Stage:** Stage 2 — DevOps Engineering Tools
- **Timeline:** Days 71 to 77

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master the software delivery lifecycle (sdlc) and devops feedback loops and articulate its operational tradeoffs.
- Master continuous integration (ci): automated linting, testing, and building on commit and articulate its operational tradeoffs.
- Master continuous delivery (cd) versus continuous deployment: human gates vs full automation and articulate its operational tradeoffs.
- Master pipeline stages: checkout, lint, test, build, package, test-deploy, production and articulate its operational tradeoffs.
- Master automated testing in pipelines: unit tests, integration tests, smoke tests and articulate its operational tradeoffs.
- Master build automation and caching dependencies and articulate its operational tradeoffs.
- Master deployment strategies: blue-green, canary, rolling updates, and recreate and articulate its operational tradeoffs.
- Master artifact management: registries, semantic versioning, and immutable build tags and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using Git triggers, CI pipelines, Semantic Versioning, Container Registries.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 10.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of CI/CD Fundamentals is critical. DevOps engineers must understand the software delivery lifecycle (sdlc) and devops feedback loops and continuous integration (ci): automated linting, testing, and building on commit to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of CI/CD Fundamentals
CI/CD Fundamentals forms a foundational pillar of DevOps Engineering Tools. When operating distributed systems at scale, engineers must manage:
- **The Software Delivery Lifecycle (SDLC) and DevOps feedback loops:** Understanding architectural components, state management, and operational boundaries.
- **Continuous Integration (CI): automated linting, testing, and building on commit:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Continuous Delivery (CD) versus Continuous Deployment: human gates vs full automation:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, Git triggers and CI pipelines provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 71):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for Git triggers.
- **Tuesday (Day 72):** Fundamental configuration, command-line interfaces, and executing Assignment A11-01 and A11-02.
- **Wednesday (Day 73):** Deep dive into Continuous Delivery (CD) versus Continuous Deployment: human gates vs full automation, edge cases, and completing Assignment A11-03.
- **Thursday (Day 74):** Production hardening, security controls, automated healthchecks, and completing Assignment A11-04.
- **Friday (Day 75):** Diagnostic methodology, error injection drills, completing Assignment A11-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 76):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for CI/CD Fundamentals ==="
which git || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-11
cd ~/devops-lab/week-11

# 4. Verification and telemetry capture
echo "Ready for Week 11 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in CI/CD Fundamentals**
During a high-traffic deployment, a critical failure occurred involving the software delivery lifecycle (sdlc) and devops feedback loops. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in CI/CD Fundamentals**
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
# Recommended tooling installation for CI/CD Fundamentals
# Tools required: Git triggers, CI pipelines, Semantic Versioning, Container Registries
echo "Ensure Git triggers is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: Git triggers](https://www.python.org/doc/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A11-01 through A11-05.
2. Terminal execution logs and verification evidence in `submissions/week-11/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-11-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by The Software Delivery Lifecycle (SDLC) and DevOps feedback loops.
2. What are the key operational differences between happy-path implementation and production-grade resilience in CI/CD Fundamentals?
3. How do you monitor and debug failures occurring within Git triggers?
4. Describe two common security vulnerabilities or misconfigurations associated with Continuous Integration (CI): automated linting, testing, and building on commit and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing The Software Delivery Lifecycle (SDLC) and DevOps feedback loops and Continuous Integration (CI): automated linting, testing, and building on commit. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
