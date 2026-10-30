# Assignment A03-02: A03-02: Configuring and Implementing IPv4 and IPv6 addressing, subnets and CIDR notation

- **Assignment ID:** `A03-02`
- **Week:** Week 03 — Networking Fundamentals I
- **Difficulty:** Beginner-Intermediate
- **Estimated Duration:** 75 minutes

---

## 1. Learning Objective
Develop hands-on competence in ipv4 and ipv6 addressing, subnets and cidr notation using iproute2 (ip addr, ip route).

---

## 2. Background and Context
In production environments, ipv4 and ipv6 addressing, subnets and cidr notation is a core engineering requirement. Engineers must understand how iproute2 (ip addr, ip route) behaves under realistic conditions, avoid common operational anti-patterns, and verify state through reproducible telemetry.

---

## 3. Requirements
1. Adhere strictly to the Principle of Least Privilege and safe engineering practices.
2. All commands, configurations, and verification scripts must be version-controlled in Git.
3. Every step must be executed in a dedicated sandbox or directory (`~/devops-lab/week-03/assignment-02/`).
4. Output logs, terminal recordings, or configuration files must be documented in the submission folder.

---

## 4. Step-by-Step Tasks
### Task 1: Environment Setup & Initialization
- Create the isolated lab directory:
  ```bash
  mkdir -p ~/devops-lab/week-03/assignment-02
  cd ~/devops-lab/week-03/assignment-02
  ```
- Initialize tracking and verify tool dependencies (iproute2 (ip addr, ip route)).

### Task 2: Core Technical Implementation
- Implement the primary technical requirement for ipv4 and ipv6 addressing, subnets and cidr notation.
- Construct the configuration files or scripts adhering to standard industry patterns.
- Ensure all permissions, network bindings, and variables are explicitly defined.

### Task 3: Verification & Telemetry Collection
- Execute standard testing and operational verification commands:
  ```bash
  echo "=== Verifying implementation for A03-02 ==="
  # Run verification commands
  ```
- Verify error-handling behavior when given invalid parameters or unexpected conditions.

### Task 4: Documentation & Evidence Capture
- Record your execution logs and save output artifacts into `submissions/week-03/assignment-02/`.

---

## 5. Expected Result
A verified, working implementation of ipv4 and ipv6 addressing, subnets and cidr notation with zero syntax errors, passing validation tests, and documented in clear terminal transcripts.

---

## 6. Submission Requirements
Place the following files in `submissions/week-03/assignment-02/`:
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
