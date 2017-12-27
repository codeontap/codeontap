# CMDB Structure

## Hosting Configuration

````
config/
|
|- <product>/ ______________________ #
|
|  |- <solution>/ __________________ #
|    |- solution.json ______________ # describes the resources required to host the product
|    |- *.ftl ______________________ # custom resource templates used to generate solution specific resources
|
|    |- <segment>/ _________________ # an instance of the solution
|       |- segment.json ____________ # describes the environment the solution should be deployed to
````

## Application Configuration

````
config/
|
|- appsettings/ ____________________ # application specific settings
|
|   |- <segment>/ __________________ # segment specific settings
|
|     |- <application>-v<version>/ __ # Application based settings
|
|        |- build.json _____________ # Code repo commimt id and build tooling
|        |- appsettings.json _______ # application specifc overrides 
````

### Provisioning

````
infrastructure/ ____________________ # the provisioned infrastructure for the solution
|
|- <cloud provider>/ _______________ # the cloud provider of the infrastructure
|
|    |- <segment>/ _________________ # the segment level infrastructure
|
|        |- <template type>/ _______ # the provisioning process for the segment
|
|            |- *-template.json ____ # the declartive template used for provisioning
|            |- *-stack.json _______ # the output from the declaritve template
|            |- *-epilouge.sh ______ # a script run before the template is run
|            |- *-prolouge.sh ______ # a script run after the tempalte has run
|
|- credentials/
|
|    |- <segment>/ _________________ # segment level credentials
|
|        |- <application>/ _________ # application level credentials
|            |- credential.json ____ # credential details
|
|            |- asFile/ ____________ # allows for file based credentials
|                |- <credential files (certifcates,keys etc)>
````

### Accounts

The accounts CMDB is a seperate repository to the domain level CMDB respostiory as it can be shared across multiple domains/applications. Accounts can be grouped into subdirectories inorder to classify them.

````
<tenant>/ _________________________ # the organsisation details over all
|    |- domains.json ______________ # DNS zone details used for service naming and resolution
|    |- tenant.json _______________ # default settings for the organisation
|    |- ipaddressgroups_<name>.json # IP address collections used for access control
|    |- countrygroups.json ________ # country collections used for access control
|
<account>/ ________________________ # a cloud provider account
|
|    |- config/ ___________________ # account level configuration details
|        |- account.json __________ # account specifc details
|
|        |- appsettings/
|            |- appsettings.json __ # account level application settings
|
|    |- infrastructure/
|
|        |- credentials/
|            |- credentials.json __ # account level credentials
````
