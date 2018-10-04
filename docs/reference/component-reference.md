# apigateway

Application level API proxy

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

### Component Format

```json
[{"Names" : ["Fragment","Container"],"Type" : "string","Default" : ""},{"Name" : "Links","Type" : "object","Default" : {}},{"Name" : "WAF","Children" : [{"Name" : "IPAddressGroups","Type" : ["array","string"],"Mandatory" : true},{"Name" : "Default","Type" : "string","Values" : ["ALLOW","BLOCK"],"Default" : "BLOCK"},{"Name" : "RuleDefault","Type" : "string","Values" : ["ALLOW","BLOCK"],"Default" : "ALLOW"}]},{"Name" : "EndpointType","Type" : "string","Values" : ["EDGE","REGIONAL"],"Default" : "EDGE"},{"Name" : "IPAddressGroups","Type" : ["array","string"],"Default" : []},{"Name" : "Authentication","Type" : "string","Values" : ["IP","SIG4ORIP","SIG4ANDIP"],"Default" : "IP"},{"Name" : "CloudFront","Children" : [{"Name" : "AssumeSNI","Type" : "boolean","Default" : true},{"Name" : "EnableLogging","Type" : "boolean","Default" : true},{"Name" : "CountryGroups","Type" : ["array","string"],"Default" : []},{"Name" : "CustomHeaders","Type" : ["array","any"],"Default" : []},{"Name" : "Mapping","Type" : "boolean","Default" : false},{"Name" : "Compress","Type" : "boolean","Default" : true}]},{"Name" : "Certificate","Children" : [{"Name" : "*"}]},{"Name" : "Publish","Children" : [{"Name" : "DnsNamePrefix","Type" : "string","Default" : "docs"},{"Name" : "IPAddressGroups","Type" : ["array","string"],"Default" : []}]},{"Name" : "Mapping","Children" : [{"Name" : "IncludeStage","Type" : "boolean","Default" : true}]},{"Name" : "Profiles","Children" : [{"Name" : "SecurityProfile","Type" : "string","Default" : "default"}]}]
```

### Attribute Reference

-   **Fragment**
    -   **Alternate Names** - Container
    -   **Type** - string
    -   **Default** - null
-   **Links**
    -   **Type** - object
    -   **Default** - {}
-   **WAF**
    -   **IPAddressGroups**
        -   **Type** - array, string
        -   **Mandatory** - true
    -   **Default**
        -   **Type** - string
        -   **Values** - ALLOW, BLOCK
        -   **Default** - BLOCK
    -   **RuleDefault**
        -   **Type** - string
        -   **Values** - ALLOW, BLOCK
        -   **Default** - ALLOW
-   **EndpointType**
    -   **Type** - string
    -   **Values** - EDGE, REGIONAL
    -   **Default** - EDGE
-   **IPAddressGroups**
    -   **Type** - array, string
    -   **Default** - \[]
-   **Authentication**
    -   **Type** - string
    -   **Values** - IP, SIG4ORIP, SIG4ANDIP
    -   **Default** - IP
-   **CloudFront**
    -   **AssumeSNI**
        -   **Type** - boolean
        -   **Default** - true
    -   **EnableLogging**
        -   **Type** - boolean
        -   **Default** - true
    -   **CountryGroups**
        -   **Type** - array, string
        -   **Default** - \[]
    -   **CustomHeaders**
        -   **Type** - array, any
        -   **Default** - \[]
    -   **Mapping**
        -   **Type** - boolean
        -   **Default** - false
    -   **Compress**
        -   **Type** - boolean
        -   **Default** - true
-   **Certificate**
    -   * * *
-   **Publish**
    -   **DnsNamePrefix**
        -   **Type** - string
        -   **Default** - docs
    -   **IPAddressGroups**
        -   **Type** - array, string
        -   **Default** - \[]
-   **Mapping**
    -   **IncludeStage**
        -   **Type** - boolean
        -   **Default** - true
-   **Profiles**
    -   **SecurityProfile**
        -   **Type** - string
        -   **Default** - default

* * *

# cache

Managed in-memory cache services

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Component Format

```json
[{"Name" : "Engine","Type" : "string","Mandatory" : true},{"Name" : "EngineVersion","Type" : "string"},{"Name" : "Port","Type" : "string"},{"Name" : "Backup","Children" : [{"Name" : "RetentionPeriod","Type" : "string","Default" : ""}]}]
```

### Attribute Reference

-   **Engine**
    -   **Type** - string
    -   **Mandatory** - true
-   **EngineVersion**
    -   **Type** - string
-   **Port**
    -   **Type** - string
-   **Backup**
    -   **RetentionPeriod**
        -   **Type** - string
        -   **Default** - null

* * *

# userpool

Managed identity service

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Notes

!!! warning
	Requires second deployment to complete configuration

### Component Format

```json
[{"Name" : "MFA","Type" : "boolean","Default" : false},{"Name" : "AdminCreatesUser","Type" : "boolean","Default" : true},{"Name" : "UnusedAccountTimeout","Type" : "number","Default" : 7},{"Name" : "VerifyEmail","Type" : "boolean","Default" : true},{"Name" : "VerifyPhone","Type" : "boolean","Default" : false},{"Name" : "LoginAliases","Type" : ["array","string"],"Default" : ["email"]},{"Name" : "ClientGenerateSecret","Type" : "boolean","Default" : false},{"Name" : "ClientTokenValidity","Type" : "number","Default" : 30},{"Name" : "AllowUnauthenticatedIds","Type" : "boolean","Default" : false},{"Name" : "AuthorizationHeader","Type" : "string","Default" : "Authorization"},{"Name" : "OAuth","Children" : [{"Name" : "Scopes","Type" : ["array","string"],"Default" : ["openid"]},{"Name" : "Flows","Type" : ["array","string"],"Default" : ["code"]}]},{"Name" : "PasswordPolicy","Children" : [{"Name" : "MinimumLength","Type" : "number","Default" : 10},{"Name" : "Lowercase","Type" : "boolean","Default" : true},{"Name" : "Uppercase","Type" : "boolean","Default" : true},{"Name" : "Numbers","Type" : "boolean","Default" : true},{"Name" : "SpecialCharacters","Type" : "boolean","Default" : true}]},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]}]
```

### Attribute Reference

-   **MFA**
    -   **Type** - boolean
    -   **Default** - false
-   **AdminCreatesUser**
    -   **Type** - boolean
    -   **Default** - true
