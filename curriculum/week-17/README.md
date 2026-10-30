# Week 17: Kubernetes Fundamentals I

**Stage 3: Production Engineering and Capstone (Days 113-119)**

---

## 1. Week Number and Title
- **Week:** Week 17
- **Title:** Kubernetes Fundamentals I
- **Stage:** Stage 3 — Production Engineering and Capstone
- **Timeline:** Days 113 to 119

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master why kubernetes exists: challenges of managing containers at production scale and articulate its operational tradeoffs.
- Master kubernetes control plane architecture: kube-apiserver, etcd, kube-scheduler, kube-controller-manager and articulate its operational tradeoffs.
- Master kubernetes worker node components: kubelet, kube-proxy, container runtime (containerd) and articulate its operational tradeoffs.
- Master pods: the atomic deployment unit, single-container vs multi-container pods and articulate its operational tradeoffs.
- Master deployments and replicasets: declarative self-healing and desired state management and articulate its operational tradeoffs.
- Master namespaces: multi-tenancy, logical isolation, and resource scoping and articulate its operational tradeoffs.
- Master the kubectl cli: context, configuration (~/.kube/config), and core imperative commands and articulate its operational tradeoffs.
- Master declarative yaml manifests: apiversion, kind, metadata, spec, status and articulate its operational tradeoffs.
- Master setting up local single-node clusters: minikube / k3s / kind and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using Minikube / Kind, kubectl, Kubernetes 1.29+, k9s (terminal UI).
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 16.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of Kubernetes Fundamentals I is critical. DevOps engineers must understand why kubernetes exists: challenges of managing containers at production scale and kubernetes control plane architecture: kube-apiserver, etcd, kube-scheduler, kube-controller-manager to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of Kubernetes Fundamentals I
Kubernetes Fundamentals I forms a foundational pillar of Production Engineering and Capstone. When operating distributed systems at scale, engineers must manage:
- **Why Kubernetes exists: challenges of managing containers at production scale:** Understanding architectural components, state management, and operational boundaries.
- **Kubernetes control plane architecture: kube-apiserver, etcd, kube-scheduler, kube-controller-manager:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Kubernetes worker node components: kubelet, kube-proxy, container runtime (containerd):** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, Minikube / Kind and kubectl provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 113):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for Minikube / Kind.
- **Tuesday (Day 114):** Fundamental configuration, command-line interfaces, and executing Assignment A17-01 and A17-02.
- **Wednesday (Day 115):** Deep dive into Kubernetes worker node components: kubelet, kube-proxy, container runtime (containerd), edge cases, and completing Assignment A17-03.
- **Thursday (Day 116):** Production hardening, security controls, automated healthchecks, and completing Assignment A17-04.
- **Friday (Day 117):** Diagnostic methodology, error injection drills, completing Assignment A17-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 118):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for Kubernetes Fundamentals I ==="
which minikube || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-17
cd ~/devops-lab/week-17

# 4. Verification and telemetry capture
echo "Ready for Week 17 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in Kubernetes Fundamentals I**
During a high-traffic deployment, a critical failure occurred involving why kubernetes exists: challenges of managing containers at production scale. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in Kubernetes Fundamentals I**
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
# Recommended tooling installation for Kubernetes Fundamentals I
# Tools required: Minikube / Kind, kubectl, Kubernetes 1.29+, k9s (terminal UI)
echo "Ensure Minikube / Kind is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: Minikube / Kind](https://kubernetes.io/docs/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A17-01 through A17-05.
2. Terminal execution logs and verification evidence in `submissions/week-17/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-17-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Why Kubernetes exists: challenges of managing containers at production scale.
2. What are the key operational differences between happy-path implementation and production-grade resilience in Kubernetes Fundamentals I?
3. How do you monitor and debug failures occurring within Minikube / Kind?
4. Describe two common security vulnerabilities or misconfigurations associated with Kubernetes control plane architecture: kube-apiserver, etcd, kube-scheduler, kube-controller-manager and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Why Kubernetes exists: challenges of managing containers at production scale and Kubernetes control plane architecture: kube-apiserver, etcd, kube-scheduler, kube-controller-manager. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
