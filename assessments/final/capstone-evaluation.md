# Capstone Project Evaluation Rubric

| Evaluation Area | Max Points | Passing Bar | Detailed Criteria |
|---|:---:|:---:|---|
| **1. Architecture Design & IaC** | 15 | 12 | Modular Terraform code, clean VPC design, secure IAM policies, remote state locking. |
| **2. Containerization & Multi-Stage Builds** | 10 | 8 | Non-root containers, multi-stage Dockerfiles, minimal attack surface (<50MB image). |
| **3. CI/CD Automation** | 15 | 12 | Automated linting, testing, image building, GHCR publishing, and deployment gates in GitHub Actions. |
| **4. Database & Persistence** | 10 | 8 | Automated schema migrations, connection pooling, persistent storage, and automated backup scripts. |
| **5. Reverse Proxy & HTTPS** | 10 | 8 | Nginx reverse proxy with valid TLS/SSL certificates, HTTP/2, and security headers. |
| **6. Observability & Telemetry** | 15 | 12 | Prometheus metrics collection, Grafana dashboards, application health probes, and Alertmanager routing. |
| **7. Security & Hardening** | 10 | 8 | Zero committed secrets, Trivy scan with zero HIGH/CRITICAL CVEs, least privilege security groups. |
| **8. Reliability & Failure Handling** | 5 | 4 | Graceful container shutdown (SIGTERM), restart policies, and healthcheck probes. |
| **9. Documentation & Runbooks** | 5 | 4 | Complete README, architecture diagram, deployment runbook, and disaster recovery plan. |
| **10. Live Defense & Troubleshooting** | 5 | 4 | Able to explain all design decisions, modify code on demand, and handle simulated failures. |
| **Total** | **100** | **85** | **Minimum Passing Benchmark: 85 / 100** |
