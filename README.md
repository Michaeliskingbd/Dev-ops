# 180-Day (24-Week) Professional DevOps Engineering Mentorship Programme

> **A rigorous, competency-based engineering curriculum taking learners from Linux & networking foundations to production-grade cloud infrastructure, CI/CD automation, Kubernetes, observability, and full-stack capstone delivery.**

---

## 🎯 Programme Manifesto

DevOps is not a set of disjointed tools. It is the disciplined intersection of systems engineering, automation, network architecture, security, and site reliability. 

This 180-day (24-week) programme is designed for aspiring engineers who may have limited development experience and zero prior professional DevOps experience. **This is not a crash course.** It prioritises deep architectural comprehension, practical terminal mastery, rigorous troubleshooting, and demonstrable competence over superficial check-the-box completions.

```
Stage 1: Technical Foundations (Weeks 01–08)
  └── Linux, Networking, Git, Python, Bash Automation, Backend & Database
        ▼
   [ PROGRESSION GATE 1: Core Systems Engineering Sign-Off ]
        ▼
Stage 2: DevOps Engineering Tools (Weeks 09–16)
  └── Docker, Multi-Container Orchestration, CI/CD, GitHub Actions, AWS, Terraform
        ▼
   [ PROGRESSION GATE 2: Cloud & Infrastructure Automation Sign-Off ]
        ▼
Stage 3: Production Engineering & Capstone (Weeks 17–24)
  └── Kubernetes, Observability, DevSecOps, SRE & Reliability, Capstone Delivery
        ▼
   [ PROGRESSION GATE 3 & FINAL MENTOR DEFENSE ]
```

---

## 🧭 Repository Architecture

```text
devops-180-days/
├── .github/                      # Issue templates, PR templates, and validation workflows
│   ├── ISSUE_TEMPLATE/           # Assignment, weekly report, assessment, and blocker forms
│   ├── PULL_REQUEST_TEMPLATE.md  # Standard pull request verification template
│   └── workflows/                # Submission validation, Markdown linting, weekly reminders
├── programme/                    # Programme philosophy, roadmap, schedule, and gates
│   ├── roadmap.md                # 24-week visual and milestone roadmap
│   ├── weekly-schedule.md        # Hour-by-hour weekly operating schedule
│   ├── progression-gates.md      # Detailed criteria for Gates 1, 2, and 3
│   └── learning-expectations.md  # Engineering mindset and troubleshooting protocol
├── curriculum/                   # Complete weekly technical curriculum (Weeks 01–24)
│   ├── week-01/ to week-24/      # 17 required technical sections per week
├── assignments/                  # 120 practical engineering assignments (5 per week)
│   ├── week-01/ to week-24/      # Hands-on implementation specs
├── assessments/                  # Assessment rubrics and examination criteria
│   ├── weekly/                   # 100-point weekly rubrics & troubleshooting tasks
│   ├── progression-gates/        # Formal Stage 1, Stage 2, and Stage 3 evaluations
│   └── final/                    # Final Capstone Defense and comprehensive examination
├── submissions/                  # Learner work repository organized by week
│   ├── week-01/ to week-24/      # Submitted code, configurations, logs, and screenshots
├── weekly-reports/               # Structured weekly progress reports
│   ├── template.md               # 15-point mandatory weekly reporting template
│   └── README.md                 # Submission and evidence collection standards
├── projects/                     # Hands-on projects portfolio
│   ├── mini-projects/            # 4 intermediate milestone projects
│   └── capstone/                 # Complete 3-tier production application & cloud infra
├── mentor/                       # Mentor supervision playbook and resources
│   ├── mentor-guide.md           # Mentor cadence, questioning, and review standards
│   ├── review-process.md         # Pull request review protocol and grading workflow
│   ├── assessment-rubric.md      # Master competency rubric and grading tiers
│   ├── answer-keys/              # Reference implementations, outputs, and keys (mentor-only)
│   └── progress-dashboard.md     # Real-time learner tracking dashboard
├── resources/                    # Curated, verified documentation and cheat-sheets
│   ├── linux.md, networking.md, python.md, backend.md, docker.md, cicd.md,
│   └── aws.md, terraform.md, kubernetes.md, monitoring.md, security.md
└── scripts/                      # Automation tooling for learners and mentors
    ├── validate_submission.py    # Automated submission and report validator
    ├── generate_progress.py      # Structured progress dashboard generator
    └── setup_github.py           # GitHub CLI initialization for milestones, labels, issues
```

