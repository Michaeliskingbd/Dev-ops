# Week 12: GitHub Actions

**Stage 2: DevOps Engineering Tools (Days 78-84)**

---

## 1. Week Number and Title
- **Week:** Week 12
- **Title:** GitHub Actions
- **Stage:** Stage 2 — DevOps Engineering Tools
- **Timeline:** Days 78 to 84

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master github actions workflow architecture: workflows, jobs, steps, runners and articulate its operational tradeoffs.
- Master events and triggers: push, pull_request, workflow_dispatch, schedule, paths filter and articulate its operational tradeoffs.
- Master runner environments: github-hosted runners versus self-hosted runners and articulate its operational tradeoffs.
- Master standard community actions (actions/checkout, actions/setup-python, actions/cache) and articulate its operational tradeoffs.
- Master managing secrets, variables, and environment configuration securely and articulate its operational tradeoffs.
- Master environment protection rules and required manual approval gates and articulate its operational tradeoffs.
- Master building automated test and lint pipelines for python/node and articulate its operational tradeoffs.
- Master automated docker image build and publish to github container registry (ghcr) and articulate its operational tradeoffs.
- Master automated deployment workflows triggered by release tags and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using GitHub Actions, GHCR / Docker Hub, actionlint, gh CLI.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 11.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of GitHub Actions is critical. DevOps engineers must understand github actions workflow architecture: workflows, jobs, steps, runners and events and triggers: push, pull_request, workflow_dispatch, schedule, paths filter to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of GitHub Actions
GitHub Actions forms a foundational pillar of DevOps Engineering Tools. When operating distributed systems at scale, engineers must manage:
- **GitHub Actions workflow architecture: workflows, jobs, steps, runners:** Understanding architectural components, state management, and operational boundaries.
- **Events and triggers: push, pull_request, workflow_dispatch, schedule, paths filter:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Runner environments: GitHub-hosted runners versus self-hosted runners:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, GitHub Actions and GHCR / Docker Hub provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 78):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for GitHub Actions.
- **Tuesday (Day 79):** Fundamental configuration, command-line interfaces, and executing Assignment A12-01 and A12-02.
- **Wednesday (Day 80):** Deep dive into Runner environments: GitHub-hosted runners versus self-hosted runners, edge cases, and completing Assignment A12-03.
- **Thursday (Day 81):** Production hardening, security controls, automated healthchecks, and completing Assignment A12-04.
- **Friday (Day 82):** Diagnostic methodology, error injection drills, completing Assignment A12-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 83):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for GitHub Actions ==="
which github || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-12
cd ~/devops-lab/week-12

# 4. Verification and telemetry capture
echo "Ready for Week 12 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in GitHub Actions**
During a high-traffic deployment, a critical failure occurred involving github actions workflow architecture: workflows, jobs, steps, runners. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in GitHub Actions**
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
# Recommended tooling installation for GitHub Actions
# Tools required: GitHub Actions, GHCR / Docker Hub, actionlint, gh CLI
echo "Ensure GitHub Actions is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: GitHub Actions](https://docs.github.com/en/actions)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A12-01 through A12-05.
2. Terminal execution logs and verification evidence in `submissions/week-12/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-12-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by GitHub Actions workflow architecture: workflows, jobs, steps, runners.
2. What are the key operational differences between happy-path implementation and production-grade resilience in GitHub Actions?
3. How do you monitor and debug failures occurring within GitHub Actions?
4. Describe two common security vulnerabilities or misconfigurations associated with Events and triggers: push, pull_request, workflow_dispatch, schedule, paths filter and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing GitHub Actions workflow architecture: workflows, jobs, steps, runners and Events and triggers: push, pull_request, workflow_dispatch, schedule, paths filter. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
