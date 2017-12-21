# CMDB Structure

## Hosting Configuration

* **config**
        * **product** - The Application
                * **solution** - Defines the resources required to create the Product
        * **segment** - Defines the environments the solution should be deployed to

    **solution.json** - describes the resources required to host the product
    **segment.json** - describes the environment the the solution should be deployed to
    ***.ftl** - custom resource templates used to generate solution specific resources

## Application Configuration

* **config**
        * **appsettings** - Application Specific settings
                * **segment** - Segment Specific Settings
                * **app** - Segment based app settings

    **appsettings.json** - application specific settings can be set at any level
    **build.json** - Sets the commit ID to build for app for a given segment

### Provisioning

* **infrastructure**
        * **cloud provider** - The Cloud provider the infrastructure is written for
                * **segment** - The specific templates for a given config segment
                        * **template** - The actual templates or scripts used to build

### Credentials

* **infrastructure**
        * **credentials**
                * **segment** - Credentials specific to a segment
                        * **app** - Credentials specific to an application

    **credential.json** - Contains credentials used in the build or the application - Set at any level of the credentials
    **asFile** - Allows for file based credentials such as certificates