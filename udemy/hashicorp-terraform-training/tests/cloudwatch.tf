resource "aws_cloudwatch_log_group" "test_firehose_log_group" {
  name = "/aws/kinesisfirehose/${var.firehose_stream_name}-delivery"

  tags = {
    ENV = "${var.environment}"
  }
}

resource "aws_cloudwatch_log_stream" "test_firehose_log_stream" {
  name           = "/aws/kinesisfirehose/${var.firehose_stream_name}-stream"
  log_group_name = "${aws_cloudwatch_log_group.test_firehose_log_group.name}"
}