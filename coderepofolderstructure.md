# App Code Repository Structure

## Devops

Devops folder defines how the code is built using the codeontap platform including how to build and host the code contained within the repo.

* **devops** - Contains application build and deployment description
		* **resource build tools**
				* **tooling resources**
   
	**deployment_unit.json** - lists the required resources that need to be deployed
	**resource.json** - Describes the specific requirements for a specific resource type

## Product

* **product** 
		* **devops** - Describes an overall product deployment - ApiGateway setup
		* **imp** - application implementation
				* **devops** - An API Gateway endpoint
				* **src** - the source code of the application itself


## API Specific

Follows the same Product description but also includes a mocking section

* **product**
		* **api**
				* **spec**
						* **swagger.yaml**
				* **imp**
				* **devops**
		* **mock** 
				* **imp**
				* **devops** 

The spec contains the swagger definition from the product overall. The same spec is used for both the active API and the mock api. This ensures consistency between the mock and the active API