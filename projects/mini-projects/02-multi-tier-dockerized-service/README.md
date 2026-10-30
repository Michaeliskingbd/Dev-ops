# Mini-Project 2: Multi-Tier Containerized Application Architecture

**Stage:** Stage 2 (Week 10 Milestone)  
**Technologies:** Docker, Docker Compose, Python FastAPI, PostgreSQL, Nginx

## Project Overview
Containerize a 3-tier web service consisting of an Nginx reverse proxy, a Python FastAPI REST backend, and a PostgreSQL database.

## Functional Requirements
1. **Multi-Stage Dockerfile:** Backend Dockerfile using multi-stage build, non-root user, and image size < 80MB.
2. **Docker Compose Orchestration:**
   - Isolated internal bridge network `backend-tier` (Postgres and API only).
   - Public bridge network `frontend-tier` (Nginx and API only).
   - Database credentials passed via `.env` file (never hardcoded).
   - Healthcheck on PostgreSQL ensuring API container waits for database readiness before starting.
   - Named volume for persistent database storage across container restarts.
