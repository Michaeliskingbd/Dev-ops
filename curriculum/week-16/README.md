# Week 16: Terraform Fundamentals II

**Stage 2: DevOps Engineering Tools (Days 106-112)**

---

## 1. Week Number and Title
- **Week:** Week 16
- **Title:** Terraform Fundamentals II
- **Stage:** Stage 2 — DevOps Engineering Tools
- **Timeline:** Days 106 to 112

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master terraform modules: root module versus child modules, inputs and outputs and articulate its operational tradeoffs.
- Master designing reusable infrastructure components (vpc module, compute module) and articulate its operational tradeoffs.
- Master remote state management: amazon s3 backend with dynamodb state locking and articulate its operational tradeoffs.
- Master managing multiple environments: directory separation versus terraform workspaces and articulate its operational tradeoffs.
- Master terraform validation, canonical formatting (fmt), and linting (tflint) and articulate its operational tradeoffs.
- Master dependency management: implicit versus explicit dependencies (depends_on) and articulate its operational tradeoffs.
- Master detecting and handling infrastructure drift (terraform refresh and plan) and articulate its operational tradeoffs.
- Master automating terraform workflows in github actions with oidc aws credentials and articulate its operational tradeoffs.
- Master secure infrastructure configuration: preventing plain-text secret leaks in state and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using Terraform Remote Backend (S3/DynamoDB), tflint, tfsec / trivy, GitHub Actions OIDC.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 15.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of Terraform Fundamentals II is critical. DevOps engineers must understand terraform modules: root module versus child modules, inputs and outputs and designing reusable infrastructure components (vpc module, compute module) to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of Terraform Fundamentals II
Terraform Fundamentals II forms a foundational pillar of DevOps Engineering Tools. When operating distributed systems at scale, engineers must manage:
- **Terraform modules: root module versus child modules, inputs and outputs:** Understanding architectural components, state management, and operational boundaries.
- **Designing reusable infrastructure components (VPC module, Compute module):** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Remote state management: Amazon S3 backend with DynamoDB state locking:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, Terraform Remote Backend (S3/DynamoDB) and tflint provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 106):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for Terraform Remote Backend (S3/DynamoDB).
- **Tuesday (Day 107):** Fundamental configuration, command-line interfaces, and executing Assignment A16-01 and A16-02.
- **Wednesday (Day 108):** Deep dive into Remote state management: Amazon S3 backend with DynamoDB state locking, edge cases, and completing Assignment A16-03.
- **Thursday (Day 109):** Production hardening, security controls, automated healthchecks, and completing Assignment A16-04.
- **Friday (Day 110):** Diagnostic methodology, error injection drills, completing Assignment A16-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 111):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for Terraform Fundamentals II ==="
which terraform || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-16
cd ~/devops-lab/week-16

# 4. Verification and telemetry capture
echo "Ready for Week 16 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in Terraform Fundamentals II**
During a high-traffic deployment, a critical failure occurred involving terraform modules: root module versus child modules, inputs and outputs. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in Terraform Fundamentals II**
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
# Recommended tooling installation for Terraform Fundamentals II
# Tools required: Terraform Remote Backend (S3/DynamoDB), tflint, tfsec / trivy, GitHub Actions OIDC
echo "Ensure Terraform Remote Backend (S3/DynamoDB) is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: Terraform Remote Backend (S3/DynamoDB)](https://developer.hashicorp.com/terraform/docs)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A16-01 through A16-05.
2. Terminal execution logs and verification evidence in `submissions/week-16/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-16-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Terraform modules: root module versus child modules, inputs and outputs.
2. What are the key operational differences between happy-path implementation and production-grade resilience in Terraform Fundamentals II?
3. How do you monitor and debug failures occurring within Terraform Remote Backend (S3/DynamoDB)?
4. Describe two common security vulnerabilities or misconfigurations associated with Designing reusable infrastructure components (VPC module, Compute module) and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Terraform modules: root module versus child modules, inputs and outputs and Designing reusable infrastructure components (VPC module, Compute module). The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
