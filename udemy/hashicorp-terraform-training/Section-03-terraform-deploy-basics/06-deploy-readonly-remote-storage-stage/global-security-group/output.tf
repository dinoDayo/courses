output "global_sg_id" {
  description = "output global security group id"
  value       = aws_security_group.global_sg.id
  # sensitive   = true
}
