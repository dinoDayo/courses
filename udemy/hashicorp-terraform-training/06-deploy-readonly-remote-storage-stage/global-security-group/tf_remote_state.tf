terraform {
  backend "s3" {
    encrypt                 = true
    bucket                  = "terraform-mystack-tfstate"
    key                     = "global_security_group/terraform.tfstate"
    region                  = "us-east-1"
    profile                 = "default"
    dynamodb_table          = "terraform-state"
    shared_credentials_file = "$HOME/.aws/credentials"
  }
}