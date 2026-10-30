# Programme Progression Gates

Progressing through this programme is strictly competency-based. A learner cannot advance simply because time has elapsed.

There are three mandatory progression gates:
1. **Gate 1:** Technical Foundations (Conclusion of Week 8)
2. **Gate 2:** DevOps Engineering Tools (Conclusion of Week 16)
3. **Gate 3:** Production Engineering and Capstone Defense (Conclusion of Week 24)

---

## 🚪 Progression Gate 1: Technical Foundations (Week 8)

### Required Competencies:
- **Linux Systems:** Create, manage, and audit Linux users, groups, permissions (standard & special bits), processes, systemd services, and journalctl logs.
- **Networking:** Explain and diagram OSI/TCP-IP layers, calculate CIDR subnets, trace DNS resolution from root servers to client, and configure Nginx reverse proxies with SSL.
- **Git & Collaboration:** Manage feature branches, resolve complex merge conflicts without data loss, rebase cleanly, and manage GitHub issues and PRs.
- **Automation:** Write robust Bash scripts with strict mode (`set -euo pipefail`) and Python 3 automation scripts utilizing `subprocess`, `requests`, and JSON/YAML parsing.
- **Backend & Database:** Stand up a RESTful API communicating with a PostgreSQL database, execute relational queries, and manage secrets via environment variables.

### The Gate 1 Evaluation Protocol:
1. **Written Examination (45 minutes):** 20 rigorous conceptual questions covering systems, networking, and SQL. Minimum score: 80%.
2. **Live Troubleshooting Scenario (60 minutes):**
   - The mentor presents an Ubuntu VM with three deliberate faults:
     - Fault A: A broken systemd service failing due to incorrect permissions and missing environment variable.
     - Fault B: A local firewall (UFW) blocking reverse proxy traffic to an internal API.
     - Fault C: A corrupted PostgreSQL configuration preventing network socket binding.
   - The learner must diagnose, explain, and fix all three faults in real-time.
3. **Passing Benchmark:** Minimum 80/100 aggregate score with zero safety violations.

### Remedial Plan for Gate 1 Failure:
- If a learner scores 70–79: 1-week intensive remediation focusing on weak areas, followed by reassessment.
- If a learner scores below 70: Repeat Weeks 6–8 before re-attempting Gate 1.

---

## 🚪 Progression Gate 2: DevOps Engineering Tools (Week 16)

### Required Competencies:
- **Containers:** Author secure, non-root, multi-stage Dockerfiles producing minimal image footprints; orchestrate multi-container apps using Docker Compose with persistent volumes and healthchecks.
- **CI/CD Automation:** Design and implement GitHub Actions workflows with secrets management, matrix testing, automated linting, and image publishing to GHCR.
- **Cloud (AWS):** Provision and configure secure VPCs with public and private subnets, Route Tables, Internet Gateways, NAT Gateways, EC2 instances behind bastion hosts, and Security Groups.
- **Infrastructure as Code (Terraform):** Build modular Terraform configurations, manage remote state with S3 and DynamoDB locking, manage multiple environments, detect drift, and integrate with CI/CD.

### The Gate 2 Evaluation Protocol:
1. **Live Infrastructure Deployment (60 minutes):**
   - From an empty AWS account / local sandbox, execute a clean Terraform deployment provisioning a multi-tier VPC, security groups, and an EC2 instance running a containerized API.
2. **Live Pipeline & Container Troubleshooting (60 minutes):**
   - Injected failure in a GitHub Actions pipeline (e.g., broken test step, failed Docker build cache, or expired credentials).
   - Injected container failure (e.g., database connection timeout, failing healthcheck probe, wrong file permissions in non-root container).
3. **Passing Benchmark:** Minimum 80/100 aggregate score. Zero hardcoded AWS secrets.

### Remedial Plan for Gate 2 Failure:
- If score 70–79: Remediate specific module (Docker, AWS, or Terraform) with 3 additional real-world provisioning labs within 7 days.
- If score below 70: Repeat Weeks 13–16.

---

## 🚪 Progression Gate 3: Production Engineering & Capstone Defense (Week 24)

### Required Competencies:
- **Kubernetes:** Deploy multi-pod applications with Deployments, Services, ConfigMaps, Secrets, PersistentVolumes, Ingress routing, and Horizontal Pod Autoscaling.
- **Observability:** Configure Prometheus and Grafana, deploy Node Exporter, write PromQL queries for error rates and latency, and configure Alertmanager notifications.
- **DevSecOps:** Implement automated container vulnerability scanning with Trivy, lock down IAM policies according to least privilege, and configure TLS/HTTPS.
- **Reliability:** Execute automated database backups, calculate RTO/RPO, conduct chaos failure simulations, and author formal incident post-mortems.
- **Capstone Project:** Successfully defend a production-grade 3-tier cloud deployment built from scratch.

### The Gate 3 Evaluation Protocol:
1. **Capstone Architecture Defense (60 minutes):**
   - 20-minute architecture presentation of the full-stack cloud deployment.
   - 40-minute Socratic defense: the mentor challenges infrastructure choices, cost models, scaling limits, and failure handling.
2. **Chaos & Incident Response Drill (60 minutes):**
   - Mentor injects a live production incident (e.g., killed database pod, simulated DDoS load causing HPA starvation, invalid TLS certificate).
   - Learner must detect the alert, triage the incident, mitigate the failure, restore service, and write a blameless post-mortem.
3. **Passing Benchmark:** Minimum 85/100 score. Unanimous mentor sign-off.
