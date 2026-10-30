# 180-Day / 24-Week DevOps Engineering Roadmap

```mermaid
timeline
    title 180-Day Professional DevOps Engineering Roadmap
    section Stage 1: Technical Foundations
        Week 01 : Linux Foundations I : Distros, FHS, Navigation, Permissions, Users & Groups
        Week 02 : Linux Foundations II : Processes, systemd, apt, SSH, journalctl, Storage
        Week 03 : Networking Foundations I : OSI/TCP-IP, IPv4/CIDR, Subnetting, DNS, Ports
        Week 04 : Networking Foundations II : HTTP/S, TLS, Nginx Reverse Proxy, Firewalls, Wireshark/tcpdump
        Week 05 : Git & GitHub : Branching, Merging vs Rebasing, PRs, Git Hooks, GitHub CLI
        Week 06 : Python Foundations I : Types, Data Structures, Control Flow, Functions, File I/O
        Week 07 : Python & Bash Automation : Subprocess, Requests, JSON/YAML, Bash Scripts, Crontab
        Week 08 : Backend & Databases : REST APIs, HTTP Methods, PostgreSQL, SQL, Client-Server Flow
        Stage 1 Gate : PROGRESSION GATE 1 : Comprehensive Systems, Networking & Database Exam
    section Stage 2: DevOps Engineering Tools
        Week 09 : Docker Fundamentals I : Container Architecture, Dockerfile, Layer Caching, CLI
        Week 10 : Docker Fundamentals II : Docker Compose, Networking, Named Volumes, Multi-Stage Builds
        Week 11 : CI/CD Fundamentals : SDLC, CI Pipelines, Automated Testing, Deployment Strategies
        Week 12 : GitHub Actions : Workflows, Jobs, Secrets, Matrix Builds, GHCR Publishing
        Week 13 : AWS Fundamentals I : IAM Policies, Least Privilege, EC2 Instances, Security Groups
        Week 14 : AWS Fundamentals II : VPC, Public/Private Subnets, NAT Gateways, S3, RDS, Budgets
        Week 15 : Terraform Fundamentals I : IaC Principles, HCL, Providers, State File, Plan & Apply
        Week 16 : Terraform Fundamentals II : Modules, Remote S3 Backend, DynamoDB Lock, Drift Detection
        Stage 2 Gate : PROGRESSION GATE 2 : Cloud Infrastructure & Automated CI/CD Defense
    section Stage 3: Production Engineering & Capstone
        Week 17 : Kubernetes Fundamentals I : Architecture, Control Plane, Pods, Deployments, kubectl
        Week 18 : Kubernetes Fundamentals II : Services (ClusterIP/NodePort), ConfigMaps, Secrets, PV/PVC
        Week 19 : Kubernetes Operations : Ingress Controllers, CoreDNS, HPA Autoscaling, Helm Charts
        Week 20 : Monitoring & Observability : Prometheus, Grafana, Node Exporter, PromQL, Alertmanager
        Week 21 : DevOps Security : DevSecOps, Trivy Container Scanning, Dependency Audits, TLS, SSM
        Week 22 : Reliability & Production Ops : High Availability, Database Backups, Disaster Recovery, RCA
        Week 23 : Capstone Implementation : Architecture Build: React + FastAPI + Postgres on AWS
        Week 24 : Capstone Completion & Final Exam : Production Readiness Review, Chaos Testing, Live Defense
        Stage 3 Gate : PROGRESSION GATE 3 : Final Capstone Defense & Senior Mentor Sign-off
```

---

## Stage Breakdown Matrix

### Stage 1: Technical Foundations (Weeks 1–8)
*Establish the fundamental technical knowledge required to understand how applications, operating systems, networks, and servers work.*