---

## 📅 24-Week Curriculum Matrix

| Week | Stage | Topic | Focus Areas | Key Deliverable |
|:---:|:---:|---|---|---|
| **01** | Stage 1 | Linux Fundamentals I | Distros, terminal, FHS, permissions, users/groups | Multi-user Linux environment & permission audit |
| **02** | Stage 1 | Linux Fundamentals II | Processes, systemd, package management, SSH, storage | Custom systemd service & automated log audit |
| **03** | Stage 1 | Networking Fundamentals I | OSI/TCP-IP, IPv4/IPv6, CIDR, ports, TCP/UDP, DNS | Multi-subnet network architecture & DNS trace |
| **04** | Stage 1 | Networking Fundamentals II | HTTP/S, TLS, Nginx reverse proxy, firewalls, packet analysis | Secure Nginx reverse proxy & packet captures |
| **05** | Stage 1 | Git and GitHub | Commits, branching, rebase, conflicts, PRs, GH CLI | Conflict resolution repo & contribution workflow |
| **06** | Stage 1 | Python Fundamentals I | Types, collections, control flow, functions, file I/O | Log parsing and system metric utility in Python |
| **07** | Stage 1 | Python & Bash Automation | Subprocess, requests, JSON/YAML, Bash scripts, cron | Automated system health monitor & slack notifier |
| **08** | Stage 1 | Backend & Database Fundamentals | REST APIs, HTTP codes, PostgreSQL, SQL queries, .env | Deployed REST API connected to PostgreSQL |
| **GATE 1** | **STAGE 1 PROGRESSION GATE** | **Comprehensive Systems Engineering Defense & Hands-On Exam** | |
| **09** | Stage 2 | Docker Fundamentals I | Namespaces/cgroups, Dockerfile, layer cache, CLI | Hardened non-root microservice Docker image |
| **10** | Stage 2 | Docker Fundamentals II | Docker Compose, bridge networks, volumes, healthchecks | 3-tier containerized stack (Web + API + DB) |
| **11** | Stage 2 | CI/CD Fundamentals | SDLC, CI principles, automated testing, deployment patterns | Automated test & lint pipeline architecture |
| **12** | Stage 2 | GitHub Actions | Workflows, jobs, runners, secrets, GHCR image push | Production CI pipeline publishing to GHCR |
| **13** | Stage 2 | AWS Fundamentals I | IAM, policies, EC2, security groups, key pairs, bastion | Hardened EC2 application host with bastion |
| **14** | Stage 2 | AWS Fundamentals II | VPC, public/private subnets, IGW, NAT, S3, RDS, Budgets | High-availability 2-tier AWS VPC network |
| **15** | Stage 2 | Terraform Fundamentals I | IaC principles, HCL, providers, resources, state, plan/apply | Modular VPC & EC2 provisioned via Terraform |
| **16** | Stage 2 | Terraform Fundamentals II | Modules, remote S3/DynamoDB state, environments, drift | Production Terraform module suite with remote lock |
| **GATE 2** | **STAGE 2 PROGRESSION GATE** | **Cloud Infrastructure & Automated Delivery Defense** | |
| **17** | Stage 3 | Kubernetes Fundamentals I | Architecture, Pods, Deployments, ReplicaSets, kubectl | Resilient self-healing Deployment in local cluster |
| **18** | Stage 3 | Kubernetes Fundamentals II | Services, ConfigMaps, Secrets, PV/PVC, health probes | Stateful 3-tier microservice deployed on K8s |
| **19** | Stage 3 | Kubernetes Operations | Ingress, CoreDNS, HPA autoscaling, rolling updates, Helm | Helm chart packaging & zero-downtime rollout |
| **20** | Stage 3 | Monitoring & Observability | Prometheus, Node Exporter, Grafana dashboards, Alertmanager | Production telemetry stack & alert routing |
| **21** | Stage 3 | DevOps Security | DevSecOps, least privilege, Trivy scanning, TLS, SSM | Security audit, container scanning & secrets vault |
| **22** | Stage 3 | Reliability & Production Ops | High availability, backups, RTO/RPO, disaster recovery, RCA | Backup automation, chaos drill & RCA incident report |
| **23** | Stage 3 | Capstone Implementation | Architecture build: React + FastAPI + Postgres on AWS | Live end-to-end cloud deployment via CI/CD |
| **24** | Stage 3 | Capstone Completion & Final Exam | Production readiness review, chaos injection, defense | Capstone Defense & Comprehensive Technical Exam |
| **GATE 3** | **STAGE 3 PROGRESSION GATE** | **Final Capstone Defense & Senior Mentor Sign-off** | |

