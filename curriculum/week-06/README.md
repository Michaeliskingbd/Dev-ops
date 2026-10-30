# Week 06: Python Fundamentals I

**Stage 1: Technical Foundations (Days 36-42)**

---

## 1. Week Number and Title
- **Week:** Week 06
- **Title:** Python Fundamentals I
- **Stage:** Stage 1 — Technical Foundations
- **Timeline:** Days 36 to 42

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master python runtime environment, variables, and primitive data types and articulate its operational tradeoffs.
- Master string manipulation, formatting (f-strings), and number operations and articulate its operational tradeoffs.
- Master data structures: lists, tuples, sets, and dictionaries and articulate its operational tradeoffs.
- Master control flow: conditional branching (if/elif/else) and articulate its operational tradeoffs.
- Master iteration: for loops, while loops, and list comprehensions and articulate its operational tradeoffs.
- Master functions: parameters, default values, return types, and docstrings and articulate its operational tradeoffs.
- Master exception handling with try/except/finally and custom errors and articulate its operational tradeoffs.
- Master file system i/o: reading, writing, and context managers (with open) and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using Python 3.12+, venv, pytest basics, pylint/flake8.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 05.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of Python Fundamentals I is critical. DevOps engineers must understand python runtime environment, variables, and primitive data types and string manipulation, formatting (f-strings), and number operations to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of Python Fundamentals I
Python Fundamentals I forms a foundational pillar of Technical Foundations. When operating distributed systems at scale, engineers must manage:
- **Python runtime environment, variables, and primitive data types:** Understanding architectural components, state management, and operational boundaries.
- **String manipulation, formatting (f-strings), and number operations:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Data structures: lists, tuples, sets, and dictionaries:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, Python 3.12+ and venv provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 36):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for Python 3.12+.
- **Tuesday (Day 37):** Fundamental configuration, command-line interfaces, and executing Assignment A06-01 and A06-02.
- **Wednesday (Day 38):** Deep dive into Data structures: lists, tuples, sets, and dictionaries, edge cases, and completing Assignment A06-03.
- **Thursday (Day 39):** Production hardening, security controls, automated healthchecks, and completing Assignment A06-04.
- **Friday (Day 40):** Diagnostic methodology, error injection drills, completing Assignment A06-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 41):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for Python Fundamentals I ==="
which python || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-06
cd ~/devops-lab/week-06

# 4. Verification and telemetry capture
echo "Ready for Week 06 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in Python Fundamentals I**
During a high-traffic deployment, a critical failure occurred involving python runtime environment, variables, and primitive data types. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in Python Fundamentals I**
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
# Recommended tooling installation for Python Fundamentals I
# Tools required: Python 3.12+, venv, pytest basics, pylint/flake8
echo "Ensure Python 3.12+ is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: Python 3.12+](https://www.python.org/doc/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A06-01 through A06-05.
2. Terminal execution logs and verification evidence in `submissions/week-06/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-06-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Python runtime environment, variables, and primitive data types.
2. What are the key operational differences between happy-path implementation and production-grade resilience in Python Fundamentals I?
3. How do you monitor and debug failures occurring within Python 3.12+?
4. Describe two common security vulnerabilities or misconfigurations associated with String manipulation, formatting (f-strings), and number operations and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Python runtime environment, variables, and primitive data types and String manipulation, formatting (f-strings), and number operations. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
