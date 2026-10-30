terraform {
  required_version = ">= 1.8.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.40"
    }
  }

  backend "s3" {
    bucket         = "devops-capstone-tfstate-mike-2026"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "devops-capstone-tfstate-locks"
    encrypt        = true
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "DevOps-Capstone-180"
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}
