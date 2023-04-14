# Serverless Data Engineering in Rust

This repository contains an example implementation of serverless data engineering using Rust programming language. The implementation showcases how to build an event-driven serverless pipeline using Rust and AWS services such as Lambda, S3, and DynamoDB.

## Overview

The pipeline takes data in the form of JSON from an event source and processes it using a Rust Lambda function. The processed data is then stored in a DynamoDB table for later retrieval. The pipeline can be easily extended to include additional steps or to process data from different event sources.

The implementation uses the AWS Serverless Application Model (SAM) to define the infrastructure for the pipeline. The SAM template defines the Lambda function, S3 bucket, and DynamoDB table used by the pipeline.

## Architecture
![serverless pipeline](https://user-images.githubusercontent.com/70916756/228685561-091541f2-e74d-45fc-9e41-fbcc2f20c762.png)
## Requirements

To use this implementation, you need to have the following software and services:

- Rust programming language
- AWS account
- AWS CLI
- AWS SAM CLI

## Usage

To deploy the pipeline, follow these steps:

1. Clone this repository: `git clone https://github.com/silongtan/Rust-Serverless/`
2. Navigate to the project directory: `cd serverless-data-engineering-rust`
3. Build the Rust Lambda function: `cargo build --release --target x86_64-unknown-linux-musl`
4. Package the function code: `sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket your-s3-bucket-name`
5. Deploy the pipeline: `sam deploy --template-file packaged.yaml --stack-name your-stack-name --capabilities CAPABILITY_IAM`

To test the pipeline, you can create an event in the S3 bucket defined in the SAM template. The Lambda function will be triggered automatically and will process the event data.

Before triggering the lambda function, you need to create a S3 bucket, this can be done in the AWS console. The name of the bucket will be used in the next step. 

After the bucket is created, navigate to the lambda page and set up a trigger for the lambda function. The trigger should be set to S3 and the bucket name should be the name of the bucket you created in the previous step.

Once the 2 steps above is completed, the lambda function can be triggered by uploading a file to the S3 bucket. The output or the invocation of the lambda function can be seen in the cloudwatch logs.

## Demo

## License

This implementation is released under the MIT license. See `LICENSE` for more information.

## Contributions

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or a pull request.
