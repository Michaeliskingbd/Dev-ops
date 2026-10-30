# Docker & Container Engineering

> Essential guide for containerization, Dockerfile multi-stage builds, UnionFS layer optimization, Docker Compose architectures, and security.

---

## 1. Verified Official Documentation & Standards
- [Docker Engine Official Documentation](https://docs.docker.com/engine/)
- [Dockerfile Best Practices Guide](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Compose Specification](https://docs.docker.com/compose/)
- [Hadolint - Dockerfile Linter](https://github.com/hadolint/hadolint)

---

## 2. Essential CLI & Configuration Cheatsheet
```dockerfile
# Multi-stage production build pattern
FROM python:3.12-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.12-slim AS runtime
WORKDIR /app
RUN groupadd -g 1001 appgroup && useradd -u 1001 -g appgroup -s /bin/sh appuser
COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appgroup . .
ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 3. Best Practices & Production Guidelines
- **Reproducibility:** Never configure production components manually. All configuration must be committed to Git.
- **Least Privilege:** Restrict permissions, ports, and access tokens to the absolute minimum required.
- **Fail Fast:** Incorporate automated validation and linting in early CI stages.
- **Continuous Observability:** Instrument metrics and structured logs at every tier of the architecture.
