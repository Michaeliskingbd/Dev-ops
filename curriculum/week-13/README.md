# Week 13: AWS Fundamentals I

**Stage 2: DevOps Engineering Tools (Days 85-91)**

---

## 1. Week Number and Title
- **Week:** Week 13
- **Title:** AWS Fundamentals I
- **Stage:** Stage 2 — DevOps Engineering Tools
- **Timeline:** Days 85 to 91

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master cloud computing service models (iaas, paas, saas) and shared responsibility model and articulate its operational tradeoffs.
- Master aws global infrastructure: regions, availability zones (azs), and edge locations and articulate its operational tradeoffs.
- Master identity and access management (iam): users, groups, roles, policies, and mfa and articulate its operational tradeoffs.
- Master iam policy json grammar (effect, action, resource, condition) and articulate its operational tradeoffs.
- Master amazon ec2: instance families, sizing, pricing models (on-demand, spot, reserved) and articulate its operational tradeoffs.
- Master key pairs, ami selection (ubuntu lts), and secure ssh bastion access and articulate its operational tradeoffs.
- Master ec2 security groups: stateful firewall rules (inbound/outbound) and articulate its operational tradeoffs.
- Master deploying and configuring a basic linux application server on ec2 and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using AWS Management Console, AWS CLI v2, EC2, IAM, SSH.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 12.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of AWS Fundamentals I is critical. DevOps engineers must understand cloud computing service models (iaas, paas, saas) and shared responsibility model and aws global infrastructure: regions, availability zones (azs), and edge locations to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of AWS Fundamentals I
AWS Fundamentals I forms a foundational pillar of DevOps Engineering Tools. When operating distributed systems at scale, engineers must manage:
- **Cloud computing service models (IaaS, PaaS, SaaS) and shared responsibility model:** Understanding architectural components, state management, and operational boundaries.
- **AWS Global Infrastructure: Regions, Availability Zones (AZs), and Edge Locations:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Identity and Access Management (IAM): users, groups, roles, policies, and MFA:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, AWS Management Console and AWS CLI v2 provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 85):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for AWS Management Console.
- **Tuesday (Day 86):** Fundamental configuration, command-line interfaces, and executing Assignment A13-01 and A13-02.
- **Wednesday (Day 87):** Deep dive into Identity and Access Management (IAM): users, groups, roles, policies, and MFA, edge cases, and completing Assignment A13-03.
- **Thursday (Day 88):** Production hardening, security controls, automated healthchecks, and completing Assignment A13-04.
- **Friday (Day 89):** Diagnostic methodology, error injection drills, completing Assignment A13-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 90):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for AWS Fundamentals I ==="
which aws || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-13
cd ~/devops-lab/week-13

# 4. Verification and telemetry capture
echo "Ready for Week 13 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in AWS Fundamentals I**
During a high-traffic deployment, a critical failure occurred involving cloud computing service models (iaas, paas, saas) and shared responsibility model. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in AWS Fundamentals I**
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
# Recommended tooling installation for AWS Fundamentals I
# Tools required: AWS Management Console, AWS CLI v2, EC2, IAM, SSH
echo "Ensure AWS Management Console is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: AWS Management Console](https://docs.aws.amazon.com/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A13-01 through A13-05.
2. Terminal execution logs and verification evidence in `submissions/week-13/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-13-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Cloud computing service models (IaaS, PaaS, SaaS) and shared responsibility model.
2. What are the key operational differences between happy-path implementation and production-grade resilience in AWS Fundamentals I?
3. How do you monitor and debug failures occurring within AWS Management Console?
4. Describe two common security vulnerabilities or misconfigurations associated with AWS Global Infrastructure: Regions, Availability Zones (AZs), and Edge Locations and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Cloud computing service models (IaaS, PaaS, SaaS) and shared responsibility model and AWS Global Infrastructure: Regions, Availability Zones (AZs), and Edge Locations. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