-   **UnusedAccountTimeout**
    -   **Type** - number
    -   **Default** - 7
-   **VerifyEmail**
    -   **Type** - boolean
    -   **Default** - true
-   **VerifyPhone**
    -   **Type** - boolean
    -   **Default** - false
-   **LoginAliases**
    -   **Type** - array, string
    -   **Default** - email
-   **ClientGenerateSecret**
    -   **Type** - boolean
    -   **Default** - false
-   **ClientTokenValidity**
    -   **Type** - number
    -   **Default** - 30
-   **AllowUnauthenticatedIds**
    -   **Type** - boolean
    -   **Default** - false
-   **AuthorizationHeader**
    -   **Type** - string
    -   **Default** - Authorization
-   **OAuth**
    -   **Scopes**
        -   **Type** - array, string
        -   **Default** - openid
    -   **Flows**
        -   **Type** - array, string
        -   **Default** - code
-   **PasswordPolicy**
    -   **MinimumLength**
        -   **Type** - number
        -   **Default** - 10
    -   **Lowercase**
        -   **Type** - boolean
        -   **Default** - true
    -   **Uppercase**
        -   **Type** - boolean
        -   **Default** - true
    -   **Numbers**
        -   **Type** - boolean
        -   **Default** - true
    -   **SpecialCharacters**
        -   **Type** - boolean
        -   **Default** - true
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string

* * *

# computecluster

Auto-Scaling IaaS with code deployment

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

### Component Format

```json
[{"Name" : ["Fragment","Container"],"Type" : "string","Default" : ""},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]},{"Name" : "UseInitAsService","Type" : "boolean","Default" : false},{"Name" : "MinUpdateInstances","Type" : "number","Default" : 1},{"Name" : "ReplaceOnUpdate","Type" : "boolean","Default" : false},{"Name" : "UpdatePauseTime","Type" : "string","Default" : "5M"},{"Name" : "StartupTimeout","Type" : "string","Default" : "15M"},{"Name" : "DockerHost","Type" : "boolean","Default" : false},{"Name" : "Ports","Subobjects" : true,"Children" : [{"Name" : "IPAddressGroups","Type" : ["array","string"],"Default" : []},{"Name" : "LB","Children" : [{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : "LinkName","Type" : "string","Default" : "lb"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string","Default" : ""}]}]}]
```

### Attribute Reference

-   **Fragment**
    -   **Alternate Names** - Container
    -   **Type** - string
    -   **Default** - null
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **UseInitAsService**
    -   **Type** - boolean
    -   **Default** - false
-   **MinUpdateInstances**
    -   **Type** - number
    -   **Default** - 1
-   **ReplaceOnUpdate**
    -   **Type** - boolean
    -   **Default** - false
-   **UpdatePauseTime**
    -   **Type** - string
    -   **Default** - 5M
-   **StartupTimeout**
    -   **Type** - string
    -   **Default** - 15M
-   **DockerHost**
    -   **Type** - boolean
    -   **Default** - false
-   **Ports**
    -   **IPAddressGroups**
        -   **Type** - array, string
        -   **Default** - \[]
    -   **LB**
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **LinkName**
        -   **Type** - string
        -   **Default** - lb
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
        -   **Default** - null

* * *

# contenthub

Hub for decentralised content hosting with centralised publishing
github
application

### Component Format

```json
[{"Name" : "Prefix","Type" : "string","Mandatory" : true},{"Name" : "Engine","Type" : "string","Default" : "github"},{"Name" : "Branch","Type" : "string","Default" : "master"},{"Name" : "Repository","Type" : "string","Default" : ""}]
```

### Attribute Reference

-   **Prefix**
    -   **Type** - string
    -   **Mandatory** - true
-   **Engine**
    -   **Type** - string
    -   **Default** - github
-   **Branch**
    -   **Type** - string
    -   **Default** - master
-   **Repository**
    -   **Type** - string
    -   **Default** - null

* * *

# contentnode

Node for decentralised content hosting with centralised publishing

### Deployment Properties

-   **Available Providers** - github
-   **Component Level** - application

### Component Format

```json
[{"Name" : "Path","Children" : [{"Name" : "Host","Type" : "string","Default" : ""},{"Name" : "Style","Type" : "string","Default" : "single"},{"Name" : "IncludeInPath","Children" : [{"Name" : "Product","Type" : "boolean","Default" : true},{"Name" : "Environment","Type" : "boolean","Default" : false},{"Name" : "Solution","Type" : "boolean","Default" : false},{"Name" : "Segment","Type" : "boolean","Default" : true},{"Name" : "Tier","Type" : "boolean","Default" : false},{"Name" : "Component","Type" : "boolean","Default" : false},{"Name" : "Instance","Type" : "boolean","Default" : false},{"Name" : "Version","Type" : "boolean","Default" : false},{"Name" : "Host","Type" : "boolean","Default" : false}]}]},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]}]
```

### Attribute Reference

-   **Path**
    -   **Host**
        -   **Type** - string
        -   **Default** - null
    -   **Style**
        -   **Type** - string
        -   **Default** - single
    -   **IncludeInPath**
    -   **Product**
        -   **Type** - boolean
        -   **Default** - true
    -   **Environment**
        -   **Type** - boolean
        -   **Default** - false
    -   **Solution**
        -   **Type** - boolean
        -   **Default** - false
    -   **Segment**
        -   **Type** - boolean
        -   **Default** - true
    -   **Tier**
        -   **Type** - boolean
        -   **Default** - false
    -   **Component**
        -   **Type** - boolean
        -   **Default** - false
    -   **Instance**
        -   **Type** - boolean
        -   **Default** - false
    -   **Version**
        -   **Type** - boolean
        -   **Default** - false
    -   **Host**
        -   **Type** - boolean
        -   **Default** - false
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string

* * *

# datapipeline

Managed Data ETL Processing

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

### Component Format

```json
[{"Name" : ["Fragment","Container"],"Type" : "string","Default" : ""},{"Name" : "Permissions","Children" : [{"Name" : "Decrypt","Type" : "boolean","Default" : true},{"Name" : "AsFile","Type" : "boolean","Default" : true},{"Name" : "AppData","Type" : "boolean","Default" : true},{"Name" : "AppPublic","Type" : "boolean","Default" : true}]},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]}]
```

### Attribute Reference

