# apigateway

Application level API proxy

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"Fragment" : "<string>",
	"Links" : "<object>",
	"WAF" : {
		"IPAddressGroups" : "<array of string>",
		"Default" : "BLOCK",
		"RuleDefault" : "ALLOW"
	},
	"EndpointType" : "EDGE",
	"IPAddressGroups" : "<array of string>",
	"Authentication" : "IP",
	"CloudFront" : {
		"AssumeSNI" : true,
		"EnableLogging" : true,
		"CountryGroups" : "<array of string>",
		"CustomHeaders" : "<array of any>",
		"Mapping" : false,
		"Compress" : true
	},
	"Certificate" : {
		"*" : "<unknown>"
	},
	"Publish" : {
		"DnsNamePrefix" : "docs",
		"IPAddressGroups" : "<array of string>"
	},
	"Mapping" : {
		"IncludeStage" : true
	},
	"Profiles" : {
		"SecurityProfile" : "default"
	}
}
```

## Attribute Reference

-   **Fragment**
    -   **Alternate Names** - Container
    -   **Type** - string
    -   **Default** - null
-   **Links**
    -   **Type** - object
    -   **Default** - {}
-   **WAF**
    -   **IPAddressGroups**
        -   **Type** - array of string
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
    -   **Type** - array of string
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
        -   **Type** - array of string
        -   **Default** - \[]
    -   **CustomHeaders**
        -   **Type** - array of any
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
        -   **Type** - array of string
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

# apiusageplan

provides a metered link between an API gateway and an invoking client

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	}
}
```

## Attribute Reference

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
        -   **Types** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string

* * *

# cache

Managed in-memory cache services

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"Engine" : "<string>",
	"EngineVersion" : "<string>",
	"Port" : "<string>",
	"Backup" : {
		"RetentionPeriod" : "<string>"
	}
}
```

## Attribute Reference

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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Notes

!!! warning
    Requires second deployment to complete configuration

## Component Format

```json
{
	"MFA" : false,
	"AdminCreatesUser" : true,
	"UnusedAccountTimeout" : 7,
	"VerifyEmail" : true,
	"VerifyPhone" : false,
	"LoginAliases" : [
		"email"
	],
	"ClientGenerateSecret" : false,
	"ClientTokenValidity" : 30,
	"AllowUnauthenticatedIds" : false,
	"AuthorizationHeader" : "Authorization",
	"OAuth" : {
		"Scopes" : [
			"openid"
		],
		"Flows" : [
			"code"
		]
	},
	"PasswordPolicy" : {
		"MinimumLength" : 10,
		"Lowercase" : true,
		"Uppercase" : true,
		"Numbers" : true,
		"SpecialCharacters" : true
	},
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	}
}
```

## Attribute Reference

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
    -   **Type** - array of string
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
        -   **Type** - array of string
        -   **Default** - openid
    -   **Flows**
        -   **Type** - array of string
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
        -   **Types** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string

* * *

# computecluster

Auto-Scaling IaaS with code deployment

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"Fragment" : "<string>",
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	},
	"UseInitAsService" : false,
	"MinUpdateInstances" : 1,
	"ReplaceOnUpdate" : false,
	"UpdatePauseTime" : "5M",
	"StartupTimeout" : "15M",
	"DockerHost" : false,
	"Ports" : {
		"example" : {
			"IPAddressGroups" : "<array of string>",
			"LB" : {
				"Tier" : "<string>",
				"Component" : "<string>",
				"LinkName" : "lb",
				"Instance" : "<string>",
				"Version" : "<string>",
				"PortMapping" : "<string>"
			}
		}
	}
}
```

## Attribute Reference

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
        -   **Types** - string
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
        -   **Type** - array of string
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

## Deployment Properties

-   **Available Providers** - github
-   **Component Level** - application

## Component Format

```json
{
	"Prefix" : "<string>",
	"Engine" : "github",
	"Branch" : "master",
	"Repository" : "<string>"
}
```

## Attribute Reference

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

## Deployment Properties

-   **Available Providers** - github
-   **Component Level** - application

## Component Format

