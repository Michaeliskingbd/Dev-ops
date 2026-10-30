# Week 09: Docker Fundamentals I

**Stage 2: DevOps Engineering Tools (Days 57-63)**

---

## 1. Week Number and Title
- **Week:** Week 09
- **Title:** Docker Fundamentals I
- **Stage:** Stage 2 — DevOps Engineering Tools
- **Timeline:** Days 57 to 63

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master virtualisation (hypervisors) versus containerisation (cgroups, namespaces) and articulate its operational tradeoffs.
- Master docker daemon, containerd, and client architecture and articulate its operational tradeoffs.
- Master images versus running containers and articulate its operational tradeoffs.
- Master anatomy of a dockerfile: from, run, copy, workdir, expose, cmd, entrypoint and articulate its operational tradeoffs.
- Master image layers, union file system (overlay2), and build cache optimization and articulate its operational tradeoffs.
- Master container lifecycle: create, start, stop, pause, restart, kill, rm and articulate its operational tradeoffs.
- Master docker cli commands: run, ps, exec, logs, inspect, stats, build, tag and articulate its operational tradeoffs.
- Master building custom minimal images using alpine and distroless bases and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using Docker Engine, docker CLI, dive (layer inspector), Dockerfile.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 08.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of Docker Fundamentals I is critical. DevOps engineers must understand virtualisation (hypervisors) versus containerisation (cgroups, namespaces) and docker daemon, containerd, and client architecture to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of Docker Fundamentals I
Docker Fundamentals I forms a foundational pillar of DevOps Engineering Tools. When operating distributed systems at scale, engineers must manage:
- **Virtualisation (hypervisors) versus Containerisation (cgroups, namespaces):** Understanding architectural components, state management, and operational boundaries.
- **Docker daemon, containerd, and client architecture:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Images versus running containers:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, Docker Engine and docker CLI provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 57):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for Docker Engine.
- **Tuesday (Day 58):** Fundamental configuration, command-line interfaces, and executing Assignment A09-01 and A09-02.
- **Wednesday (Day 59):** Deep dive into Images versus running containers, edge cases, and completing Assignment A09-03.
- **Thursday (Day 60):** Production hardening, security controls, automated healthchecks, and completing Assignment A09-04.
- **Friday (Day 61):** Diagnostic methodology, error injection drills, completing Assignment A09-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 62):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for Docker Fundamentals I ==="
which docker || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-09
cd ~/devops-lab/week-09

# 4. Verification and telemetry capture
echo "Ready for Week 09 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in Docker Fundamentals I**
During a high-traffic deployment, a critical failure occurred involving virtualisation (hypervisors) versus containerisation (cgroups, namespaces). The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in Docker Fundamentals I**
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
# Recommended tooling installation for Docker Fundamentals I
# Tools required: Docker Engine, docker CLI, dive (layer inspector), Dockerfile
echo "Ensure Docker Engine is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: Docker Engine](https://docs.docker.com/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A09-01 through A09-05.
2. Terminal execution logs and verification evidence in `submissions/week-09/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-09-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Virtualisation (hypervisors) versus Containerisation (cgroups, namespaces).
2. What are the key operational differences between happy-path implementation and production-grade resilience in Docker Fundamentals I?
3. How do you monitor and debug failures occurring within Docker Engine?
4. Describe two common security vulnerabilities or misconfigurations associated with Docker daemon, containerd, and client architecture and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Virtualisation (hypervisors) versus Containerisation (cgroups, namespaces) and Docker daemon, containerd, and client architecture. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
