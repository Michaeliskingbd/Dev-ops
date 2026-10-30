# Week 14: AWS Fundamentals II

**Stage 2: DevOps Engineering Tools (Days 92-98)**

---

## 1. Week Number and Title
- **Week:** Week 14
- **Title:** AWS Fundamentals II
- **Stage:** Stage 2 — DevOps Engineering Tools
- **Timeline:** Days 92 to 98

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master virtual private cloud (vpc) architecture: ip addressing and subnets and articulate its operational tradeoffs.
- Master public subnets, private subnets, and database subnets and articulate its operational tradeoffs.
- Master internet gateways (igw) and route tables and articulate its operational tradeoffs.
- Master nat gateways versus nat instances for egress from private subnets and articulate its operational tradeoffs.
- Master amazon s3: buckets, object storage, versioning, lifecycles, and bucket policies and articulate its operational tradeoffs.
- Master amazon rds overview: managed relational databases (postgresql) and multi-az and articulate its operational tradeoffs.
- Master amazon route 53: hosted zones, dns routing policies, and domain management and articulate its operational tradeoffs.
- Master amazon cloudwatch: metrics, alarms, and cloudwatch logs agent and articulate its operational tradeoffs.
- Master aws billing, cost allocation tags, cost explorer, and aws budgets alerts and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using AWS VPC, AWS S3, AWS RDS PostgreSQL, AWS CloudWatch, AWS Budgets.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 13.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of AWS Fundamentals II is critical. DevOps engineers must understand virtual private cloud (vpc) architecture: ip addressing and subnets and public subnets, private subnets, and database subnets to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of AWS Fundamentals II
AWS Fundamentals II forms a foundational pillar of DevOps Engineering Tools. When operating distributed systems at scale, engineers must manage:
- **Virtual Private Cloud (VPC) architecture: IP addressing and subnets:** Understanding architectural components, state management, and operational boundaries.
- **Public subnets, private subnets, and database subnets:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Internet Gateways (IGW) and Route Tables:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, AWS VPC and AWS S3 provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 92):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for AWS VPC.
- **Tuesday (Day 93):** Fundamental configuration, command-line interfaces, and executing Assignment A14-01 and A14-02.
- **Wednesday (Day 94):** Deep dive into Internet Gateways (IGW) and Route Tables, edge cases, and completing Assignment A14-03.
- **Thursday (Day 95):** Production hardening, security controls, automated healthchecks, and completing Assignment A14-04.
- **Friday (Day 96):** Diagnostic methodology, error injection drills, completing Assignment A14-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 97):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for AWS Fundamentals II ==="
which aws || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-14
cd ~/devops-lab/week-14

# 4. Verification and telemetry capture
echo "Ready for Week 14 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in AWS Fundamentals II**
During a high-traffic deployment, a critical failure occurred involving virtual private cloud (vpc) architecture: ip addressing and subnets. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in AWS Fundamentals II**
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
# Recommended tooling installation for AWS Fundamentals II
# Tools required: AWS VPC, AWS S3, AWS RDS PostgreSQL, AWS CloudWatch, AWS Budgets
echo "Ensure AWS VPC is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: AWS VPC](https://docs.aws.amazon.com/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A14-01 through A14-05.
2. Terminal execution logs and verification evidence in `submissions/week-14/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-14-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Virtual Private Cloud (VPC) architecture: IP addressing and subnets.
2. What are the key operational differences between happy-path implementation and production-grade resilience in AWS Fundamentals II?
3. How do you monitor and debug failures occurring within AWS VPC?
4. Describe two common security vulnerabilities or misconfigurations associated with Public subnets, private subnets, and database subnets and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Virtual Private Cloud (VPC) architecture: IP addressing and subnets and Public subnets, private subnets, and database subnets. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
