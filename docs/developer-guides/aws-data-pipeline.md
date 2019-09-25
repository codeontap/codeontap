# Data Pipeline Development

Developing for a data pipeline is very "open" to say the least, this is primarily due to the fact that a data pipeline essentially spins up an [AWS EC2](https://aws.amazon.com/ec2/) instance which can effectively invoke or perform any action within the entire AWS stack using the [AWS CLI](https://aws.amazon.com/cli/), only limited by the instances permissions.

As a result the easier way to think for developing a [AWS Data Pipeline](https://aws.amazon.com/datapipeline/) is to rather look at what tasks pipelines are useful for and what tools you need to perform the duties you wish to carry out using the Data Pipeline.

## Should I be using an AWS Data Pipeline

If the task you are wishing to perform is simply that "a task" and not "a service" per'se, this is the best place to begin. Data Pipeline is targeted at repetitive data processing jobs, of generally "larger" datasets and not micro transactions (we're talking hundreds of MB and up per process).

If you have a process that needs to be run periodically and take data from say an S3 bucket, manipulate it and then write the processed data somewhere, then chances are you want to use an AWS Data Pipeline.

## Developing an AWS Data Pipeline

### Overview

Since the nature of a Data Pipeline in itself is so open, it's hard to say specifics regarding how to specifically develop for one. The best place to start is to see what (if any) prebuilt Data Pipeline activities can be used for your process, see [the list of AWS Data Pipeline activities](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-activities.html), also be aware of what databases are supported (or datasets from an S3 bucket) [here](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-databases.html).

Knowing what activities you can use in your Data Pipeline means you can work toward implementing them using their individual control sets (via cli/api calls), for any other custom processes, such as needing to run a container or the like, you will need to resort to shell scripts and or other scripts to execute such tasks. At it's core Data Pipeline is an EC2 instance that is run (executed) periodically, which generally mounts a dataset from either an S3 bucket, database or similar data store service, it then performs an operation to the data (whether that be manipulation or something similar) and then exports it either back to the same medium or another medium before being considered "complete".

As most of the built-in "AWS supported" Data pipeline activities are generally just around moving data from one medium to another, for any actual data manipulation (eg. ogr2ogr or similar) we need to write custom processes to handle this task and execute them using the EC2 containers shell (which is initially executed using a shell command from the pipeline's definition).

So, taking a step back, from beginning to end a data pipeline should:

1. be defined by a pipeline definition
1. take inputs from a values file (parameter values for the pipeline definition)
1. execute something as part of the definition (generally a shell command/script)
1. perform an operation when run
1. save manipulated data "somewhere"
1. and close

### Running a pipeline

When developing a pipeline the easiest way to test the pipeline is to deploy the pipeline into an AWS account. When submitting a pipeline to the AWS API it will be validated and you will receive a reasonably good error response if anything fails. Deploying the pipeline does not activate the pipeline so you can still look through the visualisation of your developed pipeline to confirm everything is ok before executing it.

To deploy a pipeline with the aws cli

1. Create the Pipeline. This just adds an empty pipeline which you will add config to

    ```bash
    aws --region "${region}" datapipeline create-pipeline --name "<Name for the pipeline>" --unique-id "< A unique Id for the pipeline>"
    ```

2. Update the pipeline with your configuration. You will need to have a complete pipeline values file with the appropriate variables setup for S3 buckets etc

    ```bash
    aws --region "${region}" datapipeline put-pipeline-definition --pipeline-id "<The Id returned from the create>" --pipeline-definition "file://<Path to pipeline-definition.json>" --parameter-objects "file://<Path to pipeline-parameters.json>" --parameter-values-uri "file://<Path to values.json>"
    ```

3. This will validate the pipeline and provide you with any feed back on the definition itself. If you make updates to the pipeline you just need to re-run step 2
4. You can then access the pipeline from the AWS console. The visual editor will show you how your pipeline will look and should give you an idea of what will happen.

For further information on pipeline management the AWS guide is the best to go from https://docs.aws.amazon.com/data-pipeline/index.html

### In more detail and actual practice

#### Pipeline Definition and Parameter Values

The pipeline definition `pipeline-definition.json` is used to specify the source and destination for data processed by the pipeline, as well as specifying any environment settings (eg. env vars) and the actual operation for the pipeline itself to perform (eg. executing a shell script on the EC2 instance, which performs a data manipulation operation).

As an example, for a pipeline that mounts an S3 bucket with source data, executes a shell operation against that data and then writes the output of that shell operation to an RDS database, the pipeline-definition (in conjunction with parameterised values in a values file) would specify which S3 bucket and the directory under it to mount to the EC2 instance, the script to exec on the EC2 instance (with any required env vars populated from the values file) and the RDS database connection details (maybe also env vars).

#### Executing a Shell Command

Should your pipeline require an actual data manipulation process opposed to just moving from one medium to another and it is not supported by a built in [AWS Data Pipeline activity](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-concepts-activities.html), you will need to execute the operation using a shell command (which could for instance be an AWS cli call).

When developing a shell based operation, we recommend that you use the predefined layout for scripting below, this provides a standard that can be implemented and reused easily using CodeOnTap. Scripts are to be defined in a respository using an `/aws_pipeline/src/` directory, where the primary script to be executed falls under a `./00_init/` subdirectory, containing an `./init.sh` script (the one executed). Under the `./src/` directory should also fall the pipeline-definition.json and parameters / values files. This continues with `./01_*/init.sh`, `./02_*/init.sh` dirs/scripts and so on as necessary.

The result being of the layout:

```plaintext
/aws_pipeline/src/pipeline-definition.json
/aws_pipeline/src/pipeline-parameters.json
/aws_pipeline/src/values.json
/aws_pipeline/src/00_init/init.sh
/aws_pipeline/src/01_any_name/init.sh - "any_name" here can be "any... name"
/aws_pipeline/src/02_any_other_name/init.sh
/aws_pipeline/src/03_another_operation_name/init.sh
```

Required files/directories associated with any operation script can also be placed/located in the numbered/named `./0x_name/` directory, such that:

```plaintext
/aws_pipeline/src/14_database_setup/init.sh
/aws_pipeline/src/14_database_setup/configuration_defaults.yaml
/aws_pipeline/src/14_database_setup/some_other_required_file_or_dir
```

#### A look at the ./00_init/init.sh script

The `/aws_pipeline/src/00_init/init.sh` script is notably the first script executed as part of a *"shell driven data-pipeline"* for lack of a better term. This means it generally serves the purpose of installing any required software (on the official AMI using yum), then starting any required services on the EC2 instance (such as docker), creating any working directories and setting permissions, making any baseline AWS CLI calls and then moving onto finally executing the next script in-line `../01_*/init.sh`.

### Some Characteristics to Note

#### Disk Size

When using an EC2 instance in a data pipeline if you use the default Ec2 ami type the S3 staging directory (the location on the instance where the S3 bucket data is initially placed before performing any operations) only has minimal disk space. We have a defined *rinse-and-repeat* pipeline-definition that contains a preprocessing step that attaches a new block-device (disk) to the staging location to increase the staging location volume size. This may need to be implemented and/or configured based on your requirements (anything greater than 5GB). When used in a COT (Code on Tap) implementation, the disks are only used during the data pipeline execution so over provisioning the disk size is a non-issue.

##### AWS CLI

The AWS CLI version that generally ships *out-of-the-box* with the Data Pipeline official AMI, is generally outdated and lacking functions such as the "wait" function, we recommend updating the installed cli for any shell based pipelines as part of the `00_init/init.sh` operation, by using pip: `pip install --upgrade awscli`

## Code Samples

### Ec2 Pipeline startup script

This script is a standard init script that you can use to set-up an ec2 based instance that is deployed as part of a pipeline job.
It Includes

- Package Installation
- Software update
- Setting up the code to run and executing the first script in your pipeline code

```bash
#!/bin/bash
#
# This script serves as a template for any shell based AWS Data Pipeline
# wishing to be used within the Code-on-Tap ecosystem. By simply uncommenting
# and/or updating fields within the "optional actions" section of this file, you can
# enable particular features that may be of use within your pipeline, else feel free
# to add to it as necessary for your own use case.


# Move these into the pipeline def as env vars (the dirs are specified there anyway)
# PIPELINE_ID=${1}
# export CODE_RUN_DIR="/code/"


# Update the available software list
yum update -y;

# Update to the latest AWS CLI
pip install --upgrade awscli

# Install baseline software (we recommend always installing these)
yum install -y sysstat jq;


##############################
### BEGIN OPTIONAL ACTIONS ###
##############################

## Install Python 3.6
#yum install -y python36;

## Install and start docker (we wait 10 seconds before starting the daemon [recommended])
#yum install -y docker;
#sleep 10;
#service docker start;


##############################
#### END OPTIONAL ACTIONS ####
##############################



# create the code run dir
mkdir ${CODE_RUN_DIR}

# cp the code to the code run dir
cp -R ${PIPELINE_DIR}/* ${CODE_RUN_DIR}/

# set pems on any shell scripts
chmod 755 ${CODE_RUN_DIR}/*_*/*.sh;

# perform the first actions
bash ${CODE_RUN_DIR}/01_*/init.sh ${PIPELINE_ID} ${VPCID}
```