```json
{
	"Path" : {
		"Host" : "<string>",
		"Style" : "single",
		"IncludeInPath" : {
			"Product" : true,
			"Environment" : false,
			"Solution" : false,
			"Segment" : true,
			"Tier" : false,
			"Component" : false,
			"Instance" : false,
			"Version" : false,
			"Host" : false
		}
	},
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	}
}
```

## Attribute Reference

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
        -   **Types** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string

* * *

# datapipeline

Managed Data ETL Processing

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"Fragment" : "<string>",
	"Permissions" : {
		"Decrypt" : true,
		"AsFile" : true,
		"AppData" : true,
		"AppPublic" : true
	},
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	}
}
```

## Attribute Reference

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
        -   **Types** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string

* * *

# dataset

A data aretefact that is managed in a similar way to a code unit

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"Engine" : "<string>",
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	},
	"Prefix" : "<string>"
}
```

## Attribute Reference

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
        -   **Types** - string
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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"FixedIP" : false,
	"DockerHost" : false,
	"Fragment" : "<string>",
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	},
	"Ports" : {
		"example" : {
			"IPAddressGroups" : "<array of string>",
			"LB" : {
				"Tier" : "<string>",
				"Component" : "<string>",
				"LinkName" : "lb",
				"Instance" : "<string>",
				"Version" : "<string>",
				"PortMapping" : "<string>"
			}
		}
	}
}
```

## Attribute Reference

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
        -   **Types** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **Ports**
    -   **IPAddressGroups**
        -   **Type** - array of string
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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Sub Components

-   [service](#service)
    -   **Component Attribute** - Services
    -   **Link Attribute** - Service
-   [task](#task)
    -   **Component Attribute** - Tasks
    -   **Link Attribute** - Task

## Component Format

```json
{
	"Fragment" : "<string>",
	"FixedIP" : false,
	"LogDriver" : "awslogs",
	"ClusterLogGroup" : true,
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	},
	"DockerUsers" : {
		"example" : {
			"UserName" : "<string>",
			"UID" : "<number>"
		}
	},
	"Services" : {
		"example" : "< instance of service>"
	},
	"Tasks" : {
		"example" : "< instance of task>"
	}
}
```

## Attribute Reference

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
        -   **Types** - string
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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"Containers" : {
		"example" : {
			"Cpu" : "<number>",
			"Links" : {
				"example" : {
					"Any" : "<string>",
					"Tenant" : "<string>",
					"Product" : "<string>",
					"Environment" : "<string>",
					"Segment" : "<string>",
					"Tier" : "<string>",
					"Component" : "<string>",
					"Function" : "<string>",
					"Service" : "<string>",
					"Task" : "<string>",
					"PortMapping" : "<string>",
					"Mount" : "<string>",
					"Platform" : "<string>",
					"Instance" : "<unknown>",
					"Version" : "<string>",
					"Role" : "<string>",
					"Direction" : "<string>"
				}
			},
			"LocalLogging" : false,
			"LogDriver" : "awslogs",
			"ContainerLogGroup" : false,
			"RunCapabilities" : "<array of string>",
			"Privileged" : false,
			"MaximumMemory" : "<unknown>",
			"MemoryReservation" : "<number>",
			"Ports" : {
				"example" : {
					"Container" : "unknown",
					"DynamicHostPort" : false,
					"LB" : {
						"Tier" : "<string>",
						"Component" : "<string>",
						"LinkName" : "lb",
						"Instance" : "<string>",
						"Version" : "<string>",
						"PortMapping" : "<string>"
					},
					"IPAddressGroups" : "<array of string>"
				}
			},
			"Version" : "<string>",
			"ContainerNetworkLinks" : "<array of string>"
		}
	},
	"DesiredCount" : -1,
	"UseTaskRole" : true,
	"Permissions" : {
		"Decrypt" : true,
		"AsFile" : true,
		"AppData" : true,
		"AppPublic" : true
	},
	"TaskLogGroup" : true,
	"NetworkMode" : "<string>",
	"ContainerNetworkLinks" : false
}
```

