# Week 21: DevOps Security

**Stage 3: Production Engineering and Capstone (Days 141-147)**

---

## 1. Week Number and Title
- **Week:** Week 21
- **Title:** DevOps Security
- **Stage:** Stage 3 — Production Engineering and Capstone
- **Timeline:** Days 141 to 147

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master devsecops philosophy: shifting security left into development and delivery workflows and articulate its operational tradeoffs.
- Master the principle of least privilege (polp) across iam, os, and containers and articulate its operational tradeoffs.
- Master hardening cloud iam: root account lockdown, role-based access, mfa enforcement and articulate its operational tradeoffs.
- Master secrets management best practices: aws ssm parameter store / secrets manager / hashicorp vault and articulate its operational tradeoffs.
- Master host and operating system hardening: ssh bastion, key-only auth, minimal packages and articulate its operational tradeoffs.
- Master container security: non-root users, drop capabilities, seccomp, apparmor and articulate its operational tradeoffs.
- Master dependency vulnerability scanning (pip-audit, npm audit, safety) and articulate its operational tradeoffs.
- Master container image vulnerability scanning with trivy and grype and articulate its operational tradeoffs.
- Master tls/https enforcement: automated certificates via let's encrypt / certbot and articulate its operational tradeoffs.
- Master network security: security groups, vpc network acls, and kubernetes networkpolicies and articulate its operational tradeoffs.
- Master securing ci/cd pipelines: secret masking, pinned actions, runner hardening and articulate its operational tradeoffs.
- Master stride threat modelling for web application infrastructure and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using Trivy, pip-audit, Certbot / Let's Encrypt, AWS SSM, GitGuardian.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 20.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of DevOps Security is critical. DevOps engineers must understand devsecops philosophy: shifting security left into development and delivery workflows and the principle of least privilege (polp) across iam, os, and containers to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of DevOps Security
DevOps Security forms a foundational pillar of Production Engineering and Capstone. When operating distributed systems at scale, engineers must manage:
- **DevSecOps philosophy: shifting security left into development and delivery workflows:** Understanding architectural components, state management, and operational boundaries.
- **The Principle of Least Privilege (PoLP) across IAM, OS, and containers:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Hardening cloud IAM: root account lockdown, role-based access, MFA enforcement:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, Trivy and pip-audit provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 141):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for Trivy.
- **Tuesday (Day 142):** Fundamental configuration, command-line interfaces, and executing Assignment A21-01 and A21-02.
- **Wednesday (Day 143):** Deep dive into Hardening cloud IAM: root account lockdown, role-based access, MFA enforcement, edge cases, and completing Assignment A21-03.
- **Thursday (Day 144):** Production hardening, security controls, automated healthchecks, and completing Assignment A21-04.
- **Friday (Day 145):** Diagnostic methodology, error injection drills, completing Assignment A21-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 146):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for DevOps Security ==="
which trivy || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-21
cd ~/devops-lab/week-21

# 4. Verification and telemetry capture
echo "Ready for Week 21 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in DevOps Security**
During a high-traffic deployment, a critical failure occurred involving devsecops philosophy: shifting security left into development and delivery workflows. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in DevOps Security**
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
# Recommended tooling installation for DevOps Security
# Tools required: Trivy, pip-audit, Certbot / Let's Encrypt, AWS SSM, GitGuardian
echo "Ensure Trivy is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: Trivy](https://www.python.org/doc/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A21-01 through A21-05.
2. Terminal execution logs and verification evidence in `submissions/week-21/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-21-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by DevSecOps philosophy: shifting security left into development and delivery workflows.
2. What are the key operational differences between happy-path implementation and production-grade resilience in DevOps Security?
3. How do you monitor and debug failures occurring within Trivy?
4. Describe two common security vulnerabilities or misconfigurations associated with The Principle of Least Privilege (PoLP) across IAM, OS, and containers and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing DevSecOps philosophy: shifting security left into development and delivery workflows and The Principle of Least Privilege (PoLP) across IAM, OS, and containers. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