-   **Fragment**
    -   **Alternate Names** - Container
    -   **Type** - string
    -   **Default** - null
-   **Permissions**
    -   **Decrypt**
        -   **Type** - boolean
        -   **Default** - true
    -   **AsFile**
        -   **Type** - boolean
        -   **Default** - true
    -   **AppData**
        -   **Type** - boolean
        -   **Default** - true
    -   **AppPublic**
        -   **Type** - boolean
        -   **Default** - true
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string

* * *

# dataset

A data aretefact that is managed in a similar way to a code unit

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

### Component Format

```json
[{"Name" : "Engine","Type" : "string","Values" : ["s3","rdsSnapshot"],"Mandatory" : true},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]},{"Name" : "Prefix","Type" : "string","Default" : ""}]
```

### Attribute Reference

-   **Engine**
    -   **Type** - string
    -   **Values** - s3, rdsSnapshot
    -   **Mandatory** - true
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **Prefix**
    -   **Type** - string
    -   **Default** - null

* * *

# ec2

A single virtual machine with no code deployment 

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Component Format

```json
[{"Name" : "FixedIP","Type" : "boolean","Default" : false},{"Name" : "DockerHost","Type" : "boolean","Default" : false},{"Name" : ["Fragment","Container"],"Type" : "string","Default" : ""},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]},{"Name" : "Ports","Subobjects" : true,"Children" : [{"Name" : "IPAddressGroups","Type" : ["array","string"],"Default" : []},{"Name" : "LB","Children" : [{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : "LinkName","Type" : "string","Default" : "lb"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string","Default" : ""}]}]}]
```

### Attribute Reference

-   **FixedIP**
    -   **Type** - boolean
    -   **Default** - false
-   **DockerHost**
    -   **Type** - boolean
    -   **Default** - false
-   **Fragment**
    -   **Alternate Names** - Container
    -   **Type** - string
    -   **Default** - null
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **Ports**
    -   **IPAddressGroups**
        -   **Type** - array, string
        -   **Default** - \[]
    -   **LB**
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **LinkName**
        -   **Type** - string
        -   **Default** - lb
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
        -   **Default** - null

* * *

# ecs

An autoscaling container host cluster

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Component Format

```json
[{"Name" : ["Fragment","Container"],"Type" : "string","Default" : ""},{"Name" : "FixedIP","Type" : "boolean","Default" : false},{"Name" : "LogDriver","Type" : "string","Values" : ["awslogs","json-file","fluentd"],"Default" : "awslogs"},{"Name" : "ClusterLogGroup","Type" : "boolean","Default" : true},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]},{"Name" : "DockerUsers","Subobjects" : true,"Children" : [{"Name" : "UserName","Type" : "string"},{"Name" : "UID","Type" : "number","Mandatory" : true}]}]
```

### Attribute Reference

-   **Fragment**
    -   **Alternate Names** - Container
    -   **Type** - string
    -   **Default** - null
-   **FixedIP**
    -   **Type** - boolean
    -   **Default** - false
-   **LogDriver**
    -   **Type** - string
    -   **Values** - awslogs, json-file, fluentd
    -   **Default** - awslogs
-   **ClusterLogGroup**
    -   **Type** - boolean
    -   **Default** - true
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **DockerUsers**
    -   **UserName**
        -   **Type** - string
    -   **UID**
        -   **Type** - number
        -   **Mandatory** - true

* * *

# service

An orchestrated container with always on scheduling

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

### Component Format

```json
[{"Name" : "Containers","Subobjects" : true,"Children" : [{"Name" : "Cpu","Type" : "number","Default" : ""},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]},{"Name" : "LocalLogging","Type" : "boolean","Default" : false},{"Name" : "LogDriver","Type" : "string","Values" : ["awslogs","json-file","fluentd"],"Default" : "awslogs"},{"Name" : "ContainerLogGroup","Type" : "boolean","Default" : false},{"Name" : "RunCapabilities","Type" : ["array","string"],"Default" : []},{"Name" : "Privileged","Type" : "boolean","Default" : false},{"Name" : ["MaximumMemory","MemoryMaximum","MaxMemory"],"Types" : "number","Description" : "Set to 0 to not set a maximum"},{"Name" : ["MemoryReservation","Memory","ReservedMemory"],"Type" : "number","Mandatory" : true},{"Name" : "Ports","Subobjects" : true,"Children" : ["Container",{"Name" : "DynamicHostPort","Type" : "boolean","Default" : false},{"Name" : "LB","Children" : [{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : "LinkName","Type" : "string","Default" : "lb"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string","Default" : ""}]},{"Name" : "IPAddressGroups","Type" : ["array","string"],"Default" : []}]},{"Name" : "Version","Type" : "string","Default" : ""},{"Name" : "ContainerNetworkLinks","Type" : ["array","string"],"Default" : []}]},{"Name" : "DesiredCount","Type" : "number","Default" : -1},{"Name" : "UseTaskRole","Type" : "boolean","Default" : true},{"Name" : "Permissions","Children" : [{"Name" : "Decrypt","Type" : "boolean","Default" : true},{"Name" : "AsFile","Type" : "boolean","Default" : true},{"Name" : "AppData","Type" : "boolean","Default" : true},{"Name" : "AppPublic","Type" : "boolean","Default" : true}]},{"Name" : "TaskLogGroup","Type" : "boolean","Default" : true},{"Name" : "NetworkMode","Type" : "string","Values" : ["none","bridge","awsvpc","host"],"Default" : ""},{"Name" : "ContainerNetworkLinks","Type" : "boolean","Default" : false}]
```

### Attribute Reference

-   **Containers**
    -   **Cpu**
        -   **Type** - number
        -   **Default** - null
    -   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
    -   **LocalLogging**
        -   **Type** - boolean
        -   **Default** - false
    -   **LogDriver**
        -   **Type** - string
        -   **Values** - awslogs, json-file, fluentd
        -   **Default** - awslogs
    -   **ContainerLogGroup**
        -   **Type** - boolean
        -   **Default** - false
    -   **RunCapabilities**
        -   **Type** - array, string
        -   **Default** - \[]
    -   **Privileged**
        -   **Type** - boolean
        -   **Default** - false
    -   **MaximumMemory**
        -   **Alternate Names** - MemoryMaximum, MaxMemory
        -   **Types** - number
        -   **Description** - Set to 0 to not set a maximum
    -   **MemoryReservation**
        -   **Alternate Names** - Memory, ReservedMemory
        -   **Type** - number
        -   **Mandatory** - true
    -   **Ports**
    -   **Container**
    -   **DynamicHostPort**
        -   **Type** - boolean
        -   **Default** - false
    -   **LB**
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **LinkName**
        -   **Type** - string
        -   **Default** - lb
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
        -   **Default** - null
    -   **IPAddressGroups**
        -   **Type** - array, string
        -   **Default** - \[]
    -   **Version**
        -   **Type** - string
        -   **Default** - null
    -   **ContainerNetworkLinks**
        -   **Type** - array, string
        -   **Default** - \[]
