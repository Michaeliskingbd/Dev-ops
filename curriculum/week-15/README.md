# Week 15: Terraform Fundamentals I

**Stage 2: DevOps Engineering Tools (Days 99-105)**

---

## 1. Week Number and Title
- **Week:** Week 15
- **Title:** Terraform Fundamentals I
- **Stage:** Stage 2 — DevOps Engineering Tools
- **Timeline:** Days 99 to 105

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master infrastructure as code (iac) principles: declarative vs imperative, repeatability and articulate its operational tradeoffs.
- Master terraform architecture, core engine, and provider ecosystem and articulate its operational tradeoffs.
- Master configuring providers (hashicorp aws provider) and authentication and articulate its operational tradeoffs.
- Master declaring resources and understanding hcl (hashicorp configuration language) and articulate its operational tradeoffs.
- Master input variables, variable validation, and local values (locals) and articulate its operational tradeoffs.
- Master output values and exporting infrastructure attributes and articulate its operational tradeoffs.
- Master data sources: querying existing aws resources (amis, vpcs) and articulate its operational tradeoffs.
- Master the terraform state file (terraform.tfstate): purpose, risks, and inspection and articulate its operational tradeoffs.
- Master the execution lifecycle: terraform init, validate, plan, apply, and destroy and articulate its operational tradeoffs.
- Master provisioning core aws resources (vpc, subnets, ec2, security groups) with terraform and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using Terraform CLI (>= 1.8), AWS Provider, HCL, terraform-docs.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 14.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of Terraform Fundamentals I is critical. DevOps engineers must understand infrastructure as code (iac) principles: declarative vs imperative, repeatability and terraform architecture, core engine, and provider ecosystem to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of Terraform Fundamentals I
Terraform Fundamentals I forms a foundational pillar of DevOps Engineering Tools. When operating distributed systems at scale, engineers must manage:
- **Infrastructure as Code (IaC) principles: declarative vs imperative, repeatability:** Understanding architectural components, state management, and operational boundaries.
- **Terraform architecture, core engine, and provider ecosystem:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Configuring providers (HashiCorp AWS provider) and authentication:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, Terraform CLI (>= 1.8) and AWS Provider provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 99):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for Terraform CLI (>= 1.8).
- **Tuesday (Day 100):** Fundamental configuration, command-line interfaces, and executing Assignment A15-01 and A15-02.
- **Wednesday (Day 101):** Deep dive into Configuring providers (HashiCorp AWS provider) and authentication, edge cases, and completing Assignment A15-03.
- **Thursday (Day 102):** Production hardening, security controls, automated healthchecks, and completing Assignment A15-04.
- **Friday (Day 103):** Diagnostic methodology, error injection drills, completing Assignment A15-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 104):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for Terraform Fundamentals I ==="
which terraform || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-15
cd ~/devops-lab/week-15

# 4. Verification and telemetry capture
echo "Ready for Week 15 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in Terraform Fundamentals I**
During a high-traffic deployment, a critical failure occurred involving infrastructure as code (iac) principles: declarative vs imperative, repeatability. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in Terraform Fundamentals I**
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
# Recommended tooling installation for Terraform Fundamentals I
# Tools required: Terraform CLI (>= 1.8), AWS Provider, HCL, terraform-docs
echo "Ensure Terraform CLI (>= 1.8) is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: Terraform CLI (>= 1.8)](https://developer.hashicorp.com/terraform/docs)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A15-01 through A15-05.
2. Terminal execution logs and verification evidence in `submissions/week-15/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-15-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Infrastructure as Code (IaC) principles: declarative vs imperative, repeatability.
2. What are the key operational differences between happy-path implementation and production-grade resilience in Terraform Fundamentals I?
3. How do you monitor and debug failures occurring within Terraform CLI (>= 1.8)?
4. Describe two common security vulnerabilities or misconfigurations associated with Terraform architecture, core engine, and provider ecosystem and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Infrastructure as Code (IaC) principles: declarative vs imperative, repeatability and Terraform architecture, core engine, and provider ecosystem. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
