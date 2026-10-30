# Programme Security & Financial Protection Policy

DevOps engineers hold the keys to production infrastructure. Practicing rigorous security and financial discipline starts on Day 1.

---

## 1. Secrets & Credentials Management

### Absolute Prohibitions:
- **NEVER** commit `.env`, `.pem`, `.key`, `id_rsa`, or credentials files to Git.
- **NEVER** hardcode passwords, tokens, or secret keys in Dockerfiles, Terraform manifests, or application code.
- **NEVER** paste cloud credentials into public pastebins, issue trackers, or chat channels.

### Mandatory Safeguards:
- Always ensure `.gitignore` contains rules for sensitive files before running `git add`.
- Use environment variables or secret managers (AWS SSM Parameter Store / Secrets Manager).
- In GitHub Actions, always use GitHub Encrypted Secrets (`${{ secrets.AWS_ACCESS_KEY_ID }}`) and never echo secrets in workflow logs.

```bash
# Verify your staging area before committing:
git diff --cached
```

---

## 2. Cloud Cost Safety & Free-Tier Discipline

Cloud computing can incur severe financial liabilities if misconfigured.

### Mandatory Cost Controls:
1. **Zero-Spend Default:** All exercises in Weeks 1–12 use local virtualization (Docker, Linux namespaces, local PostgreSQL).
2. **Billing Alarm Setup:** On Day 1 of AWS (Week 13), the learner must configure an AWS CloudWatch Billing Alarm with a threshold of **\$5.00 USD**.
3. **Resource Sizing:**
   - Always use `t3.micro` or `t2.micro` EC2 instances (Free Tier eligible).
   - Use `db.t3.micro` for Amazon RDS.
   - Use standard GP3 EBS storage volumes <= 20 GB.
4. **Daily Teardown Rule:**
   - At the conclusion of every study session involving AWS or Terraform:
     ```bash
     terraform destroy -auto-approve
     ```
   - Verify in the AWS Management Console that all EC2 instances, RDS databases, NAT Gateways, and Elastic IPs have been terminated or released.
5. **NAT Gateway Warning:**
   - AWS NAT Gateways cost ~$32/month base fee. In lab exercises, NAT Gateways must be created, tested, and destroyed within the same 2-hour session, or a lightweight EC2 NAT Instance must be used instead.

---

## 3. Incident Escalation Protocol

If you suspect an AWS access key or secret has been committed:
1. **Rotate / Invalidate immediately:** Log into the AWS Console -> IAM -> Users -> Security Credentials -> Deactivate / Delete Access Key.
2. **Notify your mentor:** Send an immediate alert so the mentor can audit CloudTrail activity.
3. **Scrub Git History:** Do not merely delete the file in a new commit. The secret remains in Git history. Rewrite history using `git-filter-repo`.