-   **DesiredCount**
    -   **Type** - number
    -   **Default** - -1
-   **UseTaskRole**
    -   **Type** - boolean
    -   **Default** - true
-   **Permissions**
    -   **Decrypt**
        -   **Type** - boolean
        -   **Default** - true
    -   **AsFile**
        -   **Type** - boolean
        -   **Default** - true
    -   **AppData**
        -   **Type** - boolean
        -   **Default** - true
    -   **AppPublic**
        -   **Type** - boolean
        -   **Default** - true
-   **TaskLogGroup**
    -   **Type** - boolean
    -   **Default** - true
-   **NetworkMode**
    -   **Type** - string
    -   **Values** - none, bridge, awsvpc, host
    -   **Default** - null
-   **ContainerNetworkLinks**
    -   **Type** - boolean
    -   **Default** - false

* * *

# task

A container defintion which is invoked on demand

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

### Component Format

```json
[{"Name" : "Containers","Subobjects" : true,"Children" : [{"Name" : "Cpu","Type" : "number","Default" : ""},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]},{"Name" : "LocalLogging","Type" : "boolean","Default" : false},{"Name" : "LogDriver","Type" : "string","Values" : ["awslogs","json-file","fluentd"],"Default" : "awslogs"},{"Name" : "ContainerLogGroup","Type" : "boolean","Default" : false},{"Name" : "RunCapabilities","Type" : ["array","string"],"Default" : []},{"Name" : "Privileged","Type" : "boolean","Default" : false},{"Name" : ["MaximumMemory","MemoryMaximum","MaxMemory"],"Types" : "number","Description" : "Set to 0 to not set a maximum"},{"Name" : ["MemoryReservation","Memory","ReservedMemory"],"Type" : "number","Mandatory" : true},{"Name" : "Ports","Subobjects" : true,"Children" : ["Container",{"Name" : "DynamicHostPort","Type" : "boolean","Default" : false},{"Name" : "LB","Children" : [{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : "LinkName","Type" : "string","Default" : "lb"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string","Default" : ""}]},{"Name" : "IPAddressGroups","Type" : ["array","string"],"Default" : []}]},{"Name" : "Version","Type" : "string","Default" : ""},{"Name" : "ContainerNetworkLinks","Type" : ["array","string"],"Default" : []}]},{"Name" : "UseTaskRole","Type" : "boolean","Default" : true},{"Name" : "Permissions","Children" : [{"Name" : "Decrypt","Type" : "boolean","Default" : true},{"Name" : "AsFile","Type" : "boolean","Default" : true},{"Name" : "AppData","Type" : "boolean","Default" : true},{"Name" : "AppPublic","Type" : "boolean","Default" : true}]},{"Name" : "TaskLogGroup","Type" : "boolean","Default" : true},{"Name" : "FixedName","Type" : "boolean","Default" : false}]
```

### Attribute Reference

-   **Containers**
    -   **Cpu**
        -   **Type** - number
        -   **Default** - null
    -   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
    -   **LocalLogging**
        -   **Type** - boolean
        -   **Default** - false
    -   **LogDriver**
        -   **Type** - string
        -   **Values** - awslogs, json-file, fluentd
        -   **Default** - awslogs
    -   **ContainerLogGroup**
        -   **Type** - boolean
        -   **Default** - false
    -   **RunCapabilities**
        -   **Type** - array, string
        -   **Default** - \[]
    -   **Privileged**
        -   **Type** - boolean
        -   **Default** - false
    -   **MaximumMemory**
        -   **Alternate Names** - MemoryMaximum, MaxMemory
        -   **Types** - number
        -   **Description** - Set to 0 to not set a maximum
    -   **MemoryReservation**
        -   **Alternate Names** - Memory, ReservedMemory
        -   **Type** - number
        -   **Mandatory** - true
    -   **Ports**
    -   **Container**
    -   **DynamicHostPort**
        -   **Type** - boolean
        -   **Default** - false
    -   **LB**
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **LinkName**
        -   **Type** - string
        -   **Default** - lb
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
        -   **Default** - null
    -   **IPAddressGroups**
        -   **Type** - array, string
        -   **Default** - \[]
    -   **Version**
        -   **Type** - string
        -   **Default** - null
    -   **ContainerNetworkLinks**
        -   **Type** - array, string
        -   **Default** - \[]
-   **UseTaskRole**
    -   **Type** - boolean
    -   **Default** - true
-   **Permissions**
    -   **Decrypt**
        -   **Type** - boolean
        -   **Default** - true
    -   **AsFile**
        -   **Type** - boolean
        -   **Default** - true
    -   **AppData**
        -   **Type** - boolean
        -   **Default** - true
    -   **AppPublic**
        -   **Type** - boolean
        -   **Default** - true
-   **TaskLogGroup**
    -   **Type** - boolean
    -   **Default** - true
-   **FixedName**
    -   **Type** - boolean
    -   **Default** - false

* * *

# efs

A managed network attached file share

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Component Format

```json
[{"Name" : "Encrypted","Type" : "boolean","Default" : true}]
```

### Attribute Reference

-   **Encrypted**
    -   **Type** - boolean
    -   **Default** - true

* * *

# es

A managed ElasticSearch instance

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Component Format

```json
[{"Name" : "Authentication","Type" : "string","Values" : ["IP","SIG4ORIP","SIG4ANDIP"],"Default" : "IP"},{"Name" : "IPAddressGroups","Type" : ["array","string"],"Mandatory" : true},{"Name" : "AdvancedOptions","Type" : ["array","string"],"Default" : []},{"Name" : "Version","Type" : "string","Default" : "2.3"},{"Name" : "Encrypted","Type" : "boolean","Default" : false},{"Name" : "Snapshot","Children" : [{"Name" : "Hour","Type" : "string","Default" : ""}]},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]}]
```

