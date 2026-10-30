# Week 19: Kubernetes Operations

**Stage 3: Production Engineering and Capstone (Days 127-133)**

---

## 1. Week Number and Title
- **Week:** Week 19
- **Title:** Kubernetes Operations
- **Stage:** Stage 3 — Production Engineering and Capstone
- **Timeline:** Days 127 to 133

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master ingress controllers (nginx ingress) and routing http/https traffic to services and articulate its operational tradeoffs.
- Master coredns and cluster internal dns resolution workflows and articulate its operational tradeoffs.
- Master scaling workloads manually (kubectl scale) and automatically with hpa (horizontal pod autoscaler) and articulate its operational tradeoffs.
- Master zero-downtime rolling updates and rollback strategies (kubectl rollout undo) and articulate its operational tradeoffs.
- Master helm package manager: charts, templates, values.yaml, and release lifecycle and articulate its operational tradeoffs.
- Master systematic kubernetes troubleshooting methodology (crashloopbackoff, pending, imagepullbackoff, oomkilled) and articulate its operational tradeoffs.
- Master inspecting cluster logs, events, and container standard output and articulate its operational tradeoffs.
- Master cluster resource management, resourcequotas, and limitranges and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using Nginx Ingress Controller, Helm v3, kubectl rollout, Metrics Server.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 18.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of Kubernetes Operations is critical. DevOps engineers must understand ingress controllers (nginx ingress) and routing http/https traffic to services and coredns and cluster internal dns resolution workflows to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of Kubernetes Operations
Kubernetes Operations forms a foundational pillar of Production Engineering and Capstone. When operating distributed systems at scale, engineers must manage:
- **Ingress controllers (Nginx Ingress) and routing HTTP/HTTPS traffic to Services:** Understanding architectural components, state management, and operational boundaries.
- **CoreDNS and cluster internal DNS resolution workflows:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Scaling workloads manually (kubectl scale) and automatically with HPA (Horizontal Pod Autoscaler):** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, Nginx Ingress Controller and Helm v3 provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 127):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for Nginx Ingress Controller.
- **Tuesday (Day 128):** Fundamental configuration, command-line interfaces, and executing Assignment A19-01 and A19-02.
- **Wednesday (Day 129):** Deep dive into Scaling workloads manually (kubectl scale) and automatically with HPA (Horizontal Pod Autoscaler), edge cases, and completing Assignment A19-03.
- **Thursday (Day 130):** Production hardening, security controls, automated healthchecks, and completing Assignment A19-04.
- **Friday (Day 131):** Diagnostic methodology, error injection drills, completing Assignment A19-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 132):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for Kubernetes Operations ==="
which nginx || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-19
cd ~/devops-lab/week-19

# 4. Verification and telemetry capture
echo "Ready for Week 19 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in Kubernetes Operations**
During a high-traffic deployment, a critical failure occurred involving ingress controllers (nginx ingress) and routing http/https traffic to services. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in Kubernetes Operations**
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
# Recommended tooling installation for Kubernetes Operations
# Tools required: Nginx Ingress Controller, Helm v3, kubectl rollout, Metrics Server
echo "Ensure Nginx Ingress Controller is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: Nginx Ingress Controller](https://kubernetes.io/docs/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A19-01 through A19-05.
2. Terminal execution logs and verification evidence in `submissions/week-19/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-19-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Ingress controllers (Nginx Ingress) and routing HTTP/HTTPS traffic to Services.
2. What are the key operational differences between happy-path implementation and production-grade resilience in Kubernetes Operations?
3. How do you monitor and debug failures occurring within Nginx Ingress Controller?
4. Describe two common security vulnerabilities or misconfigurations associated with CoreDNS and cluster internal DNS resolution workflows and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Ingress controllers (Nginx Ingress) and routing HTTP/HTTPS traffic to Services and CoreDNS and cluster internal DNS resolution workflows. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
