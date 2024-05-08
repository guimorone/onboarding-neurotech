provider "aws" {
  region  = "us-east-1"
  profile = "default"
}

data "archive_file" "zip_the_python_code" {
  type        = "zip"
  source_dir  = "${path.module}/src/"
  output_path = "${path.module}/${var.output_path}"
}

resource "aws_lambda_function" "terraform_lambda_func" {
  filename         = data.archive_file.zip_the_python_code.output_path
  function_name    = var.function_name
  role             = aws_iam_role.lambda_role.arn
  memory_size      = 128
  timeout          = 300
  handler          = "lambda_function.lambda_handler"
  runtime          = var.runtime
  depends_on       = [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role]
}