### Attribute Reference

-   **Authentication**
    -   **Type** - string
    -   **Values** - IP, SIG4ORIP, SIG4ANDIP
    -   **Default** - IP
-   **IPAddressGroups**
    -   **Type** - array, string
    -   **Mandatory** - true
-   **AdvancedOptions**
    -   **Type** - array, string
    -   **Default** - \[]
-   **Version**
    -   **Type** - string
    -   **Default** - 2.3
-   **Encrypted**
    -   **Type** - boolean
    -   **Default** - false
-   **Snapshot**
    -   **Hour**
        -   **Type** - string
        -   **Default** - null
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string

* * *

# lambda

Container for a Function as a Service deployment

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

### Component Format

```json
[]
```

### Attribute Reference

* * *

# function

A specific entry point for the lambda deployment

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

### Component Format

```json
[{"Name" : ["Fragment","Container"],"Type" : "string","Default" : ""},{"Name" : "Handler","Type" : "string","Mandatory" : true},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]},{"Name" : "LogMetrics","Subobjects" : true,"Children" : [{"Name" : "LogFilter","Type" : "string","Mandatory" : true}]},{"Name" : "LogWatchers","Subobjects" : true,"Children" : [{"Name" : "LogFilter","Type" : "string","Mandatory" : true},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]}]},{"Name" : "Alerts","Subobjects" : true,"Children" : ["Description",{"Name" : "Name","Type" : "string","Mandatory" : true},{"Name" : "Metric","Children" : [{"Name" : "Name","Type" : "string","Mandatory" : true},{"Name" : "Type","Type" : "string","Mandatory" : true}]},{"Name" : "Threshold","Type" : "number","Default" : 1},{"Name" : "Severity","Type" : "string","Default" : "Info"},{"Name" : "Namespace","Type" : "string","Default" : ""},{"Name" : "Comparison","Type" : "string","Default" : "Threshold"},{"Name" : "Operator","Type" : "string","Default" : "GreaterThanOrEqualToThreshold"},{"Name" : "Time","Type" : "number","Default" : 300},{"Name" : "Periods","Type" : "number","Default" : 1},{"Name" : "Statistic","Type" : "string","Default" : "Sum"},{"Name" : "ReportOk","Type" : "boolean","Default" : false},{"Name" : "MissingData","Type" : "string","Default" : "notBreaching"}]},{"Name" : ["Memory","MemorySize"],"Type" : "number","Default" : 0},{"Name" : "RunTime","Type" : "string","Values" : ["nodejs","nodejs4.3","nodejs6.10","nodejs8.10","java8","python2.7","python3.6","dotnetcore1.0","dotnetcore2.0","dotnetcore2.1","nodejs4.3-edge","go1.x"],"Mandatory" : true},{"Name" : "Schedules","Subobjects" : true,"Children" : [{"Name" : "Expression","Type" : "string","Default" : "rate(6 minutes)"},{"Name" : "InputPath","Type" : "string","Default" : "\/healthcheck"},{"Name" : "Input","Type" : "object","Default" : {}}]},{"Name" : "Timeout","Type" : "number","Default" : 0},{"Name" : "VPCAccess","Type" : "boolean","Default" : true},{"Name" : "UseSegmentKey","Type" : "boolean","Default" : false},{"Name" : "Permissions","Children" : [{"Name" : "Decrypt","Type" : "boolean","Default" : true},{"Name" : "AsFile","Type" : "boolean","Default" : true},{"Name" : "AppData","Type" : "boolean","Default" : true},{"Name" : "AppPublic","Type" : "boolean","Default" : true}]},{"Name" : "PredefineLogGroup","Type" : "boolean","Default" : false},{"Name" : "Environment","Children" : [{"Name" : "AsFile","Type" : "boolean","Default" : false},{"Name" : "Json","Children" : [{"Name" : "Escaped","Type" : "boolean","Default" : true},{"Name" : "Prefix","Type" : "string","Values" : ["json",""],"Default" : "json"}]}]}]
```

### Attribute Reference

-   **Fragment**
    -   **Alternate Names** - Container
    -   **Type** - string
    -   **Default** - null
-   **Handler**
    -   **Type** - string
    -   **Mandatory** - true
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **LogMetrics**
    -   **LogFilter**
        -   **Type** - string
        -   **Mandatory** - true
-   **LogWatchers**
    -   **LogFilter**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **Alerts**
    -   **Description**
    -   **Name**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Metric**
    -   **Name**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Type**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Threshold**
        -   **Type** - number
        -   **Default** - 1
    -   **Severity**
        -   **Type** - string
        -   **Default** - Info
    -   **Namespace**
        -   **Type** - string
        -   **Default** - null
    -   **Comparison**
        -   **Type** - string
        -   **Default** - Threshold
    -   **Operator**
        -   **Type** - string
        -   **Default** - GreaterThanOrEqualToThreshold
    -   **Time**
        -   **Type** - number
        -   **Default** - 300
    -   **Periods**
        -   **Type** - number
        -   **Default** - 1
    -   **Statistic**
        -   **Type** - string
        -   **Default** - Sum
    -   **ReportOk**
        -   **Type** - boolean
        -   **Default** - false
    -   **MissingData**
        -   **Type** - string
        -   **Default** - notBreaching
-   **Memory**
    -   **Alternate Names** - MemorySize
    -   **Type** - number
    -   **Default** - 0
-   **RunTime**
    -   **Type** - string
    -   **Values** - nodejs, nodejs4.3, nodejs6.10, nodejs8.10, java8, python2.7, python3.6, dotnetcore1.0, dotnetcore2.0, dotnetcore2.1, nodejs4.3-edge, go1.x
    -   **Mandatory** - true
-   **Schedules**
    -   **Expression**
        -   **Type** - string
        -   **Default** - rate(6 minutes)
    -   **InputPath**
        -   **Type** - string
        -   **Default** - /healthcheck
    -   **Input**
        -   **Type** - object
        -   **Default** - {}
-   **Timeout**
    -   **Type** - number
    -   **Default** - 0
-   **VPCAccess**
    -   **Type** - boolean
    -   **Default** - true
-   **UseSegmentKey**
    -   **Type** - boolean
    -   **Default** - false
-   **Permissions**
    -   **Decrypt**
        -   **Type** - boolean
        -   **Default** - true
    -   **AsFile**
        -   **Type** - boolean
        -   **Default** - true
    -   **AppData**
        -   **Type** - boolean
        -   **Default** - true
    -   **AppPublic**
        -   **Type** - boolean
        -   **Default** - true
