---
layout: page
title: Code Folder Structure
category: configuration
---
# Application Code Repository Structure

The application code repository hosts the code for an application/product along with the details of how the code should be used. Like the CMDB repository the folder structure of the repository is used by the automation service to build the application.

## Product

Multiple implementations can be place in the same product folder, the devops and imp directories just need to be placed inside a sub directory for each implementation.

````text
<product>\
|
|    |- <resource>\
|        |- devops\ __________________ # Provides product level resource details, see devops
|
|    |- imp\ _________________________ # the implementation of the product
|
|        |- devops\ __________________ # implementation level resource details, see devops
|
|        |- src\ _____________________ # the source code of the implementation
|
|        |- spec\
|            |- swagger.yaml _________ # the swagger specification for API based products
````

## Devops

Devops folder defines how the code is built using the codeontap platform including how to build and host the code contained within the repository.

````text
devops\ ______________________________ # contains the build and deployment details
|
|    |- <resource build tool> ________ # contains the build tooling information for a specific build tool
|        |- <tooling resources> ______ # the resources required by the the build tooling
|
|    |- deployment_unit.json _________ # lists the required resources to host the code
|    |- resource.json ________________ # describes the specific requirements for the resources
````
