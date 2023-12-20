terraform {
    backend "s3" {
        encrypt = true
        bucket = "terraform-mystack-tfstate"
        key="deploy-multiple-webserver-locking/terraform.tfstate"
        region = "us-east-1"
    }
}