-   **PredefineLogGroup**
    -   **Type** - boolean
    -   **Default** - false
-   **Environment**
    -   **AsFile**
        -   **Type** - boolean
        -   **Default** - false
    -   **Json**
    -   **Escaped**
        -   **Type** - boolean
        -   **Default** - true
    -   **Prefix**
        -   **Type** - string
        -   **Values** - json, 
        -   **Default** - json

* * *

# lb

A load balancer for virtual network based components

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Notes

!!! warning
	Requires second deployment to complete configuration

### Component Format

```json
[{"Name" : "Logs","Type" : "boolean","Default" : false},{"Name" : "Engine","Type" : "string","Values" : ["application","network","classic"],"Default" : "application"},{"Name" : "Profiles","Children" : [{"Name" : "SecurityProfile","Type" : "string","Default" : "default"}]},{"Name" : "IdleTimeout","Type" : "number","Default" : 60},{"Name" : "HealthCheckPort","Type" : "string","Default" : ""}]
```

### Attribute Reference

-   **Logs**
    -   **Type** - boolean
    -   **Default** - false
-   **Engine**
    -   **Type** - string
    -   **Values** - application, network, classic
    -   **Default** - application
-   **Profiles**
    -   **SecurityProfile**
        -   **Type** - string
        -   **Default** - default
-   **IdleTimeout**
    -   **Type** - number
    -   **Default** - 60
-   **HealthCheckPort**
    -   **Type** - string
    -   **Default** - null

* * *

# lbport

A specifc listener based on the client side network port

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Component Format

```json
[{"Name" : "IPAddressGroups","Type" : ["array","string"],"Default" : []},{"Name" : "Certificate","Type" : "object","Default" : {}},{"Name" : "HostFilter","Type" : "boolean","Default" : false},{"Name" : "Mapping","Type" : "string"},{"Name" : "Path","Type" : "string","Default" : "default"},{"Name" : "Priority","Type" : "number","Default" : 100},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]},{"Name" : "Authentication","Children" : [{"Name" : "SessionCookieName","Type" : "string","Default" : "AWSELBAuthSessionCookie"},{"Name" : "SessionTimeout","Type" : "number","Default" : 604800}]},{"Name" : "Redirect","Children" : [{"Name" : "Protocol","Type" : "string","Values" : ["HTTPS","#{protocol}"],"Default" : "HTTPS"},{"Name" : "Port","Type" : "string","Default" : "443"},{"Name" : "Host","Type" : "string","Default" : "#{host}"},{"Name" : "Path","Type" : "string","Default" : "\/#{path}"},{"Name" : "Query","Type" : "string","Default" : "#{query}"},{"Name" : "Permanent","Type" : "boolean","Default" : true}]},{"Name" : "Fixed","Children" : [{"Name" : "Message","Type" : "string","Default" : "This application is currently unavailable. Please try again later."},{"Name" : "ContentType","Type" : "string","Default" : "text/plain"},{"Name" : "StatusCode","Type" : "string","Default" : "404"}]},{"Name" : "Forward","Children" : [{"Name" : "TargetType","Type" : "string","Values" : ["instance","ip"],"Default" : "instance"},{"Name" : "SlowStartTime","Type" : "number","Default" : -1},{"Name" : "StickinessTime","Type" : "number","Default" : -1},{"Name" : "DeregistrationTimeout","Type" : "number","Default" : 30}]}]
```

### Attribute Reference

-   **IPAddressGroups**
    -   **Type** - array, string
    -   **Default** - \[]
-   **Certificate**
    -   **Type** - object
    -   **Default** - {}
-   **HostFilter**
    -   **Type** - boolean
    -   **Default** - false
-   **Mapping**
    -   **Type** - string
-   **Path**
    -   **Type** - string
    -   **Default** - default
-   **Priority**
    -   **Type** - number
    -   **Default** - 100
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **Authentication**
    -   **SessionCookieName**
        -   **Type** - string
        -   **Default** - AWSELBAuthSessionCookie
    -   **SessionTimeout**
        -   **Type** - number
        -   **Default** - 604800
-   **Redirect**
    -   **Protocol**
        -   **Type** - string
        -   **Values** - HTTPS, #{protocol}
        -   **Default** - HTTPS
    -   **Port**
        -   **Type** - string
        -   **Default** - 443
    -   **Host**
        -   **Type** - string
        -   **Default** - #{host}
    -   **Path**
        -   **Type** - string
        -   **Default** - /#{path}
    -   **Query**
        -   **Type** - string
        -   **Default** - #{query}
    -   **Permanent**
        -   **Type** - boolean
        -   **Default** - true
-   **Fixed**
    -   **Message**
        -   **Type** - string
        -   **Default** - This application is currently unavailable. Please try again later.
    -   **ContentType**
        -   **Type** - string
        -   **Default** - text/plain
    -   **StatusCode**
        -   **Type** - string
        -   **Default** - 404
-   **Forward**
    -   **TargetType**
        -   **Type** - string
        -   **Values** - instance, ip
        -   **Default** - instance
    -   **SlowStartTime**
        -   **Type** - number
        -   **Default** - -1
    -   **StickinessTime**
        -   **Type** - number
        -   **Default** - -1
    -   **DeregistrationTimeout**
        -   **Type** - number
        -   **Default** - 30

* * *

# mobilenotifier

A managed mobile notification proxy

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Component Format

```json
[{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]},{"Name" : "SuccessSampleRate","Type" : "string","Default" : "100"},{"Name" : "Credentials","Children" : [{"Name" : "EncryptionScheme","Type" : "string","Values" : ["base64"],"Default" : "base64"}]}]
```

### Attribute Reference

-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **SuccessSampleRate**
    -   **Type** - string
    -   **Default** - 100
-   **Credentials**
    -   **EncryptionScheme**
        -   **Type** - string
        -   **Values** - base64
        -   **Default** - base64

* * *

# mobilenotiferplatform

A specific mobile platform notification proxy

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Notes

!!! warning
	SMS Engine requires account level configuration for AWS provider
!!! info
	Platform specific credentials are required and must be provided as credentials

### Component Format

