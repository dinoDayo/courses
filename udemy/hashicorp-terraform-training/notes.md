# Notes from lectures

### Sections 1-2 notes... (deploy-single-server)
- Syntax for resource declaration: `resource "PROVIDER_TYPE" "NAME" { [CONFIG..] }`
- `terraform plan`: dry-run cmd to validate a given terraform plan
- `terraform apply`: applies logic in a given terraform plan.
- `terraform destroy`: removes resources created from a terraform apply execution

### Section 3 notes... (Deploy; from single servers to multiple)
- Interpolation is useful for accessing variable values, resource outputs, and resource attributes. The sytanx is simple; `${provider_resource-type.identifier.attribute}`, for example: `${aws_instance.my_ec2.id}`.
- A more verbose example:
    - Given a resource declaration: `resource "aws_security_group" "webserver_sg" { Ingress{...} Egress{...} }`
    - Referencing the resource declaration via interpolation: `resource "aws_instance" "My-Webserver" { vpc_security_group_ids = ["${aws_security_group.webserver_sg.id}"]}`
- `user_data` is an Amazon Web Service resource that allows us to execute an installation script on an ec2 instance once the instance is up and running.
- Variables / Resources declared in any `filename.tf` files can be referenced using `interpolation`.
- Resource values in terraform can be parameterized to simplify the process of sharing and configuring different terraform scripts.
- Variables can be declared with the following syntax: `variable <variable_name> { default = <default-variable-value> }`
- Interpolation can be used on generated variables as well, not just for user-defined resources. 
- For example: `ec2-server-name-${count.index}` will increment the name of your ec2 instances as each instance is created, limited by the number set in the count variable.
- Terraform can also print attribute values for generated AWS resources as they are created, for example, the public IP of each ec2 instance that we create with our terraform code. See `output.tf` in this lab for an example of this feature.
- NOTE: the launch config declaration syntac is slightly different from other resources..tbd why.... normal resources: `resource "blah" "blah" { blah }` vs. launch configs: `resource blah "blah" { blah }`....tags and other fields can sometimes be declared without an `=` sign in situations like this...tbd on the reasons behind these idiosycrasies. 

### Section 4 notes... (Terraform key concepts)
- tbd

