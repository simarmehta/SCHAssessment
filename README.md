# SCHAssessment

---

# AWS CloudFormation Template for S3 and EC2

## Introduction
This repository contains an AWS CloudFormation template designed to provision an S3 bucket and an EC2 instance. It's a foundational step towards building and deploying applications on AWS, demonstrating infrastructure as code (IaC) principles.

## Requirements
- AWS Account
- AWS CLI installed and configured (optional, for CLI deployment)
- An existing EC2 KeyPair for SSH access

## Template Overview
The CloudFormation template includes the following resources:
- **S3 Bucket:** A simple storage solution for any scale of data.
- **EC2 Instance:** A t2.micro instance for web serving or application hosting, with SSH and HTTP access.
- **Security Group:** Defines firewall rules to control traffic towards the EC2 instance.

## How to Deploy
### Via AWS Management Console
1. Log in to the AWS Management Console and navigate to the CloudFormation service.
2. Choose *Create stack* > *With new resources (standard)*.
3. Upload the provided CloudFormation template file.
4. Enter the required parameters (e.g., KeyName).
5. Follow the on-screen instructions to review and create the stack.

### Via AWS CLI
If you prefer using the command line, you can deploy the template using the AWS CLI:
```bash
aws cloudformation create-stack --stack-name MyStack --template-body file://path_to_template/template.yaml --parameters ParameterKey=KeyName,ParameterValue=my-key-pair
```
Replace `path_to_template/template.yaml` with the actual path to your template file and `my-key-pair` with your EC2 KeyPair name.

## Customization
To customize the deployment, you may need to adjust the following parameters in the template:
- **BucketName:** Ensure the S3 bucket name is unique globally.
- **ImageId:** Use an AMI that matches your desired AWS region and OS.
- **InstanceType:** Adjust based on your computing power needs.
- **KeyName:** Specify your existing EC2 KeyPair for SSH access.

## Enhancing Security
- **SSH Access:** The template currently allows SSH access from any IP address. For enhanced security, limit SSH access to your IP address or a known range of IP addresses by modifying the `CidrIp` parameter under `InstanceSecurityGroup`.
- **HTTP Traffic:** Similar to SSH access, consider restricting HTTP access if the EC2 instance doesn't need to be publicly accessible.
- **Parameters:** Use AWS Secrets Manager for sensitive information and reference them in your CloudFormation template to enhance security.
- **Monitoring:** Enable CloudTrail and Config to monitor and audit AWS resource configurations and changes.

## Conclusion
This template provides a basic structure for deploying an application infrastructure on AWS. It is designed for educational purposes and initial project setups. Ensure to tailor the security settings and resource configurations to fit your project's needs before moving to a production environment.








#  Assessment Part 2-

---

# Python AWS Lambda Function Deployment Guide

This guide provides step-by-step instructions on how to prepare, package, and deploy a Python AWS Lambda function using this GitHub repository as a starting point. The example function makes an HTTP GET request and returns the requester's IP address.

## Prerequisites

- AWS CLI installed and configured
- Python 3.x installed
- Git installed

## Clone the Repository

Start by cloning this repository to your local machine to get the `lambda_function.py` and other necessary files.

```bash
git clone <repository-url>
cd <repository-name>
```

Replace `<repository-url>` with the URL of this GitHub repository and `<repository-name>` with the name of the folder created by `git clone`.

## Prepare Your Function

1. **Create a `requirements.txt` File**

Create a `requirements.txt` file in the root directory of the cloned repository. This file should list all external libraries your Lambda function depends on. For the provided `lambda_function.py`, you need the `requests` library.

```plaintext
requests
```

2. **Set Up a Virtual Environment**

It's a good practice to use a virtual environment for Python projects. This keeps your project's dependencies isolated from the system Python.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install Dependencies**

With the virtual environment activated, install the required libraries specified in `requirements.txt`.

```bash
pip install -r requirements.txt
```

4. **Deactivate the Virtual Environment**

Once the dependencies are installed, you can deactivate the virtual environment.

```bash
deactivate
```

## Package Your Function

1. **Create a ZIP File**

Navigate to the root directory of your project where `lambda_function.py` and the `venv` directory are located.

- **For Linux/Mac:**


- **For Windows:**

```cmd
cd venv\Lib\site-packages
powershell Compress-Archive -Path * -DestinationPath $OLDPWD\my-function.zip -Force
cd $OLDPWD
powershell Compress-Archive -Path lambda_function.py -Update -DestinationPath my-function.zip
```

Make sure to replace `python3.x` with the specific version of Python you're using (e.g., `python3.8`).

## Deploy Your Function to AWS Lambda

1. **Create a New Lambda Function on AWS**

- Navigate to the AWS Lambda Console.
- Click on *Create function* and follow the instructions to create a new function.
- Choose *Author from scratch*, and set the runtime to match your Python version.

2. **Upload Your ZIP File**

- In the *Function code* section of your Lambda function's configuration page, choose *Upload from* > *.zip file* and upload your `my-function.zip` file.
- Set the handler information according to your function's entry point. For the provided example, it should be `lambda_function.lambda_handler`.

3. **Test Your Function**

- Configure a test event and execute your Lambda function to ensure it works as expected.



## Deploy Your Function to AWS Lambda Using the AWS CLI

Once you've packaged your function into a ZIP file, you can deploy it to AWS Lambda using the AWS CLI. This method is efficient for both initial deployments and updates to your function.

### Initial Deployment

If you haven't already created a Lambda function on AWS, you can do so using the AWS CLI. Replace `<function-name>`, `<role-arn>`, and `<runtime>` with your function's name, the ARN of the IAM role that the Lambda function assumes when it executes, and the Python runtime version, respectively.

```bash
aws lambda create-function --function-name <function-name> \
  --runtime <runtime> --role <role-arn> \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://my-function.zip
```

For the runtime, use a value like `python3.8` depending on the version of Python you're using. The handler value `lambda_function.lambda_handler` tells AWS Lambda to execute the `lambda_handler` function defined in `lambda_function.py`.


## Conclusion

You've now successfully prepared, packaged, and deployed a Python AWS Lambda function using this repository as a starting point. This process can be applied to any Python Lambda function development, allowing for rapid deployment and iteration.



