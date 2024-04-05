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