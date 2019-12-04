# Introduction

This guide uses codeontap to deploy the application life-cycle management (ALM) service. Once deployed this service can be used with the CodeOnTap Automation Plugin to crate a Jenkins based CI/CD pipeline

The service deployed in the getting started guide has the following components:

- AWS ECS cluster
  - A Jenkins container deployed as a service
  - Jenkins integration with ECS to deploy container based Jenkins agents
- AWS EFS Filesystem to host the Jenkins home drive
- AWS ELB load balancer with SSL offload configured

## Prerequisites

To build the ALM service you will need the following before you can get started

!!! warning
    The getting started guide will deploy resources which incur AWS service charges. Remember to remove the deployment when you are finished with it

- A local machine with docker installed
- AWS Account
- IAM Access Secret key configured on the local machine
- A DNS domain name for your tenant
- SSL Certificate deployed in the AWS Accounts ACM configuration ( can either be an external certificate or generated with ACM )

## Next Step: [Setup Your Local Environment](./local-env-setup.md)
