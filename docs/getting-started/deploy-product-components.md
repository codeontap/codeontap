# Deploy Product Components

Now we can finish of the deployment of the infrastructure components that the automation product will use

## Segment Components

Hop into the segment context

```bash
cd /var/opt/codeontap/automation/config/solutionsv2/shared/default/

export ACCOUNT=<account id>
```

Repeat the following steps for the listed deployment units

- **iam** - Deploys authentication roles which can be used by other components
- **lg** - Deploys log groups which can be used by other components
- **vpc** - Deploys the private network infrastructure that our container hosts wil use
- **eip** - Reserves a set of static elastic IPs' which will be used for our NAT gateway and SSH Service
- **igw** - Deploys an Internet gateway for the VPC to provide internet access
- **nat** - Deploys a Network Address Translation (NAT) and updates the vpc route tables to use it where appropriate. This provides outbound only initiated access to the internet
- **vpcednpoint** - Deploys vpcendpoints which offer dedicated network links to the cloud provider
- **ssh** - Creates an ssh auto-scale group which provides an ec2 Instance on a know IP address for management and troubleshooting

Generate the templates used to deploy the services

```bash
${GENERATION_DIR}/createSegmentTemplate.sh -u <deployment unit>
```

This should go through a few steps where we generate the cloudformation templates and scripts required to deploy the components

Deploy the unit

```bash
${GENERATION_DIR}/manageStack.sh -l segment -u <deployment unit>
```

This should now start to deploy the components into the AWS account that you defined at the start

Repeat these steps for each deployment unit listed above

## Solution Components

Now that we have the shared resources deployed, we can look at the product specific infrastructure. A solution component is product specific infrastructure that doesn't have product specific code to deploy. This includes services like object stores (s3), databases (rds), file shares (efs) and container hosts (ecs).

From the segment context, repeat the following steps for listed deployment units 

- **iam** - Deploy permissions and roles for the solution components that will be deployed. This allows for the security configuration to be separated from the infrastructure deployment
- **lg** - Deploy the log groups that will be used by the components to log their system level information. This allows for the resources to be recreated without recreating the logs and losing old log data
- **alm-lb** - A classic load balancer instance which is used for SSL offload and a public facing endpoint for Jenkins
- **alm-efs** - A persistent file share used to host the Jenkins Home folder state
- **alm-ecs** - The infrastructure required to run an Elastic Container Service cluster ( auto-scalegroup, launch profile for instances, and an ecs cluster instance)

```bash
${GENERATION_DIR}/createSolutionTemplate.sh -u <deployment unit>
```

This should go through a few steps where we generate the cloudformation templates and scripts required to deploy the components

Deploy the unit

```bash
${GENERATION_DIR}/manageStack.sh -l solution -u <deployment unit>
```

This should now start to deploy the components into the AWS account that you defined at the start

Repeat these steps for each deployment unit listed above

## Add Docker Containers to local registry

Now we need to get the containers that are used by the alm service product. We store these in a local container registry to ensure that they are always available and that the version of the container is managed by us.

We will need the following containers from docker hub to deploy the ALM service

- **codeontap/jenkins-master** - A Jenkins master with some helper scripts to get the master up and running
- **codeontap/gen3-jenkins-slave** - A Jenkins JNLP agent with codeontap installed along with some application build tools
- **codeontap/redirector** - An http -> https redirection container used by the load balancer to redirect all insecure http requests to https instead

Run the following command for each container listed with the following

- REMOTE_DOCKER_REPO = the container name listed above
- DOCKER_REPO = the name that will be used for the local container, drop codeontap/ from the name listed above ( e.g. codeontap/redirector = redirector)
- REMOTE_DOCKER_TAG = the image tag to pull - unless you want a specific version use latest
- DOCKER_TAG = the same tag as the REMOTE_DOCKER_TAG

!!! warning
    The images are quite big and will be downloaded and then uploaded, so make sure you are on a reasonable internet connection

```bash
export ACCOUNT=<account id>
${AUTOMATION_DIR}/manageDocker.sh -p -u dockerhub -i <REMOTE_DOCKER_REPO> -l <DOCKER_REPO> -r <REMOTE_DOCKER_TAG> -t <DOCKER_TAG>
```

The docker image will be pulled to your local docker instance then pushed to the private AWS Container registry (ECR). Repeat for each of the images

## Application Components

Now that we have all of the infrastructure in place and the containers staged we can deploy the application components. Application components are generally deployed with the product specific code which is built as part of your CICD process. Since the automation components are already built, we can skip the build process and just deploy the components. 

From the segment context, repeat the following steps for listed deployment units

- **iam** - Deploy permissions and roles for the application components that will be deployed. This allows for the security configuration to be separated from the component deployment
- **lg** - Deploy the log groups that will be used by the components to log their system level information. This allows for the resources to be recreated without recreating the logs and losing old log data
- **codeontap** - Deploys an ECS task definition which will be used by the Jenkins instance to provision Jenkins agents
- **jenkins** - Deploys an ECS service which ensures that a single instance of the Jenkins container is running at all times, along with a redirector instance

```bash
${GENERATION_DIR}/createApplicationTemplate.sh -u <deployment unit>
```

This should go through a few steps where we generate the cloudformation templates and scripts required to deploy the components

Deploy the unit

```bash
${GENERATION_DIR}/manageStack.sh -l application -u <deployment unit>
```

This should now start to deploy the components into the AWS account that you defined at the start

Repeat these steps for each deployment unit listed above

## Next Step: [Accessing Jenkins](./accessing-jenkins.md)
