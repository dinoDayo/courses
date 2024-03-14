## Resources
- credentials management:
```
As a fallback for the other ways of defining variables, 
Terraform searches the environment of its own process 
for environment variables named TF_VAR_ followed by 
the name of a declared variable.
```
- see documentation [here](https://developer.hashicorp.com/terraform/language/values/variables#variable-definition-precedence) for a more verbose explination of how credentials are passed to Terraform.
- template for this proof of concept pulled from [here](https://nahidsaikat.medium.com/stream-data-to-s3-using-kinesis-and-firehose-with-terraform-7ed2e25310c).
- template for kinesis config pulled from [here](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/kinesis_firehose_delivery_stream.html)
- terraform deploy workflow:
```
1. install terraform (https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
2. terraform init
3. terraform plan
4. terraform apply
```
- terraform remove workflow: `terraform destroy`