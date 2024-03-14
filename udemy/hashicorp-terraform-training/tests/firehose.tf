resource "aws_kinesis_firehose_delivery_stream" "test_delivery_stream" {
  name        = "${var.firehose_stream_name}-delivery"
  destination = "extended_s3"
  
  extended_s3_configuration {
    role_arn   = "${aws_iam_role.firehose.arn}"
    bucket_arn = "${aws_s3_bucket.test_bucket.arn}"

    buffering_size = 64     # minimum size required for dynamic partitioning
    buffering_interval = 60

    cloudwatch_logging_options {
      enabled = "true"
      log_group_name = "${aws_cloudwatch_log_group.test_firehose_log_group.name}"
      log_stream_name = "${aws_cloudwatch_log_stream.test_firehose_log_stream.name}"
    }

    # dynamic partitioning configs: https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html
    dynamic_partitioning_configuration {
      enabled = "true"
    }
    # Example prefix using partitionKeyFromQuery, applicable to JQ processor, based on AWS test data ({"TICKER_SYMBOL":"QXZ","SECTOR":"HEALTHCARE","CHANGE":-0.05,"PRICE":84.51})
    prefix              = "stream_data/symbol=!{partitionKeyFromQuery:symbol}/sector=!{partitionKeyFromQuery:sector}/year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:HH}/"
    error_output_prefix = "errors/year=!{timestamp:yyyy}/month=!{timestamp:MM}/day=!{timestamp:dd}/hour=!{timestamp:HH}/!{firehose:error-output-type}/"
    processing_configuration {
      enabled = "true"
      # JQ processor example
      processors {
        type = "MetadataExtraction"
        parameters {
          parameter_name  = "JsonParsingEngine"
          parameter_value = "JQ-1.6"
        }
        parameters {
          parameter_name  = "MetadataExtractionQuery"
          parameter_value = "{symbol:.TICKER_SYMBOL,sector:.SECTOR}"
        }
      }
    }
  }

  tags = {
    ENV = "${var.environment}"
  }
}