## Attribute Reference

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
        -   **Types** - string
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
        -   **Type** - array of string
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
        -   **Name** - Container
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
        -   **Type** - array of string
        -   **Default** - \[]
    -   **Version**
        -   **Type** - string
        -   **Default** - null
    -   **ContainerNetworkLinks**
        -   **Type** - array of string
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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"Containers" : {
		"example" : {
			"Cpu" : "<number>",
			"Links" : {
				"example" : {
					"Any" : "<string>",
					"Tenant" : "<string>",
					"Product" : "<string>",
					"Environment" : "<string>",
					"Segment" : "<string>",
					"Tier" : "<string>",
					"Component" : "<string>",
					"Function" : "<string>",
					"Service" : "<string>",
					"Task" : "<string>",
					"PortMapping" : "<string>",
					"Mount" : "<string>",
					"Platform" : "<string>",
					"Instance" : "<unknown>",
					"Version" : "<string>",
					"Role" : "<string>",
					"Direction" : "<string>"
				}
			},
			"LocalLogging" : false,
			"LogDriver" : "awslogs",
			"ContainerLogGroup" : false,
			"RunCapabilities" : "<array of string>",
			"Privileged" : false,
			"MaximumMemory" : "<unknown>",
			"MemoryReservation" : "<number>",
			"Ports" : {
				"example" : {
					"Container" : "unknown",
					"DynamicHostPort" : false,
					"LB" : {
						"Tier" : "<string>",
						"Component" : "<string>",
						"LinkName" : "lb",
						"Instance" : "<string>",
						"Version" : "<string>",
						"PortMapping" : "<string>"
					},
					"IPAddressGroups" : "<array of string>"
				}
			},
			"Version" : "<string>",
			"ContainerNetworkLinks" : "<array of string>"
		}
	},
	"UseTaskRole" : true,
	"Permissions" : {
		"Decrypt" : true,
		"AsFile" : true,
		"AppData" : true,
		"AppPublic" : true
	},
	"TaskLogGroup" : true,
	"FixedName" : false
}
```

## Attribute Reference

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
        -   **Types** - string
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
        -   **Type** - array of string
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
        -   **Name** - Container
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
        -   **Type** - array of string
        -   **Default** - \[]
    -   **Version**
        -   **Type** - string
        -   **Default** - null
    -   **ContainerNetworkLinks**
        -   **Type** - array of string
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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Sub Components

-   [efsMount](#efsMount)
    -   **Component Attribute** - Mounts
    -   **Link Attribute** - Mount

## Component Format

```json
{
	"Encrypted" : true,
	"Mounts" : {
		"example" : "< instance of efsMount>"
	}
}
```

## Attribute Reference

-   **Encrypted**
    -   **Type** - boolean
    -   **Default** - true

* * *

# efsmount

A specific directory on the share for OS mounting

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"Directory" : "<string>"
}
```

## Attribute Reference

-   **Directory**
    -   **Type** - string
    -   **Mandatory** - true

* * *

# es

