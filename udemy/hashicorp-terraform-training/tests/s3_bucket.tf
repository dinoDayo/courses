resource "aws_s3_bucket" "test_bucket" {
    bucket = "${var.firehose_stream_name}-data"

    tags = {
        ENV = "${var.environment}"
    }

}

resource "aws_s3_bucket_acl" "test_bucket_acl" {
  bucket = "${aws_s3_bucket.test_bucket.id}"
  acl    = "private"
  depends_on = [aws_s3_bucket_ownership_controls.s3_bucket_acl_ownership]
}

# Resource to avoid error "AccessControlListNotSupported: The bucket does not allow ACLs"
resource "aws_s3_bucket_ownership_controls" "s3_bucket_acl_ownership" {
  bucket = "${aws_s3_bucket.test_bucket.id}"
  rule {
    object_ownership = "ObjectWriter"
  }
}