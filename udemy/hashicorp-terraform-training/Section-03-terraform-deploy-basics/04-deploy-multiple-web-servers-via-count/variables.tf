variable "region" {
    default = "us-east-1"
}

variable "http_port" {
    default = 80
}

variable "ssh_port" {
    default = 22
}

variable "my_system" {
    default = "209.6.130.15/32"
}

variable "ami" {
    default = "ami-0a313d6098716f372"
}

variable "instance_type" {
    default = "t2.micro"
}

variable "key_name" {
    default = "terraform"
}