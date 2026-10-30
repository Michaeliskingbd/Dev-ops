# Assignment A14-04: A14-04: Production Hardening and Automation for NAT Gateways versus NAT Instances for egress from private subnets

- **Assignment ID:** `A14-04`
- **Week:** Week 14 — AWS Fundamentals II
- **Difficulty:** Intermediate-Advanced
- **Estimated Duration:** 105 minutes

---

## 1. Learning Objective
Develop hands-on competence in nat gateways versus nat instances for egress from private subnets using AWS VPC.

---

## 2. Background and Context
In production environments, nat gateways versus nat instances for egress from private subnets is a core engineering requirement. Engineers must understand how AWS VPC behaves under realistic conditions, avoid common operational anti-patterns, and verify state through reproducible telemetry.

---

## 3. Requirements
1. Adhere strictly to the Principle of Least Privilege and safe engineering practices.
2. All commands, configurations, and verification scripts must be version-controlled in Git.
3. Every step must be executed in a dedicated sandbox or directory (`~/devops-lab/week-14/assignment-04/`).
4. Output logs, terminal recordings, or configuration files must be documented in the submission folder.

---

## 4. Step-by-Step Tasks
### Task 1: Environment Setup & Initialization
- Create the isolated lab directory:
  ```bash
  mkdir -p ~/devops-lab/week-14/assignment-04
  cd ~/devops-lab/week-14/assignment-04
  ```
- Initialize tracking and verify tool dependencies (AWS VPC).

### Task 2: Core Technical Implementation
- Implement the primary technical requirement for nat gateways versus nat instances for egress from private subnets.
- Construct the configuration files or scripts adhering to standard industry patterns.
- Ensure all permissions, network bindings, and variables are explicitly defined.

### Task 3: Verification & Telemetry Collection
- Execute standard testing and operational verification commands:
  ```bash
  echo "=== Verifying implementation for A14-04 ==="
  # Run verification commands
  ```
- Verify error-handling behavior when given invalid parameters or unexpected conditions.

### Task 4: Documentation & Evidence Capture
- Record your execution logs and save output artifacts into `submissions/week-14/assignment-04/`.

---

## 5. Expected Result
A verified, working implementation of nat gateways versus nat instances for egress from private subnets with zero syntax errors, passing validation tests, and documented in clear terminal transcripts.

---

## 6. Submission Requirements
Place the following files in `submissions/week-14/assignment-04/`:
1. `solution.sh` (or `.py`, `.tf`, `.yaml` as appropriate).
2. `evidence.md` detailing exact commands executed and output received.
3. Relevant configuration files.

---

## 7. Evaluation Criteria
- **Correctness & Functionality (40%):** Implementation meets all functional requirements and passes execution tests.
- **Code & Configuration Quality (25%):** Follows formatting standards, includes comments/docstrings, and avoids hardcoded values.
- **Security & Best Practices (20%):** Enforces least privilege, secure permissions, and zero secret leaks.
- **Documentation & Evidence (15%):** Accurate, reproducible terminal transcripts and clear explanations.

---

## 8. Bonus Challenge
Extend this implementation by creating an automated self-test script that simulates an edge-case failure, verifies that the system handles the failure gracefully, and alerts the operator.
