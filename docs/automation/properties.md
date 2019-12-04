# Jenkins Property Files

The Repositories (AccountsCMDB, ProductCMDB, and Code ) are linked together in the application life cycle management service (ALM).
The Gen3 framework establishes the environmental configuration based on the location of the process calling the framework, when running as a Jenkins job the location is determined using 2 methods, the location of the Job in the job folder structure and properties files which, combined with the EnvInjector plugin which inserts environment variables into the run time of the job.

## Properties Files

The properties files follow a hierarchy structure, with a server level properties folder and a properties file per product.
These are stored in

```text
/var/opt/codeontap
```

### site.properties

The site.properties file contains the overall configuration required for the deployment of a product to any environment.

The following settings should be set in the site.properties file

### Global Settings

* **AUTOMATION_BASE_DIR** - (Required) - The directory where the Gen3-Automation GitHub repository has been cloned
* **AUTOMATION_DIR** - (Required) - The directory within the Gen3-Automation repository for the Automation provider you are using (aws is the standard option at this time)
* **GENERATION_BASE_DIR** - (Required) - The directory where the gen3 github repository has been cloned
* **GENERATION_STARTUP_DIR** - (Required) - The directory where the gen3 GitHub repository has been cloned
* **GENERATION_STARTUP_REFERENCE** (optional)
* **GENERATION_PATTERNS_REFERENCE** (optional)
* **AWS_AUTOMATION_USER** - (Required) - The name of the aws config profile that the automation server will use
* **AWS_AUTOMATION_ROLE** - (Required) - The name of the role available in each account that the automation account will assume
* **GIT_EMAIL_DEFAULT** - (Required) - The email account used when interacting with Github
* **GITHUB_ORG** - (Required) - The github organisation where the CMDB repositories live
* **ACCOUNT_UNITS** - (Required) - The account level resources to deploy
* **REMOTE_DOKER_REPOS** - (Required) - A list of Docker images used as part of the deployment process
* **ACCOUNTS** - (Required) -  A list of account ids that the automation framework will interact with. The id's are based on the Accounts CMDB

### Account Specific Settings

Account level settings are set as part of the global configuration. This allows the same account to be used across independent products.
Account specific settings are prefixed with the account ID.

* **ACCOUNTID_AWS_ACCOUNT** - (Required) - The AWS account ID which maps to the codeontap account Id
* **ACCOUNTID_DOCKER_DNS** - (Required) - The DNS name of a docker registry used for hosting private images
* **ACCOUNTID_LAMBDA_DNS** - (Required) - The name of an S3 bucket used to host lambda deployment packages