```json
[{"Name" : "Engine","Type" : "string"},{"Name" : "SuccessSampleRate","Type" : "string"},{"Name" : "Credentials","Children" : [{"Name" : "EncryptionScheme","Type" : "string","Values" : ["base64"]}]},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]},{"Name" : "LogMetrics","Subobjects" : true,"Children" : [{"Name" : "LogFilter","Type" : "string","Mandatory" : true}]}]
```

### Attribute Reference

-   **Engine**
    -   **Type** - string
-   **SuccessSampleRate**
    -   **Type** - string
-   **Credentials**
    -   **EncryptionScheme**
        -   **Type** - string
        -   **Values** - base64
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **LogMetrics**
    -   **LogFilter**
        -   **Type** - string
        -   **Mandatory** - true

* * *

# rds

A managed SQL database instance

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Component Format

```json
[{"Name" : "Engine","Mandatory" : true},{"Name" : "EngineVersion","Type" : "string"},{"Name" : "Port","Type" : "string"},{"Name" : "Encrypted","Type" : "boolean","Default" : false},{"Name" : "GenerateCredentials","Children" : [{"Name" : "Enabled","Type" : "boolean","Default" : false},{"Name" : "MasterUserName","Type" : "string","Default" : "root"},{"Name" : "CharacterLength","Type" : "number","Default" : 20},{"Name" : "EncryptionScheme","Type" : "string","Values" : ["base64"],"Default" : ""}]},{"Name" : "Size","Type" : "number","Default" : 20},{"Name" : "Backup","Children" : [{"Name" : "RetentionPeriod","Type" : "number","Default" : 35},{"Name" : "SnapshotOnDeploy","Type" : "boolean","Default" : true}]},{"Name" : "AutoMinorVersionUpgrade","Type" : "boolean"},{"Name" : "DatabaseName","Type" : "string"},{"Name" : "DBParameters","Type" : "object","Default" : {}}]
```

### Attribute Reference

-   **Engine**
    -   **Mandatory** - true
-   **EngineVersion**
    -   **Type** - string
-   **Port**
    -   **Type** - string
-   **Encrypted**
    -   **Type** - boolean
    -   **Default** - false
-   **GenerateCredentials**
    -   **Enabled**
        -   **Type** - boolean
        -   **Default** - false
    -   **MasterUserName**
        -   **Type** - string
        -   **Default** - root
    -   **CharacterLength**
        -   **Type** - number
        -   **Default** - 20
    -   **EncryptionScheme**
        -   **Type** - string
        -   **Values** - base64
        -   **Default** - null
-   **Size**
    -   **Type** - number
    -   **Default** - 20
-   **Backup**
    -   **RetentionPeriod**
        -   **Type** - number
        -   **Default** - 35
    -   **SnapshotOnDeploy**
        -   **Type** - boolean
        -   **Default** - true
-   **AutoMinorVersionUpgrade**
    -   **Type** - boolean
-   **DatabaseName**
    -   **Type** - string
-   **DBParameters**
    -   **Type** - object
    -   **Default** - {}

* * *

# s3

HTTP based object storage service

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Component Format

```json
[{"Name" : "Lifecycle","Children" : [{"Name" : "Expiration","Types" : ["string","number"],"Description" : "Provide either a date or a number of days"},{"Name" : "Offline","Types" : ["string","number"],"Description" : "Provide either a date or a number of days"},{"Name" : "Versioning","Type" : "boolean","Default" : false}]},{"Name" : "Website","Children" : [{"Name" : "Index","Type" : "string","Default" : "index.html"},{"Name" : "Error","Type" : "string","Default" : ""}]},{"Name" : "PublicAccess","Children" : [{"Name" : "Enabled","Type" : "boolean","Default" : false},{"Name" : "Permissions","Type" : "string","Values" : ["ro","wo","rw"],"Default" : "ro"},{"Name" : "IPAddressGroups","Type" : ["array","string"],"Default" : ["_localnet"]},{"Name" : "Prefix","Type" : "string","Default" : ""}]},{"Name" : "Style","Type" : "string","Description" : "TODO(mfl): Think this can be removed"},{"Name" : "Notifications","Type" : "object"},{"Name" : "CORSBehaviours","Type" : ["array","string"],"Default" : []}]
```

### Attribute Reference

-   **Lifecycle**
    -   **Expiration**
        -   **Types** - string, number
        -   **Description** - Provide either a date or a number of days
    -   **Offline**
        -   **Types** - string, number
        -   **Description** - Provide either a date or a number of days
    -   **Versioning**
        -   **Type** - boolean
        -   **Default** - false
-   **Website**
    -   **Index**
        -   **Type** - string
        -   **Default** - index.html
    -   **Error**
        -   **Type** - string
        -   **Default** - null
-   **PublicAccess**
    -   **Enabled**
        -   **Type** - boolean
        -   **Default** - false
    -   **Permissions**
        -   **Type** - string
        -   **Values** - ro, wo, rw
        -   **Default** - ro
    -   **IPAddressGroups**
        -   **Type** - array, string
        -   **Default** - \_localnet
    -   **Prefix**
        -   **Type** - string
        -   **Default** - null
-   **Style**
    -   **Type** - string
    -   **Description** - TODO(mfl): Think this can be removed
-   **Notifications**
    -   **Type** - object
-   **CORSBehaviours**
    -   **Type** - array, string
    -   **Default** - \[]

* * *

# spa

Object stored hosted web application with content distribution management

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

### Component Format

```json
[{"Name" : ["Fragment","Container"],"Type" : "string","Default" : ""},{"Name" : "Links","Type" : "object","Default" : {}},{"Name" : "WAF","Children" : [{"Name" : "IPAddressGroups","Type" : ["array","string"],"Mandatory" : true},{"Name" : "Default","Type" : "string","Values" : ["ALLOW","BLOCK"],"Default" : "BLOCK"},{"Name" : "RuleDefault","Type" : "string","Values" : ["ALLOW","BLOCK"],"Default" : "ALLOW"}]},{"Name" : "CloudFront","Children" : [{"Name" : "AssumeSNI","Type" : "boolean","Default" : true},{"Name" : "EnableLogging","Type" : "boolean","Default" : true},{"Name" : "CountryGroups","Type" : ["array","string"],"Default" : []},{"Name" : "ErrorPage","Type" : "string","Default" : "\/index.html"},{"Name" : "DeniedPage","Type" : "string","Default" : ""},{"Name" : "NotFoundPage","Type" : "string","Default" : ""},{"Name" : "CachingTTL","Children" : [{"Name" : "Default","Type" : "number","Default" : 600},{"Name" : "Maximum","Type" : "number","Default" : 31536000},{"Name" : "Minimum","Type" : "number","Default" : 0}]},{"Name" : "Compress","Type" : "boolean","Default" : true}]},{"Name" : "Certificate","Children" : [{"Name" : "*"}]},{"Name" : "Profiles","Children" : [{"Name" : "SecurityProfile","Type" : "string","Default" : "default"}]}]
```