---

## ⏱️ Sustainable Weekly Operating Rhythm

Success in this programme requires consistent, disciplined practice rather than sporadic cramming.

```text
┌─────────────────┬────────────────────────────────────────────────────────┐
│ Days            │ Structured Activity                                    │
├─────────────────┼────────────────────────────────────────────────────────┤
│ Monday – Friday │ • 60–90 min:  Deep technical study & documentation     │
│ (3–4 hrs / day) │ • 90–120 min: Hands-on implementation in terminal/IDE  │
│                 │ • 30 min:     Documentation, commit, daily reflection  │
├─────────────────┼────────────────────────────────────────────────────────┤
│ Saturday        │ • Practical Engineering Challenge                      │
│ (2–3 hrs)       │ • Weekly Knowledge Assessment                          │
│                 │ • Live Mentor Demonstration & Troubleshooting Task     │
├─────────────────┼────────────────────────────────────────────────────────┤
│ Sunday          │ • Mandatory Rest & Recharging                          │
│                 │ • Optional light review; zero mandatory assignments    │
└─────────────────┴────────────────────────────────────────────────────────┘
```

---

## ⚖️ Assessment & Progression Policy

Every week is evaluated out of **100 points**:

- **Conceptual Understanding (20 pts):** Explaining architecture, protocols, and tradeoffs in plain engineering language.
- **Practical Implementation (40 pts):** Building working, clean, and idiomatic configurations, scripts, or infrastructure.
- **Independent Problem Solving (20 pts):** Diagnosing injected failures, debugging logs, and resolving errors methodically.
- **Documentation (10 pts):** Producing clear architecture diagrams, READMEs, reproduction steps, and runbooks.
- **Consistency & Completion (10 pts):** On-time submission, clean Git commits, and structured weekly reporting.

### Scoring Thresholds
- **80 – 100:** Full Pass (qualifies for progression, provided all critical practical requirements pass).
- **70 – 79:** Conditional Pass (specific remedial exercises required within 7 days).
- **Below 70:** Unsatisfactory (requires curriculum review and formal reassessment).

> [!IMPORTANT]
> Advancing across Progression Gates (End of Week 8, Week 16, and Week 24) is **never automatic**. Progression requires active demonstration of technical mastery before a mentor.

---

## 🚀 Quick Start for Learners

1. **Clone or Fork the Repository:**
   ```bash
   git clone https://github.com/your-org/devops-180-days.git
   cd devops-180-days
   ```
2. **Review the Core Policies:**
   - Read [PROGRAMME_OVERVIEW.md](programme/roadmap.md)
   - Read [LEARNING_RULES.md](LEARNING_RULES.md)
   - Read [SECURITY_POLICY.md](SECURITY_POLICY.md)
   - Read [ASSESSMENT_POLICY.md](ASSESSMENT_POLICY.md)
3. **Set Up Your Working Branch:**
   ```bash
   git checkout -b submissions/week-01
   ```
4. **Begin Week 01:**
   - Navigate to [curriculum/week-01/README.md](curriculum/week-01/README.md)
   - Complete the assignments in [assignments/week-01/](assignments/week-01/)
   - Place your work in `submissions/week-01/`
   - Validate your submissions locally using `python scripts/validate_submission.py --week 1`
   - Submit your Pull Request according to [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🛡️ Cloud Safety & Financial Protection

We enforce strict cloud safety protocols:
- **Local-First:** Docker, Kubernetes (Kind/Minikube), and databases are mastered locally before touching the cloud.
- **Zero Surprise Bills:** AWS Budgets with \$5.00 hard alert thresholds are configured in Week 13 before provisioning resources.
- **Mandatory Teardown:** Every cloud assignment requires running `terraform destroy` or manual cleanup commands documented in the assignment.
- **Zero Committed Secrets:** Git pre-commit hooks and GitHub Actions secret scanners reject accidental credential commits.

---

## 📜 Code of Conduct & Contribution

Refer to [CONTRIBUTING.md](CONTRIBUTING.md) for contribution workflows and [LEARNING_RULES.md](LEARNING_RULES.md) for rules on AI assistance, academic honesty, and peer review.
