# Week 03: Networking Fundamentals I

**Stage 1: Technical Foundations (Days 15-21)**

---

## 1. Week Number and Title
- **Week:** Week 03
- **Title:** Networking Fundamentals I
- **Stage:** Stage 1 — Technical Foundations
- **Timeline:** Days 15 to 21

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master computer network architectures and the osi / tcp-ip models and articulate its operational tradeoffs.
- Master ipv4 and ipv6 addressing, subnets and cidr notation and articulate its operational tradeoffs.
- Master public versus private ip address spaces (rfc 1918) and articulate its operational tradeoffs.
- Master mac addresses and address resolution protocol (arp) and articulate its operational tradeoffs.
- Master ports, sockets, and transport layer protocols and articulate its operational tradeoffs.
- Master tcp state machine versus udp characteristics and articulate its operational tradeoffs.
- Master dns hierarchy, record types, and resolution lifecycle and articulate its operational tradeoffs.
- Master dhcp address allocation and articulate its operational tradeoffs.
- Master practical network troubleshooting methodology and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using iproute2 (ip addr, ip route), dig, nslookup, arp, ping, traceroute, netcat (nc).
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 02.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of Networking Fundamentals I is critical. DevOps engineers must understand computer network architectures and the osi / tcp-ip models and ipv4 and ipv6 addressing, subnets and cidr notation to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of Networking Fundamentals I
Networking Fundamentals I forms a foundational pillar of Technical Foundations. When operating distributed systems at scale, engineers must manage:
- **Computer network architectures and the OSI / TCP-IP models:** Understanding architectural components, state management, and operational boundaries.
- **IPv4 and IPv6 addressing, subnets and CIDR notation:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **Public versus private IP address spaces (RFC 1918):** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, iproute2 (ip addr, ip route) and dig provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 15):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for iproute2 (ip addr, ip route).
- **Tuesday (Day 16):** Fundamental configuration, command-line interfaces, and executing Assignment A03-01 and A03-02.
- **Wednesday (Day 17):** Deep dive into Public versus private IP address spaces (RFC 1918), edge cases, and completing Assignment A03-03.
- **Thursday (Day 18):** Production hardening, security controls, automated healthchecks, and completing Assignment A03-04.
- **Friday (Day 19):** Diagnostic methodology, error injection drills, completing Assignment A03-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 20):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for Networking Fundamentals I ==="
which iproute2 || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-03
cd ~/devops-lab/week-03

# 4. Verification and telemetry capture
echo "Ready for Week 03 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in Networking Fundamentals I**
During a high-traffic deployment, a critical failure occurred involving computer network architectures and the osi / tcp-ip models. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in Networking Fundamentals I**
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
# Recommended tooling installation for Networking Fundamentals I
# Tools required: iproute2 (ip addr, ip route), dig, nslookup, arp, ping, traceroute, netcat (nc)
echo "Ensure iproute2 (ip addr, ip route) is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: iproute2 (ip addr, ip route)](https://www.python.org/doc/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A03-01 through A03-05.
2. Terminal execution logs and verification evidence in `submissions/week-03/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-03-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by Computer network architectures and the OSI / TCP-IP models.
2. What are the key operational differences between happy-path implementation and production-grade resilience in Networking Fundamentals I?
3. How do you monitor and debug failures occurring within iproute2 (ip addr, ip route)?
4. Describe two common security vulnerabilities or misconfigurations associated with IPv4 and IPv6 addressing, subnets and CIDR notation and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing Computer network architectures and the OSI / TCP-IP models and IPv4 and IPv6 addressing, subnets and CIDR notation. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