### Attribute Reference

-   **Fragment**
    -   **Alternate Names** - Container
    -   **Type** - string
    -   **Default** - null
-   **Links**
    -   **Type** - object
    -   **Default** - {}
-   **WAF**
    -   **IPAddressGroups**
        -   **Type** - array, string
        -   **Mandatory** - true
    -   **Default**
        -   **Type** - string
        -   **Values** - ALLOW, BLOCK
        -   **Default** - BLOCK
    -   **RuleDefault**
        -   **Type** - string
        -   **Values** - ALLOW, BLOCK
        -   **Default** - ALLOW
-   **CloudFront**
    -   **AssumeSNI**
        -   **Type** - boolean
        -   **Default** - true
    -   **EnableLogging**
        -   **Type** - boolean
        -   **Default** - true
    -   **CountryGroups**
        -   **Type** - array, string
        -   **Default** - \[]
    -   **ErrorPage**
        -   **Type** - string
        -   **Default** - /index.html
    -   **DeniedPage**
        -   **Type** - string
        -   **Default** - null
    -   **NotFoundPage**
        -   **Type** - string
        -   **Default** - null
    -   **CachingTTL**
    -   **Default**
        -   **Type** - number
        -   **Default** - 600
    -   **Maximum**
        -   **Type** - number
        -   **Default** - 31536000
    -   **Minimum**
        -   **Type** - number
        -   **Default** - 0
    -   **Compress**
        -   **Type** - boolean
        -   **Default** - true
-   **Certificate**
    -   * * *
-   **Profiles**
    -   **SecurityProfile**
        -   **Type** - string
        -   **Default** - default

* * *

# sqs

Managed worker queue engine

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

### Component Format

```json
[{"Name" : "DelaySeconds","Type" : "number"},{"Name" : "MaximumMessageSize","Type" : "number"},{"Name" : "MessageRetentionPeriod","Type" : "number"},{"Name" : "ReceiveMessageWaitTimeSeconds","Type" : "number"},{"Name" : "DeadLetterQueue","Children" : [{"Name" : "MaxReceives","Type" : "number","Default" : 0}]},{"Name" : "VisibilityTimeout","Type" : "number"}]
```

### Attribute Reference

-   **DelaySeconds**
    -   **Type** - number
-   **MaximumMessageSize**
    -   **Type** - number
-   **MessageRetentionPeriod**
    -   **Type** - number
-   **ReceiveMessageWaitTimeSeconds**
    -   **Type** - number
-   **DeadLetterQueue**
    -   **MaxReceives**
        -   **Type** - number
        -   **Default** - 0
-   **VisibilityTimeout**
    -   **Type** - number

* * *

# user

A user with permissions on components deployed in the solution

### Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

### Component Format

```json
[{"Name" : ["Fragment","Container"],"Type" : "string","Default" : ""},{"Name" : "Links","Subobjects" : true,"Children" : [{"Name" : "Any","Type" : "string"},{"Name" : "Tenant","Type" : "string"},{"Name" : "Product","Type" : "string"},{"Name" : "Environment","Type" : "string"},{"Name" : "Segment","Type" : "string"},{"Name" : "Tier","Type" : "string","Mandatory" : true},{"Name" : "Component","Type" : "string","Mandatory" : true},{"Name" : ["Function"],"Type" : "string"},{"Name" : ["Service"],"Type" : "string"},{"Name" : ["Task"],"Type" : "string"},{"Name" : ["PortMapping","Port"],"Type" : "string"},{"Name" : ["Mount"],"Type" : "string"},{"Name" : ["Platform"],"Type" : "string"},{"Name" : "Instance","Type" : "string"},{"Name" : "Version","Type" : "string"},{"Name" : "Role","Type" : "string"},{"Name" : "Direction","Type" : "string"}]},{"Name" : "GenerateCredentials","Children" : [{"Name" : "Formats","Type" : ["array","string"],"Values" : ["system","console"],"Default" : ["system"]},{"Name" : "EncryptionScheme","Type" : "string","Values" : ["base64"],"Default" : ""},{"Name" : "CharacterLength","Type" : "number","Default" : 20}]},{"Name" : "Permissions","Children" : [{"Name" : "Decrypt","Type" : "boolean","Default" : true},{"Name" : "AsFile","Type" : "boolean","Default" : true},{"Name" : "AppData","Type" : "boolean","Default" : true},{"Name" : "AppPublic","Type" : "boolean","Default" : true}]}]
```

### Attribute Reference

-   **Fragment**
    -   **Alternate Names** - Container
    -   **Type** - string
    -   **Default** - null
-   **Links**
    -   **Any**
        -   **Type** - string
    -   **Tenant**
        -   **Type** - string
    -   **Product**
        -   **Type** - string
    -   **Environment**
        -   **Type** - string
    -   **Segment**
        -   **Type** - string
    -   **Tier**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Component**
        -   **Type** - string
        -   **Mandatory** - true
    -   **Function**
        -   **Type** - string
    -   **Service**
        -   **Type** - string
    -   **Task**
        -   **Type** - string
    -   **PortMapping**
        -   **Alternate Names** - Port
        -   **Type** - string
    -   **Mount**
        -   **Type** - string
    -   **Platform**
        -   **Type** - string
    -   **Instance**
        -   **Type** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **GenerateCredentials**
    -   **Formats**
        -   **Type** - array, string
        -   **Values** - system, console
        -   **Default** - system
    -   **EncryptionScheme**
        -   **Type** - string
        -   **Values** - base64
        -   **Default** - null
    -   **CharacterLength**
        -   **Type** - number
        -   **Default** - 20
-   **Permissions**
    -   **Decrypt**
        -   **Type** - boolean
        -   **Default** - true
    -   **AsFile**
        -   **Type** - boolean
        -   **Default** - true
    -   **AppData**
        -   **Type** - boolean
        -   **Default** - true
    -   **AppPublic**
        -   **Type** - boolean
        -   **Default** - true

* * *
