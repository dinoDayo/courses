variable "region" {
    default = "us-east-1"
}

variable "firehose_stream_name" {
    default = "test-logger"
}

variable "environment" {
    default = "local"
}

variable "iam_name_prefix" {
  description = "Prefix used for all created IAM roles and policies"
  type        = string
  nullable    = false
  default     = "test-kinesis-firehose-"
}