A managed ElasticSearch instance

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"Authentication" : "IP",
	"IPAddressGroups" : "<array of string>",
	"AdvancedOptions" : "<array of string>",
	"Version" : "2.3",
	"Encrypted" : false,
	"Snapshot" : {
		"Hour" : "<string>"
	},
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	}
}
```

## Attribute Reference

-   **Authentication**
    -   **Type** - string
    -   **Values** - IP, SIG4ORIP, SIG4ANDIP
    -   **Default** - IP
-   **IPAddressGroups**
    -   **Type** - array of string
    -   **Mandatory** - true
-   **AdvancedOptions**
    -   **Type** - array of string
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
        -   **Types** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string

* * *

# lambda

Container for a Function as a Service deployment

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Sub Components

-   [function](#function)
    -   **Component Attribute** - Functions
    -   **Link Attribute** - Function

## Component Format

```json
{
	"Functions" : {
		"example" : "< instance of function>"
	}
}
```

## Attribute Reference

* * *

# function

A specific entry point for the lambda deployment

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"Fragment" : "<string>",
	"Handler" : "<string>",
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	},
	"LogMetrics" : {
		"example" : {
			"LogFilter" : "<string>"
		}
	},
	"LogWatchers" : {
		"example" : {
			"LogFilter" : "<string>",
			"Links" : {
				"example" : {
					"Any" : "<string>",
					"Tenant" : "<string>",
					"Product" : "<string>",
					"Environment" : "<string>",
					"Segment" : "<string>",
					"Tier" : "<string>",
					"Component" : "<string>",
					"Function" : "<string>",
					"Service" : "<string>",
					"Task" : "<string>",
					"PortMapping" : "<string>",
					"Mount" : "<string>",
					"Platform" : "<string>",
					"Instance" : "<unknown>",
					"Version" : "<string>",
					"Role" : "<string>",
					"Direction" : "<string>"
				}
			}
		}
	},
	"Alerts" : {
		"example" : {
			"Description" : "unknown",
			"Name" : "<string>",
			"Metric" : {
				"Name" : "<string>",
				"Type" : "<string>"
			},
			"Threshold" : 1,
			"Severity" : "Info",
			"Namespace" : "<string>",
			"Comparison" : "Threshold",
			"Operator" : "GreaterThanOrEqualToThreshold",
			"Time" : 300,
			"Periods" : 1,
			"Statistic" : "Sum",
			"ReportOk" : false,
			"MissingData" : "notBreaching"
		}
	},
	"Memory" : 0,
	"RunTime" : "<string>",
	"Schedules" : {
		"example" : {
			"Expression" : "rate(6 minutes)",
			"InputPath" : "/healthcheck",
			"Input" : "<object>"
		}
	},
	"Timeout" : 0,
	"VPCAccess" : true,
	"UseSegmentKey" : false,
	"Permissions" : {
		"Decrypt" : true,
		"AsFile" : true,
		"AppData" : true,
		"AppPublic" : true
	},
	"PredefineLogGroup" : false,
	"Environment" : {
		"AsFile" : false,
		"Json" : {
			"Escaped" : true,
			"Prefix" : "json"
		}
	}
}
```

## Attribute Reference

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
        -   **Types** - string
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
        -   **Types** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **Alerts**
    -   **Name** - Description
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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Notes

!!! warning
    Requires second deployment to complete configuration

## Sub Components

-   [lbport](#lbport)
    -   **Component Attribute** - PortMappings
    -   **Link Attribute** - PortMapping, Port

## Component Format

```json
{
	"Logs" : false,
	"Engine" : "application",
	"Profiles" : {
		"SecurityProfile" : "default"
	},
	"IdleTimeout" : 60,
	"HealthCheckPort" : "<string>",
	"PortMappings" : {
		"example" : "< instance of lbport>"
	}
}
```

## Attribute Reference

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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"IPAddressGroups" : "<array of string>",
	"Certificate" : "<object>",
	"HostFilter" : false,
	"Mapping" : "<string>",
	"Path" : "default",
	"Priority" : 100,
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	},
	"Authentication" : {
		"SessionCookieName" : "AWSELBAuthSessionCookie",
		"SessionTimeout" : 604800
	},
	"Redirect" : {
		"Protocol" : "HTTPS",
		"Port" : "443",
		"Host" : "#{host}",
		"Path" : "/#{path}",
		"Query" : "#{query}",
		"Permanent" : true
	},
	"Fixed" : {
		"Message" : "This application is currently unavailable. Please try again later.",
		"ContentType" : "text/plain",
		"StatusCode" : "404"
	},
	"Forward" : {
		"TargetType" : "instance",
		"SlowStartTime" : -1,
		"StickinessTime" : -1,
		"DeregistrationTimeout" : 30
	}
}
```

## Attribute Reference

-   **IPAddressGroups**
    -   **Type** - array of string
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
        -   **Types** - string
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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Sub Components

-   [mobilenotiferplatform](#mobilenotiferplatform)
    -   **Component Attribute** - Platforms
    -   **Link Attribute** - Platform

## Component Format

```json
{
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	},
	"SuccessSampleRate" : "100",
	"Credentials" : {
		"EncryptionScheme" : "base64"
	},
	"Platforms" : {
		"example" : "< instance of mobilenotiferplatform>"
	}
}
```

## Attribute Reference

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
        -   **Types** - string
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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Notes

!!! warning
    SMS Engine requires account level configuration for AWS provider
!!! info
    Platform specific credentials are required and must be provided as credentials

## Component Format

```json
{
	"Engine" : "<string>",
	"SuccessSampleRate" : "<string>",
	"Credentials" : {
		"EncryptionScheme" : "<string>"
	},
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	},
	"LogMetrics" : {
		"example" : {
			"LogFilter" : "<string>"
		}
	}
}
```

## Attribute Reference

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
        -   **Types** - string
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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"Engine" : "<unknown>",
	"EngineVersion" : "<string>",
	"Port" : "<string>",
	"Encrypted" : false,
	"GenerateCredentials" : {
		"Enabled" : false,
		"MasterUserName" : "root",
		"CharacterLength" : 20,
		"EncryptionScheme" : "<string>"
	},
	"Size" : 20,
	"Backup" : {
		"RetentionPeriod" : 35,
		"SnapshotOnDeploy" : true
	},
	"AutoMinorVersionUpgrade" : "<boolean>",
	"DatabaseName" : "<string>",
	"DBParameters" : "<object>"
}
```

