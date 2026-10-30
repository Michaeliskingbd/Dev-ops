# Terraform Infrastructure as Code (IaC)

> Comprehensive reference for declarative infrastructure, HCL syntax, AWS provider, state file management, remote S3 locking, and reusable modules.

---

## 1. Verified Official Documentation & Standards
- [HashiCorp Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
- [Terraform AWS Provider Registry](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Terraform Best Practices Guide](https://www.terraform-best-practices.com/)
- [TFLint - Pluggable Terraform Linter](https://github.com/terraform-linters/tflint)

---

## 2. Essential CLI & Configuration Cheatsheet
```bash
# Terraform Core Lifecycle Workflow
terraform init                             # Initialize providers and backend
terraform fmt -check                       # Validate canonical code formatting
terraform validate                         # Validate syntax and configuration schema
terraform plan -out=tfplan                 # Generate speculative execution plan
terraform apply tfplan                     # Apply execution plan to cloud
terraform destroy -auto-approve            # Tear down all provisioned resources
```

---

## 3. Best Practices & Production Guidelines
- **Reproducibility:** Never configure production components manually. All configuration must be committed to Git.
- **Least Privilege:** Restrict permissions, ports, and access tokens to the absolute minimum required.
- **Fail Fast:** Incorporate automated validation and linting in early CI stages.
- **Continuous Observability:** Instrument metrics and structured logs at every tier of the architecture.
