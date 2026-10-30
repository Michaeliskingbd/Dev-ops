# Mentor Answer Key: Progression Gates 1, 2, and 3

> **CONFIDENTIAL — MENTOR EVALUATION PROTOCOL**

---

## Gate 1 (Week 8) Evaluation Key: Technical Foundations
1. **Systems Exam:** Learner must distinguish process signals (`SIGTERM` vs `SIGKILL`), explain `/proc` mechanics, and diagram the TCP 3-way handshake.
2. **Live Injected Fault 1 (systemd service crash):**
   - Root cause: Missing executable bit on script and wrong group ownership on log directory.
   - Learner must inspect `journalctl -u <service>`, run `chmod +x`, and fix ownership with `chown`.
3. **Live Injected Fault 2 (Nginx 502 Bad Gateway):**
   - Root cause: Nginx upstream configured for `127.0.0.1:8000` while backend service is bound to `127.0.0.1:8080`.
   - Learner must inspect Nginx `/var/log/nginx/error.log` and verify listening ports using `ss -tulpn`.
4. **Live Injected Fault 3 (PostgreSQL connection refusal):**
   - Root cause: `listen_addresses` in `postgresql.conf` set to `localhost` while client attempts connection over bridge IP, or missing entry in `pg_hba.conf`.

---

## Gate 2 (Week 16) Evaluation Key: DevOps Engineering Tools
1. **Terraform Live Provisioning:**
   - Verify that Terraform code uses remote backend with S3 and DynamoDB state locking.
   - Verify that security groups do not have `0.0.0.0/0` ingress on SSH (port 22) except through a bastion host or restricted IP.
2. **CI/CD Pipeline Failure Drill:**
   - Root cause: Broken test fixture or missing secret in GitHub Actions secrets.
   - Learner must inspect GitHub Actions workflow run logs, diagnose the step failure, and fix the configuration.

---

## Gate 3 (Week 24) Evaluation Key: Production & Capstone Defense
1. **Live Chaos Simulation:**
   - Terminate the database container/pod while running load tests.
   - Verify that the application backend handles reconnection gracefully without crashing permanently.
2. **Architecture Defense Interrogation:**
   - Challenge learner on cost tradeoffs: "Why RDS PostgreSQL rather than hosting Postgres on EC2?"
   - Challenge on security: "How do you rotate database credentials without zero-downtime service interruption?"