| Week | Focus Area | Core Technologies | Primary Milestone Deliverable |
|:---:|---|---|---|
| **01** | Linux Fundamentals I | Bash, Ubuntu, Coreutils, File Permissions | Hardened multi-user directory tree with permission matrix |
| **02** | Linux Fundamentals II | systemd, journalctl, OpenSSH, apt, storage | Custom daemonized systemd service with automated rotation |
| **03** | Networking Fundamentals I | IPv4, CIDR, Subnetting, DNS, TCP/UDP, ARP | Complete multi-tier enterprise subnet design & DNS audit |
| **04** | Networking Fundamentals II | HTTP/S, TLS, Nginx, UFW, tcpdump, ss | Production Nginx reverse proxy with SSL termination & packet captures |
| **05** | Git and GitHub | Git CLI, GitHub CLI, Rebasing, PRs | Clean repository with resolved merge conflict drill & PR history |
| **06** | Python Fundamentals I | Python 3.12+, Lists/Dicts, File I/O, Exceptions | Robust multi-format log analyzer & metrics parser script |
| **07** | Python & Bash Automation | Subprocess, Requests, PyYAML, Bash, Cron | Automated server health monitoring suite with Slack notifications |
| **08** | Backend & Database Fundamentals | FastAPI, PostgreSQL, SQL, REST APIs, .env | Container-ready REST API integrated with PostgreSQL database |
| **G1** | **Progression Gate 1** | **Comprehensive Systems Defense** | **Live Terminal Systems & Networking Troubleshooting Defense** |

---

### Stage 2: DevOps Engineering Tools (Weeks 9–16)
*Develop practical competence in containers, automated delivery, cloud infrastructure, and infrastructure as code.*

| Week | Focus Area | Core Technologies | Primary Milestone Deliverable |
|:---:|---|---|---|
| **09** | Docker Fundamentals I | Docker Engine, Dockerfiles, Layer Caching | Non-root production container image (<50MB) with dive analysis |
| **10** | Docker Fundamentals II | Docker Compose, Networks, Volumes, Healthchecks | Complete 3-tier containerized stack with health checking |
| **11** | CI/CD Fundamentals | CI Principles, Testing Strategies, Artifacts | Comprehensive automated testing and delivery architecture spec |
| **12** | GitHub Actions | Workflows, Runners, Secrets, GHCR, OIDC | Automated CI pipeline with test matrix and GHCR image publish |
| **13** | AWS Fundamentals I | IAM, EC2, Security Groups, SSH Bastion | Securely deployed Linux server on AWS EC2 behind a bastion host |
| **14** | AWS Fundamentals II | VPC, Subnets, NAT Gateway, S3, RDS, CloudWatch | Production-grade 2-tier AWS VPC network with RDS database |
| **15** | Terraform Fundamentals I | HCL, AWS Provider, State File, Plan/Apply | Declarative AWS VPC and compute infrastructure via Terraform |
| **16** | Terraform Fundamentals II | Modules, Remote S3 Backend, DynamoDB, Drift | Reusable modular Terraform suite with state locking and CI check |
| **G2** | **Progression Gate 2** | **Cloud & CI/CD Defense** | **Live Automated Cloud Provisioning & Broken Pipeline Debugging** |

---

### Stage 3: Production Engineering and Capstone (Weeks 17–24)
*Develop the ability to operate, secure, observe, troubleshoot, and document deployed systems in production.*

| Week | Focus Area | Core Technologies | Primary Milestone Deliverable |
|:---:|---|---|---|
| **17** | Kubernetes Fundamentals I | Kubernetes Architecture, Pods, Deployments, kubectl | Resilient self-healing Deployment manifests deployed locally |
| **18** | Kubernetes Fundamentals II | Services, ConfigMaps, Secrets, PV/PVC, Probes | Stateful 3-tier application deployment with persistent storage |
| **19** | Kubernetes Operations | Ingress, CoreDNS, HPA, Rolling Updates, Helm | Custom Helm chart with automated horizontal autoscaling |
| **20** | Monitoring & Observability | Prometheus, Grafana, Node Exporter, Alertmanager | Production observability dashboard with custom alerting rules |
| **21** | DevOps Security | DevSecOps, Trivy, pip-audit, AWS SSM, PoLP | Hardened infrastructure with zero HIGH/CRITICAL vulnerabilities |
| **22** | Reliability & Production Ops | High Availability, Backup/Restore, RTO/RPO, RCA | Automated database backup script, chaos drill, and post-mortem report |
| **23** | Capstone Implementation | Full Stack (React + FastAPI + Postgres), AWS, IaC | Fully provisioned production deployment via automated pipeline |
| **24** | Capstone Defense & Exam | Production Readiness Review, Chaos Drills, Defense | Live Mentor Architecture Defense & Final Comprehensive Examination |
| **G3** | **Progression Gate 3** | **Final Capstone Defense** | **Formal Sign-off & Junior DevOps Graduation** |
