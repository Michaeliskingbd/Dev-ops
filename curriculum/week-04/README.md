# Week 04: Networking Fundamentals II

**Stage 1: Technical Foundations (Days 22-28)**

---

## 1. Week Number and Title
- **Week:** Week 04
- **Title:** Networking Fundamentals II
- **Stage:** Stage 1 — Technical Foundations
- **Timeline:** Days 22 to 28

---

## 2. Learning Objectives
By the end of this week, the learner will be able to:
- Master http/1.1 and http/2 protocol architecture and articulate its operational tradeoffs.
- Master client-server request and response lifecycle and articulate its operational tradeoffs.
- Master tls and ssl encryption, certificate chains, and handshakes and articulate its operational tradeoffs.
- Master reverse proxies and web servers (nginx) and articulate its operational tradeoffs.
- Master load balancing algorithms and health checking and articulate its operational tradeoffs.
- Master host and network firewalls (ufw / iptables basics) and articulate its operational tradeoffs.
- Master network address translation (nat: snat & dnat) and articulate its operational tradeoffs.
- Master ssh key authentication, ssh agent, and secure tunnels and articulate its operational tradeoffs.
- Master network analysis tools: curl, ping, traceroute, dig, nslookup, netstat/ss, tcpdump and articulate its operational tradeoffs.
- Implement robust, production-hardened configurations using curl, ss, tcpdump, Nginx, OpenSSL, ufw, ssh-keygen.
- Methodically diagnose, isolate, and rectify failure modes in live environments.
- Compile clear, professional technical documentation, architecture diagrams, and runbooks.

---

## 3. Prerequisites
Successful completion and mentor sign-off of Week 03.

---

## 4. Why the Topic Matters in DevOps
In enterprise DevOps, mastery of Networking Fundamentals II is critical. DevOps engineers must understand http/1.1 and http/2 protocol architecture and client-server request and response lifecycle to build resilient, automated delivery platforms without relying on magic abstractions or unverified tutorials.

---

## 5. Concepts Explained in Beginner-Friendly Language
### 1. Architectural Foundations of Networking Fundamentals II
Networking Fundamentals II forms a foundational pillar of Technical Foundations. When operating distributed systems at scale, engineers must manage:
- **HTTP/1.1 and HTTP/2 protocol architecture:** Understanding architectural components, state management, and operational boundaries.
- **Client-server request and response lifecycle:** Core configuration patterns, lifecycle handling, and decoupling strategies.
- **TLS and SSL encryption, certificate chains, and handshakes:** Ensuring predictable performance, failure recovery, and adherence to security baselines.

### 2. Deep Dive: Implementation Mechanics
In production environments, curl and ss provide the operational interface. Engineering teams must avoid declarative guesswork:
- Understanding how configuration inputs map to runtime state.
- Inspecting internal networking, socket bindings, storage mounts, and credential injection.
- Ensuring immutable, version-controlled artifacts rather than manual snowflake modifications.

### 3. Production Best Practices & Security
Applying the Principle of Least Privilege (PoLP), strict resource isolation, deterministic version pinning, and automated health verification.

---

## 6. Detailed Daily Learning Plan (Monday–Saturday)
- **Monday (Day 22):** Core conceptual architecture, reading official specifications, and standing up local sandbox environments for curl.
- **Tuesday (Day 23):** Fundamental configuration, command-line interfaces, and executing Assignment A04-01 and A04-02.
- **Wednesday (Day 24):** Deep dive into TLS and SSL encryption, certificate chains, and handshakes, edge cases, and completing Assignment A04-03.
- **Thursday (Day 25):** Production hardening, security controls, automated healthchecks, and completing Assignment A04-04.
- **Friday (Day 26):** Diagnostic methodology, error injection drills, completing Assignment A04-05, running validation scripts, and compiling the weekly report.
- **Saturday (Day 27):** Weekly Practical Engineering Challenge, oral knowledge assessment, and live technical demonstration with the mentor.

---

## 7. Practical Terminal Exercises
```bash
# 1. Environment verification and tooling check
echo "=== Verifying tools for Networking Fundamentals II ==="
which curl || echo "Tool not yet in PATH"

# 2. Inspect active runtime state
# Execute operational discovery commands
date -u +"%Y-%m-%dT%H:%M:%SZ"

# 3. Practical implementation walkthrough
mkdir -p ~/devops-lab/week-04
cd ~/devops-lab/week-04

# 4. Verification and telemetry capture
echo "Ready for Week 04 hands-on labs."
```

---

## 8. Realistic Engineering Scenarios
**Scenario: Production Failure in Networking Fundamentals II**
During a high-traffic deployment, a critical failure occurred involving http/1.1 and http/2 protocol architecture. The team observed intermittent timeouts and service degradation. Inspection revealed misconfigured timeouts, improper socket allocation, and a lack of declarative health checking.
*The DevOps Task:* Systematically diagnose the failure using standard telemetry, isolate the root cause, apply an immutable configuration patch, and document prevention guidelines in a runbook.

---

## 9. Common Mistakes
- **Assuming default configurations are production-safe:** Default timeouts, memory allocations, and open security groups frequently cause outages.
- **Neglecting error handling and exit codes:** Scripts and pipelines that proceed despite underlying command failures create corrupted states.
- **Failing to pin versions:** Using `latest` or unpinned dependency tags leads to non-reproducible builds and sudden breakage.

---

## 10. Troubleshooting Exercises
**Exercise: Diagnosing a Configuration Breakdown in Networking Fundamentals II**
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
# Recommended tooling installation for Networking Fundamentals II
# Tools required: curl, ss, tcpdump, Nginx, OpenSSL, ufw, ssh-keygen
echo "Ensure curl is installed according to the official documentation."
```

---

## 12. Official Documentation and Reliable Learning Resources
- [Official Documentation: curl](https://www.python.org/doc/)
- [DevOps Engineering Guides & Standards](https://sre.google/sre-book/table-of-contents/)

---

## 13. Expected Weekly Deliverables
1. Completed and tested configurations/scripts for Assignments A04-01 through A04-05.
2. Terminal execution logs and verification evidence in `submissions/week-04/`.
3. Solutions for the Saturday Practical Engineering Challenge.
4. Completed Weekly Progress Report in `weekly-reports/week-04-report.md`.

---

## 14. Knowledge-Check Questions
1. Explain the core architectural design and problem solved by HTTP/1.1 and HTTP/2 protocol architecture.
2. What are the key operational differences between happy-path implementation and production-grade resilience in Networking Fundamentals II?
3. How do you monitor and debug failures occurring within curl?
4. Describe two common security vulnerabilities or misconfigurations associated with Client-server request and response lifecycle and how to mitigate them.
5. In a distributed team, how do you ensure changes to this component are peer-reviewed, tested, and tracked in version control?

---

## 15. Weekly Practical Challenge
Design, build, and document an automated, production-hardened solution implementing HTTP/1.1 and HTTP/2 protocol architecture and Client-server request and response lifecycle. The solution must run unattended, include self-healing or health checking, enforce least privilege, and include a Markdown runbook explaining disaster recovery procedures.

---

## 16. Assessment Criteria
Conceptual Understanding: 20 pts | Practical Implementation: 40 pts | Independent Problem Solving: 20 pts | Technical Documentation: 10 pts | Consistency & Completion: 10 pts.

---

## 17. Progression Requirements
Score >= 80/100 on the weekly evaluation rubric, successful demonstration of practical implementation to the mentor, and passing local validation checks.
