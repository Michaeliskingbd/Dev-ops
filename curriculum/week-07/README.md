# Week 07: Python and Bash Automation

**Stage 1: Technical Foundations (Days 43-49)**

---

## 1. Week Number and Title
- **Week:** Week 07
- **Title:** Python and Bash Automation
- **Stage:** Stage 1 — Technical Foundations
- **Timeline:** Days 43 to 49

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master python standard library modules (os, sys, pathlib, json, time) and articulate its operational tradeoffs.
- Master parsing and generating structured configurations (json and yaml) and articulate its operational tradeoffs.
- Master making http api requests with urllib and requests and articulate its operational tradeoffs.
- Master executing system processes safely with subprocess and articulate its operational tradeoffs.
- Master structured application logging and error reporting and articulate its operational tradeoffs.
- Master environment variables and secrets ingestion and articulate its operational tradeoffs.
- Master bash scripting fundamentals: shebang, variables, and parameters and articulate its operational tradeoffs.
- Master exit codes, error handling (set -euo pipefail), and logic in bash and articulate its operational tradeoffs.
- Master cli arguments parsing in python (argparse) and bash (getopts) and articulate its operational tradeoffs.
- Master automating repetitive system administration and maintenance tasks and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using Python subprocess, requests, PyYAML, Bash, cron/systemd timers.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 06.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of Python and Bash Automation is critical. DevOps engineers must understand python standard library modules (os, sys, pathlib, json, time) and parsing and generating structured configurations (json and yaml) to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of Python and Bash Automation
Python and Bash Automation forms a foundational pillar of Technical Foundations. When operating distributed systems at scale, engineers must manage:
- **Python standard library modules (os, sys, pathlib, json, time):** Understanding architectural components, state management, and operational boundaries.
- **Parsing and generating structured configurations (JSON and YAML):** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Making HTTP API requests with urllib and requests:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, Python subprocess and requests provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 43):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for Python subprocess.
- **Tuesday (Day 44):** Fundamental configuration, command-line interfaces, and executing Assignment A07-01 and A07-02.
- **Wednesday (Day 45):** Deep dive into Making HTTP API requests with urllib and requests, edge cases, and completing Assignment A07-03.
- **Thursday (Day 46):** Production hardening, security controls, automated healthchecks, and completing Assignment A07-04.
- **Friday (Day 47):** Diagnostic methodology, error injection drills, completing Assignment A07-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 48):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for Python and Bash Automation ==="
which python || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-07
cd ~/devops-lab/week-07

# 4. Verification and telemetry capture
echo "Ready for Week 07 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in Python and Bash Automation**
During a high-traffic deployment, a critical failure occurred involving python standard library modules (os, sys, pathlib, json, time). The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in Python and Bash Automation**
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
# Recommended tooling installation for Python and Bash Automation
# Tools required: Python subprocess, requests, PyYAML, Bash, cron/systemd timers
echo "Ensure Python subprocess is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: Python subprocess](https://www.python.org/doc/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A07-01 through A07-05.
2. Terminal execution logs and verification evidence in `submissions/week-07/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-07-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Python standard library modules (os, sys, pathlib, json, time).
2. What are the key operational differences between happy-path implementation and production-grade resilience in Python and Bash Automation?
3. How do you monitor and debug failures occurring within Python subprocess?
4. Describe two common security vulnerabilities or misconfigurations associated with Parsing and generating structured configurations (JSON and YAML) and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Python standard library modules (os, sys, pathlib, json, time) and Parsing and generating structured configurations (JSON and YAML). The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
