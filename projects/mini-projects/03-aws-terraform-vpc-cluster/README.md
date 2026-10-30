# Mini-Project 3: Modular AWS VPC & Compute Cluster via Terraform

**Stage:** Stage 2 (Week 16 Milestone)  
**Technologies:** Terraform, AWS (VPC, Subnets, EC2, Bastion, Security Groups), S3 Remote State

## Project Overview
Provision a secure, multi-tier AWS network and compute cluster using modular Terraform, with remote state locking in S3 and DynamoDB.

## Functional Requirements
1. **VPC Architecture:** Custom VPC (`10.0.0.0/16`) spanning 2 Availability Zones with 2 public subnets, 2 private application subnets, and 2 database subnets.
2. **Egress & Ingress:** Internet Gateway for public traffic, NAT Gateway for outbound traffic from private subnets.
3. **Compute:** EC2 Bastion host in public subnet; EC2 Application server in private subnet accessible only via Bastion SSH.
4. **Security Groups:** Strictly scoped inbound and outbound rules adhering to the Principle of Least Privilege.
5. **State Management:** Remote S3 backend with AES256 encryption and DynamoDB state locking.
