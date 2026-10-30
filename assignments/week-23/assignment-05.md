# Assignment A23-05: A23-05: Failure Injection and Resilient Troubleshooting in Provisioning production AWS cloud infrastructure using modular Terraform

- **Assignment ID:** `A23-05`
- **Week:** Week 23 — Capstone Implementation
- **Difficulty:** Advanced / Troubleshooting
- **Estimated Duration:** 120 minutes

---

## 1. Learning Objective
Develop hands-on competence in provisioning production aws cloud infrastructure using modular terraform using Terraform.

---

## 2. Background and Context
In production environments, provisioning production aws cloud infrastructure using modular terraform is a core engineering requirement. Engineers must understand how Terraform behaves under realistic conditions, avoid common operational anti-patterns, and verify state through reproducible telemetry.

---

## 3. Requirements
1. Adhere strictly to the Principle of Least Privilege and safe engineering practices.
2. All commands, configurations, and verification scripts must be version-controlled in Git.
3. Every step must be executed in a dedicated sandbox or directory (`~/devops-lab/week-23/assignment-05/`).
4. Output logs, terminal recordings, or configuration files must be documented in the submission folder.

---

## 4. Step-by-Step Tasks
### Task 1: Environment Setup & Initialization
- Create the isolated lab directory:
  ```bash
  mkdir -p ~/devops-lab/week-23/assignment-05
  cd ~/devops-lab/week-23/assignment-05
  ```
- Initialize tracking and verify tool dependencies (Terraform).

### Task 2: Core Technical Implementation
- Implement the primary technical requirement for provisioning production aws cloud infrastructure using modular terraform.
- Construct the configuration files or scripts adhering to standard industry patterns.
- Ensure all permissions, network bindings, and variables are explicitly defined.

### Task 3: Verification & Telemetry Collection
- Execute standard testing and operational verification commands:
  ```bash
  echo "=== Verifying implementation for A23-05 ==="
  # Run verification commands
  ```
- Verify error-handling behavior when given invalid parameters or unexpected conditions.

### Task 4: Documentation & Evidence Capture
- Record your execution logs and save output artifacts into `submissions/week-23/assignment-05/`.

---

## 5. Expected Result
A verified, working implementation of provisioning production aws cloud infrastructure using modular terraform with zero syntax errors, passing validation tests, and documented in clear terminal transcripts.

---

## 6. Submission Requirements
Place the following files in `submissions/week-23/assignment-05/`:
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
