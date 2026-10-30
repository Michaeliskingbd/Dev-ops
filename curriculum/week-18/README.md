# Week 18: Kubernetes Fundamentals II

**Stage 3: Production Engineering and Capstone (Days 120-126)**

---

## 1. Week Number and Title
- **Week:** Week 18
- **Title:** Kubernetes Fundamentals II
- **Stage:** Stage 3 — Production Engineering and Capstone
- **Timeline:** Days 120 to 126

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master kubernetes services: service discovery, endpoints, and label selectors and articulate its operational tradeoffs.
- Master service types: clusterip (internal), nodeport (port exposure), loadbalancer (cloud) and articulate its operational tradeoffs.
- Master configuring applications with configmaps (literal, file, directory) and articulate its operational tradeoffs.
- Master managing sensitive data with kubernetes secrets (base64 encoding vs encryption at rest) and articulate its operational tradeoffs.
- Master persistent volumes (pv), persistent volume claims (pvc), and storageclasses and articulate its operational tradeoffs.
- Master container health probes: startupprobe, livenessprobe, and readinessprobe and articulate its operational tradeoffs.
- Master resource requests and limits: cpu (millicores) and memory (mib/gib), qos classes and articulate its operational tradeoffs.
- Master deploying a complete 3-tier application (frontend, backend api, postgresql) in kubernetes and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using kubectl, Local PV/PVC, Kubernetes Health Probes, Kubeval / kubeconform.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 17.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of Kubernetes Fundamentals II is critical. DevOps engineers must understand kubernetes services: service discovery, endpoints, and label selectors and service types: clusterip (internal), nodeport (port exposure), loadbalancer (cloud) to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of Kubernetes Fundamentals II
Kubernetes Fundamentals II forms a foundational pillar of Production Engineering and Capstone. When operating distributed systems at scale, engineers must manage:
- **Kubernetes Services: Service discovery, endpoints, and label selectors:** Understanding architectural components, state management, and operational boundaries.
- **Service types: ClusterIP (internal), NodePort (port exposure), LoadBalancer (cloud):** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Configuring applications with ConfigMaps (literal, file, directory):** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, kubectl and Local PV/PVC provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 120):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for kubectl.
- **Tuesday (Day 121):** Fundamental configuration, command-line interfaces, and executing Assignment A18-01 and A18-02.
- **Wednesday (Day 122):** Deep dive into Configuring applications with ConfigMaps (literal, file, directory), edge cases, and completing Assignment A18-03.
- **Thursday (Day 123):** Production hardening, security controls, automated healthchecks, and completing Assignment A18-04.
- **Friday (Day 124):** Diagnostic methodology, error injection drills, completing Assignment A18-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 125):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for Kubernetes Fundamentals II ==="
which kubectl || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-18
cd ~/devops-lab/week-18

# 4. Verification and telemetry capture
echo "Ready for Week 18 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in Kubernetes Fundamentals II**
During a high-traffic deployment, a critical failure occurred involving kubernetes services: service discovery, endpoints, and label selectors. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in Kubernetes Fundamentals II**
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
# Recommended tooling installation for Kubernetes Fundamentals II
# Tools required: kubectl, Local PV/PVC, Kubernetes Health Probes, Kubeval / kubeconform
echo "Ensure kubectl is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: kubectl](https://kubernetes.io/docs/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A18-01 through A18-05.
2. Terminal execution logs and verification evidence in `submissions/week-18/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-18-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Kubernetes Services: Service discovery, endpoints, and label selectors.
2. What are the key operational differences between happy-path implementation and production-grade resilience in Kubernetes Fundamentals II?
3. How do you monitor and debug failures occurring within kubectl?
4. Describe two common security vulnerabilities or misconfigurations associated with Service types: ClusterIP (internal), NodePort (port exposure), LoadBalancer (cloud) and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Kubernetes Services: Service discovery, endpoints, and label selectors and Service types: ClusterIP (internal), NodePort (port exposure), LoadBalancer (cloud). The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
