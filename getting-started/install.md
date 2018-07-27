# Getting Started

This getting started guide uses codeontap to deploy the application life-cycle management (ALM) service. Once deployed this service is used to build and deploy your applications.

The service deployed in the getting started guide has the following components:

- AWS ECS cluster
  - A Jenkins container deployed as a service
  - Jenkins integration with ECS to deploy container based slave build agents
- AWS EFS Filesystem to host the Jenkins home drive
- AWS ELB load balancer with SSL offload configured

## Prerequisites

To build the ALM service you will need the following before you can get started

- A local machine with docker installed
- AWS Account
- IAM Access Secret key configured on the local machine
- A DNS domain name used for the automation service
- SSL Certificate deployed in the AWS Accounts ACM configuration ( can either be an external certificate or generated with ACM )

## Installation Process

1. Create a directory which will be used to store the CMDB and state data. This should be configured as a git repository and ideally synced with a source control provider

2. Pull down the codeontap docker image

    ```bash
    docker pull codeontap/gen3:stable
    ```

## Provisioning Setup

1. Add product certificate mapping for automation product
2. Create and Deploy Account level components
   1. audit
   2. s3
   3. apigateway
   4. waf
3. Create and deploy segment level components
   1. cmk
   2. vpc
   3. s3
   4. eip
   5. ssh
4. Encrypt Credentials
   - Github Client Secret
   - Github Credentials
5. Create and deploy solution level components
   1. iam
   2. lg
   3. alm-elb
   4. alm-efs
   5. alm-ecs
   6. redirector
   7. codeontap
   8. jenkins