# DevSecOps & Cloud Infrastructure Security

> Reference guide for the Principle of Least Privilege, container vulnerability scanning with Trivy, IAM policy hardening, secrets isolation, and TLS.

---

## 1. Verified Official Documentation & Standards
- [OWASP DevSecOps Guideline](https://owasp.org/www-project-devsecops-guideline/)
- [Trivy Vulnerability Scanner Documentation](https://aquasecurity.github.io/trivy/)
- [Center for Internet Security (CIS) Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [Let's Encrypt / Certbot Documentation](https://certbot.eff.org/)

---

## 2. Essential CLI & Configuration Cheatsheet
```bash
# Security & Vulnerability Scanning
trivy image --severity HIGH,CRITICAL myapp:v1.0.0    # Scan Docker image for CVEs
pip-audit                                            # Audit Python dependencies
git-secrets --scan                                   # Scan git repo for committed secrets
checkov -d ./terraform                               # Static analysis of IaC for security misconfigs
```

---

## 3. Best Practices & Production Guidelines
- **Reproducibility:** Never configure production components manually. All configuration must be committed to Git.
- **Least Privilege:** Restrict permissions, ports, and access tokens to the absolute minimum required.
- **Fail Fast:** Incorporate automated validation and linting in early CI stages.
- **Continuous Observability:** Instrument metrics and structured logs at every tier of the architecture.