## Attribute Reference

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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"Lifecycle" : {
		"Expiration" : "<unknown>",
		"Offline" : "<unknown>",
		"Versioning" : false
	},
	"Website" : {
		"Index" : "index.html",
		"Error" : "<string>"
	},
	"PublicAccess" : {
		"Enabled" : false,
		"Permissions" : "ro",
		"IPAddressGroups" : [
			"_localnet"
		],
		"Prefix" : "<string>"
	},
	"Style" : "<string>",
	"Notifications" : "<object>",
	"CORSBehaviours" : "<array of string>"
}
```

## Attribute Reference

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
        -   **Type** - array of string
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
    -   **Type** - array of string
    -   **Default** - \[]

* * *

# spa

Object stored hosted web application with content distribution management

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"Fragment" : "<string>",
	"Links" : "<object>",
	"WAF" : {
		"IPAddressGroups" : "<array of string>",
		"Default" : "BLOCK",
		"RuleDefault" : "ALLOW"
	},
	"CloudFront" : {
		"AssumeSNI" : true,
		"EnableLogging" : true,
		"CountryGroups" : "<array of string>",
		"ErrorPage" : "/index.html",
		"DeniedPage" : "<string>",
		"NotFoundPage" : "<string>",
		"CachingTTL" : {
			"Default" : 600,
			"Maximum" : 31536000,
			"Minimum" : 0
		},
		"Compress" : true
	},
	"Certificate" : {
		"*" : "<unknown>"
	},
	"Profiles" : {
		"SecurityProfile" : "default"
	}
}
```

## Attribute Reference

-   **Fragment**
    -   **Alternate Names** - Container
    -   **Type** - string
    -   **Default** - null
-   **Links**
    -   **Type** - object
    -   **Default** - {}
-   **WAF**
    -   **IPAddressGroups**
        -   **Type** - array of string
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
        -   **Type** - array of string
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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"DelaySeconds" : "<number>",
	"MaximumMessageSize" : "<number>",
	"MessageRetentionPeriod" : "<number>",
	"ReceiveMessageWaitTimeSeconds" : "<number>",
	"DeadLetterQueue" : {
		"MaxReceives" : 0
	},
	"VisibilityTimeout" : "<number>"
}
```

## Attribute Reference

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

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"Fragment" : "<string>",
	"Links" : {
		"example" : {
			"Any" : "<string>",
			"Tenant" : "<string>",
			"Product" : "<string>",
			"Environment" : "<string>",
			"Segment" : "<string>",
			"Tier" : "<string>",
			"Component" : "<string>",
			"Function" : "<string>",
			"Service" : "<string>",
			"Task" : "<string>",
			"PortMapping" : "<string>",
			"Mount" : "<string>",
			"Platform" : "<string>",
			"Instance" : "<unknown>",
			"Version" : "<string>",
			"Role" : "<string>",
			"Direction" : "<string>"
		}
	},
	"GenerateCredentials" : {
		"Formats" : [
			"system"
		],
		"EncryptionScheme" : "<string>",
		"CharacterLength" : 20
	},
	"Permissions" : {
		"Decrypt" : true,
		"AsFile" : true,
		"AppData" : true,
		"AppPublic" : true
	}
}
```

## Attribute Reference

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
        -   **Types** - string
    -   **Version**
        -   **Type** - string
    -   **Role**
        -   **Type** - string
    -   **Direction**
        -   **Type** - string
-   **GenerateCredentials**
    -   **Formats**
        -   **Type** - array of string
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
