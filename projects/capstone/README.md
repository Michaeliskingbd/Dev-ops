# DevOps Engineering Capstone Project: Production Cloud Platform

> **A comprehensive, portfolio-worthy DevOps capstone project demonstrating end-to-end cloud infrastructure, CI/CD automation, container orchestration, telemetry, and site reliability.**

---

## 🎯 Capstone System Architecture

```text
                                  Internet
                                     │
                             [ Route 53 / DNS ]
                                     │
                             [ Nginx Proxy / TLS ]
                                     │
               ┌─────────────────────┴─────────────────────┐
               ▼                                           ▼
       [ Frontend Web UI ]                       [ FastAPI REST API ]
       (React / Static Nginx)                    (Python / Multi-Stage)
                                                           │
                                             ┌─────────────┴─────────────┐
                                             ▼                           ▼
                                    [ PostgreSQL RDS / DB ]     [ Prometheus & Grafana ]
                                    (Encrypted, Multi-AZ)       (Telemetry & Alerts)
```

---

## 📋 Capstone Requirements & Deliverables

1. **Application Layer (`app/`):**
   - Simple responsive Web UI frontend.
   - Production FastAPI backend providing CRUD endpoints and `/healthz` & `/metrics`.
   - PostgreSQL relational database with automated migrations.
2. **Containerization:**
   - Multi-stage Dockerfiles for both frontend and backend.
   - Non-root user execution, hardened attack surface.
   - Local integration testing via Docker Compose.
3. **Infrastructure as Code (`terraform/`):**
   - Modular Terraform provisioning AWS VPC, Subnets, EC2, RDS, and Security Groups.
   - Remote state stored in S3 with DynamoDB locking.
4. **CI/CD Pipeline (`.github/workflows/`):**
   - Automated linting, testing, Docker image building, and GHCR container publishing.
   - Automated deployment pipeline with manual approval gates.
5. **Observability Stack (`monitoring/`):**
   - Prometheus scraping application and infrastructure metrics.
   - Grafana dashboard visualizing latency, throughput, error rates, and CPU/RAM.
   - Alertmanager rules for high error rates and host degradation.
6. **Production Runbooks & Documentation:**
   - Architecture specification, deployment runbook, and disaster recovery plan.
