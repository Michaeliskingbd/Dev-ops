# Amazon Web Services (AWS) Infrastructure

> Practical guide to AWS Global Infrastructure, IAM least privilege, EC2 virtual servers, VPC networking, S3 object storage, and RDS databases.

---

## 1. Verified Official Documentation & Standards
- [AWS Documentation Portal](https://docs.aws.amazon.com/)
- [AWS IAM User Guide & Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Amazon EC2 Linux Instances Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Concepts.html)
- [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/index.html)

---

## 2. Essential CLI & Configuration Cheatsheet
```bash
# AWS CLI Core Operational Commands
aws sts get-caller-identity                # Verify active credentials & IAM role
aws ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId,State.Name,PublicIpAddress]" --output table
aws s3 ls                                  # List S3 buckets
aws rds describe-db-instances              # Inspect RDS database instances
aws cloudwatch get-metric-statistics       # Query metrics
```

---

## 3. Best Practices & Production Guidelines
- **Reproducibility:** Never configure production components manually. All configuration must be committed to Git.
- **Least Privilege:** Restrict permissions, ports, and access tokens to the absolute minimum required.
- **Fail Fast:** Incorporate automated validation and linting in early CI stages.
- **Continuous Observability:** Instrument metrics and structured logs at every tier of the architecture.
