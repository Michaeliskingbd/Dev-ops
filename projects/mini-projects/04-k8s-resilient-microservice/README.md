# Mini-Project 4: Resilient Microservice Deployment on Kubernetes

**Stage:** Stage 3 (Week 19 Milestone)  
**Technologies:** Kubernetes, kubectl, Helm, Ingress, Horizontal Pod Autoscaler (HPA)

## Project Overview
Package, deploy, and scale a containerized application in Kubernetes with zero-downtime rolling updates, persistent storage, and horizontal autoscaling.

## Functional Requirements
1. **Kubernetes Manifests:** Deployments with liveness and readiness probes, resource requests and limits.
2. **Services & Networking:** Internal ClusterIP service exposed via Nginx Ingress Controller with custom path routing.
3. **Config & Secrets:** ConfigMaps for environment configuration and Kubernetes Secrets for sensitive credentials.
4. **Helm Chart:** Package the entire application stack as a parameterized Helm chart with `values.yaml`.
5. **Autoscaling:** Configure Horizontal Pod Autoscaler (HPA) scaling between 2 and 10 pods based on CPU utilization.
