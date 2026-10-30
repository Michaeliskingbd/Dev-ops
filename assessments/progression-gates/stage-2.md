# Progression Gate 2: DevOps Engineering Tools (Week 16)

**Gate Milestone:** Transition from Tooling to Production Engineering & Capstone  
**Format:** Live Cloud Provisioning (60 mins) + Pipeline Debugging (60 mins) + IaC Defense (30 mins)  
**Passing Threshold:** Minimum 80 / 100 aggregate points. Zero committed secrets.

---

## 1. Mandatory Competencies Checklist
- [ ] **Containers:** Authoring hardened, non-root multi-stage Dockerfiles and Docker Compose 3-tier architectures with persistent volumes and healthchecks.
- [ ] **CI/CD:** Designing GitHub Actions workflows with secrets management, matrix testing, and automated GHCR image publishing.
- [ ] **AWS Cloud:** Provisioning VPCs, subnets, route tables, security groups, EC2 instances, and RDS databases following security baselines.
- [ ] **Terraform (IaC):** Writing modular Terraform, managing remote state with S3 and DynamoDB locking, detecting drift, and zero hardcoded secrets.

---

## 2. Gate 2 Examination Structure

### Part A: Live Modular Cloud Deployment (40 Points)
The learner is given an empty cloud sandbox and must execute a clean Terraform apply that provisions:
- A custom VPC with public and private subnets across two Availability Zones.
- An EC2 bastion host and an EC2 application server running a containerized microservice.
- Secure Security Groups allowing only necessary traffic.

### Part B: Broken CI/CD Pipeline & Container Debugging (40 Points)
The mentor injects failures into a GitHub Actions workflow:
- A broken automated test suite caused by environment variable mismatch.
- A failed Docker build caused by incorrect layer caching and missing build arguments.
- A failed deployment step due to IAM permission denial.

*The learner must diagnose the pipeline logs, apply fixes, and achieve a green build.*

### Part C: Terraform State & Security Defense (20 Points)
Oral defense explaining state locking, drift detection, and the consequences of manual changes.
