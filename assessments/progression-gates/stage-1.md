# Progression Gate 1: Technical Foundations (Week 8)

**Gate Milestone:** Transition from Technical Foundations to DevOps Engineering Tools  
**Format:** Written Technical Exam (45 mins) + Live Hands-on Troubleshooting Scenario (60 mins) + Architecture Defense (30 mins)  
**Passing Threshold:** Minimum 80 / 100 aggregate points with zero critical safety violations.

---

## 1. Mandatory Competencies Checklist
To be eligible to sit for Gate 1, the learner must have independently demonstrated:
- [ ] **Linux Administration:** Creation and auditing of users, groups, octal permissions, systemd unit files, process signals, and journalctl analysis.
- [ ] **Networking:** OSI/TCP-IP models, IPv4 subnetting and CIDR math, DNS hierarchy and query tracing, and Nginx reverse proxy configuration.
- [ ] **Git & Collaboration:** Branching models, conflict resolution, interactive rebase, and clean GitHub pull request workflows.
- [ ] **Scripting & Automation:** Writing strict Bash scripts (`set -euo pipefail`) and Python 3 automation scripts using `subprocess`, `requests`, and YAML/JSON parsing.
- [ ] **Databases & APIs:** Standing up a REST API connected to a PostgreSQL database with relational schema definitions and environment configuration.

---

## 2. Gate 1 Examination Structure

### Part A: Systems & Networking Written Examination (20 Points)
20 multiple-part technical questions covering Linux kernel namespaces, TCP state machine, DNS record propagation, and SQL joins.

### Part B: Live Tri-Fault Troubleshooting Examination (50 Points)
The mentor provides an SSH terminal into a broken virtual environment with 3 deliberate failures:
1. **Fault 1 (Linux & systemd):** A system service fails to start due to permission denied on a socket directory and a syntax error in `/etc/systemd/system/app.service`.
2. **Fault 2 (Networking & Security):** An Nginx reverse proxy returns HTTP 502 Bad Gateway because the backend service is listening on `127.0.0.1` while Nginx is routing to the container bridge IP, and UFW is blocking traffic.
3. **Fault 3 (Database Connectivity):** The REST API fails to connect to PostgreSQL due to missing database initialization, wrong credentials in `.env`, and unapplied database migrations.

*The learner must restore the full end-to-end user journey within 60 minutes.*

### Part C: Socratic Architecture Defense (30 Points)
The learner presents the architecture of their Week 8 REST API and PostgreSQL deployment, defending security choices, environment variable isolation, and connection pooling.

---

## 3. Remediation & Reassessment Protocol
- **Score 70–79:** Remedial assignment addressing identified gaps, re-evaluated within 5 days.
- **Score < 70:** Mandatory 2-week curriculum review of Weeks 5–8 before re-attempting Gate 1.
