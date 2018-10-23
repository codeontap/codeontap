# apigateway

Application level API proxy

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"apigateway" : {
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
}
```

## Attribute Reference

-   [Fragment](#Fragment) _(Container)_ - Optional - **Type:** string  
-   [Links](#Links) - Optional - **Type:** object  
-   [WAF](#WAF)
    -   [IPAddressGroups](#IPAddressGroups) - Required - **Type:** array of string  
    -   [Default](#Default) - Optional - **Type:** string  
        **Possible Values:** `[ALLOW, BLOCK]`  
        **Default:** `BLOCK`  
    -   [RuleDefault](#RuleDefault) - Optional - **Type:** string  
        **Possible Values:** `[ALLOW, BLOCK]`  
        **Default:** `ALLOW`  
-   [EndpointType](#EndpointType) - Optional - **Type:** string  
    **Possible Values:** `[EDGE, REGIONAL]`  
    **Default:** `EDGE`  
-   [IPAddressGroups](#IPAddressGroups) - Optional - **Type:** array of string  
-   [Authentication](#Authentication) - Optional - **Type:** string  
    **Possible Values:** `[IP, SIG4ORIP, SIG4ANDIP]`  
    **Default:** `IP`  
-   [CloudFront](#CloudFront)
    -   [AssumeSNI](#AssumeSNI) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [EnableLogging](#EnableLogging) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [CountryGroups](#CountryGroups) - Optional - **Type:** array of string  
    -   [CustomHeaders](#CustomHeaders) - Optional - **Type:** array of any  
    -   [Mapping](#Mapping) - Optional - **Type:** boolean  
        **Default:** `false`  
    -   [Compress](#Compress) - Optional - **Type:** boolean  
        **Default:** `true`  
-   [Certificate](#Certificate)
    -   [\*](#*) - Optional  
-   [Publish](#Publish)
    -   [DnsNamePrefix](#DnsNamePrefix) - Optional - **Type:** string  
        **Default:** `docs`  
    -   [IPAddressGroups](#IPAddressGroups) - Optional - **Type:** array of string  
-   [Mapping](#Mapping)
    -   [IncludeStage](#IncludeStage) - Optional - **Type:** boolean  
        **Default:** `true`  
-   [Profiles](#Profiles)
    -   [SecurityProfile](#SecurityProfile) - Optional - **Type:** string  
        **Default:** `default`  

* * *

# apiusageplan

provides a metered link between an API gateway and an invoking client

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"apiusageplan" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
			}
		}
	}
}
```

## Attribute Reference

-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  

* * *

# cache

Managed in-memory cache services

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"cache" : {
		"Engine" : "<string>",
		"EngineVersion" : "<string>",
		"Port" : "<string>",
		"Backup" : {
			"RetentionPeriod" : "<string>"
		}
	}
}
```

## Attribute Reference

-   [Engine](#Engine) - Required - **Type:** string  
-   [EngineVersion](#EngineVersion) - Optional - **Type:** string  
-   [Port](#Port) - Optional - **Type:** string  
-   [Backup](#Backup)
    -   [RetentionPeriod](#RetentionPeriod) - Optional - **Type:** string  

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
	"userpool" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
			}
		}
	}
}
```

## Attribute Reference

-   [MFA](#MFA) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [AdminCreatesUser](#AdminCreatesUser) - Optional - **Type:** boolean  
    **Default:** `true`  
-   [UnusedAccountTimeout](#UnusedAccountTimeout) - Optional - **Type:** number  
    **Default:** `7`  
-   [VerifyEmail](#VerifyEmail) - Optional - **Type:** boolean  
    **Default:** `true`  
-   [VerifyPhone](#VerifyPhone) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [LoginAliases](#LoginAliases) - Optional - **Type:** array of string  
    **Default:** `email`  
-   [ClientGenerateSecret](#ClientGenerateSecret) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [ClientTokenValidity](#ClientTokenValidity) - Optional - **Type:** number  
    **Default:** `30`  
-   [AllowUnauthenticatedIds](#AllowUnauthenticatedIds) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [AuthorizationHeader](#AuthorizationHeader) - Optional - **Type:** string  
    **Default:** `Authorization`  
-   [OAuth](#OAuth)
    -   [Scopes](#Scopes) - Optional - **Type:** array of string  
        **Default:** `openid`  
    -   [Flows](#Flows) - Optional - **Type:** array of string  
        **Default:** `code`  
-   [PasswordPolicy](#PasswordPolicy)
    -   [MinimumLength](#MinimumLength) - Optional - **Type:** number  
        **Default:** `10`  
    -   [Lowercase](#Lowercase) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [Uppercase](#Uppercase) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [Numbers](#Numbers) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [SpecialCharacters](#SpecialCharacters) - Optional - **Type:** boolean  
        **Default:** `true`  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  

* * *

# computecluster

Auto-Scaling IaaS with code deployment

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"computecluster" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
			}
		},
		"UseInitAsService" : false,
		"AutoScaling" : {
			"WaitForSignal" : true,
			"MinUpdateInstances" : 1,
			"ReplaceCluster" : false,
			"UpdatePauseTime" : "5M",
			"StartupTimeout" : "15M",
			"AlwaysReplaceOnUpdate" : false,
			"ActivityCooldown" : 30
		},
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
}
```

## Attribute Reference

-   [Fragment](#Fragment) _(Container)_ - Optional - **Type:** string  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
-   [UseInitAsService](#UseInitAsService) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [AutoScaling](#AutoScaling)
    -   [WaitForSignal](#WaitForSignal) - Optional - **Type:** boolean  
        **Default:** `true`  
        **Description:** Wait for a cfn-signal before treating the instances as alive  
    -   [MinUpdateInstances](#MinUpdateInstances) - Optional - **Type:** number  
        **Default:** `1`  
        **Description:** The minimum number of instances which must be available during an update  
    -   [ReplaceCluster](#ReplaceCluster) - Optional - **Type:** boolean  
        **Default:** `false`  
        **Description:** When set to true a brand new cluster will be built, if false the instances in the current cluster will be replaced  
    -   [UpdatePauseTime](#UpdatePauseTime) - Optional - **Type:** string  
        **Default:** `5M`  
        **Description:** How long to pause betweeen updates of instances  
    -   [StartupTimeout](#StartupTimeout) - Optional - **Type:** string  
        **Default:** `15M`  
        **Description:** How long to wait for a cfn-signal to be received from a host  
    -   [AlwaysReplaceOnUpdate](#AlwaysReplaceOnUpdate) - Optional - **Type:** boolean  
        **Default:** `false`  
        **Description:** Replace instances on every update action  
    -   [ActivityCooldown](#ActivityCooldown) - Optional - **Type:** number  
        **Default:** `30`  
-   [DockerHost](#DockerHost) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [Ports](#Ports)
    -   [IPAddressGroups](#IPAddressGroups) - Optional - **Type:** array of string  
    -   [LB](#LB)
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [LinkName](#LinkName) - Optional - **Type:** string  
          **Default:** `lb`  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  

* * *

# contenthub

Hub for decentralised content hosting with centralised publishing

## Deployment Properties

-   **Available Providers** - github
-   **Component Level** - application

## Component Format

```json
{
	"contenthub" : {
		"Prefix" : "<string>",
		"Engine" : "github",
		"Branch" : "master",
		"Repository" : "<string>"
	}
}
```

## Attribute Reference

-   [Prefix](#Prefix) - Required - **Type:** string  
-   [Engine](#Engine) - Optional - **Type:** string  
    **Default:** `github`  
-   [Branch](#Branch) - Optional - **Type:** string  
    **Default:** `master`  
-   [Repository](#Repository) - Optional - **Type:** string  

* * *

# contentnode

Node for decentralised content hosting with centralised publishing

## Deployment Properties

-   **Available Providers** - github
-   **Component Level** - application

## Component Format

```json
{
	"contentnode" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
			}
		}
	}
}
```

## Attribute Reference

-   [Path](#Path)
    -   [Host](#Host) - Optional - **Type:** string  
    -   [Style](#Style) - Optional - **Type:** string  
        **Default:** `single`  
    -   [IncludeInPath](#IncludeInPath)
    -   [Product](#Product) - Optional - **Type:** boolean  
          **Default:** `true`  
    -   [Environment](#Environment) - Optional - **Type:** boolean  
          **Default:** `false`  
    -   [Solution](#Solution) - Optional - **Type:** boolean  
          **Default:** `false`  
    -   [Segment](#Segment) - Optional - **Type:** boolean  
          **Default:** `true`  
    -   [Tier](#Tier) - Optional - **Type:** boolean  
          **Default:** `false`  
    -   [Component](#Component) - Optional - **Type:** boolean  
          **Default:** `false`  
    -   [Instance](#Instance) - Optional - **Type:** boolean  
          **Default:** `false`  
    -   [Version](#Version) - Optional - **Type:** boolean  
          **Default:** `false`  
    -   [Host](#Host) - Optional - **Type:** boolean  
          **Default:** `false`  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  

* * *

# datapipeline

Managed Data ETL Processing

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"datapipeline" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
			}
		}
	}
}
```

## Attribute Reference

-   [Fragment](#Fragment) _(Container)_ - Optional - **Type:** string  
-   [Permissions](#Permissions)
    -   [Decrypt](#Decrypt) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AsFile](#AsFile) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AppData](#AppData) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AppPublic](#AppPublic) - Optional - **Type:** boolean  
        **Default:** `true`  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  

* * *

# dataset

A data aretefact that is managed in a similar way to a code unit

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"dataset" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
			}
		},
		"Prefix" : "<string>"
	}
}
```

## Attribute Reference

-   [Engine](#Engine) - Required - **Type:** string  
    **Possible Values:** `[s3, rdsSnapshot]`  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
-   [Prefix](#Prefix) - Optional - **Type:** string  

* * *

# ec2

A single virtual machine with no code deployment 

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"ec2" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
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
}
```

## Attribute Reference

-   [FixedIP](#FixedIP) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [DockerHost](#DockerHost) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [Fragment](#Fragment) _(Container)_ - Optional - **Type:** string  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
-   [Ports](#Ports)
    -   [IPAddressGroups](#IPAddressGroups) - Optional - **Type:** array of string  
    -   [LB](#LB)
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [LinkName](#LinkName) - Optional - **Type:** string  
          **Default:** `lb`  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  

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
	"ecs" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
			}
		},
		"AutoScaling" : {
			"WaitForSignal" : true,
			"MinUpdateInstances" : 1,
			"ReplaceCluster" : false,
			"UpdatePauseTime" : "5M",
			"StartupTimeout" : "15M",
			"AlwaysReplaceOnUpdate" : false,
			"ActivityCooldown" : 30
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
}
```

## Attribute Reference

-   [Fragment](#Fragment) _(Container)_ - Optional - **Type:** string  
-   [FixedIP](#FixedIP) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [LogDriver](#LogDriver) - Optional - **Type:** string  
    **Possible Values:** `[awslogs, json-file, fluentd]`  
    **Default:** `awslogs`  
-   [ClusterLogGroup](#ClusterLogGroup) - Optional - **Type:** boolean  
    **Default:** `true`  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
-   [AutoScaling](#AutoScaling)
    -   [WaitForSignal](#WaitForSignal) - Optional - **Type:** boolean  
        **Default:** `true`  
        **Description:** Wait for a cfn-signal before treating the instances as alive  
    -   [MinUpdateInstances](#MinUpdateInstances) - Optional - **Type:** number  
        **Default:** `1`  
        **Description:** The minimum number of instances which must be available during an update  
    -   [ReplaceCluster](#ReplaceCluster) - Optional - **Type:** boolean  
        **Default:** `false`  
        **Description:** When set to true a brand new cluster will be built, if false the instances in the current cluster will be replaced  
    -   [UpdatePauseTime](#UpdatePauseTime) - Optional - **Type:** string  
        **Default:** `5M`  
        **Description:** How long to pause betweeen updates of instances  
    -   [StartupTimeout](#StartupTimeout) - Optional - **Type:** string  
        **Default:** `15M`  
        **Description:** How long to wait for a cfn-signal to be received from a host  
    -   [AlwaysReplaceOnUpdate](#AlwaysReplaceOnUpdate) - Optional - **Type:** boolean  
        **Default:** `false`  
        **Description:** Replace instances on every update action  
    -   [ActivityCooldown](#ActivityCooldown) - Optional - **Type:** number  
        **Default:** `30`  
-   [DockerUsers](#DockerUsers)
    -   [UserName](#UserName) - Optional - **Type:** string  
    -   [UID](#UID) - Required - **Type:** number  

* * *

# service

An orchestrated container with always on scheduling

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"service" : {
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
						"Instance" : "<string>",
						"Version" : "<string>",
						"Role" : "<string>",
						"Direction" : "<string>",
						"Type" : "<string>"
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
}
```

## Attribute Reference

-   [Containers](#Containers)
    -   [Cpu](#Cpu) - Optional - **Type:** number  
    -   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
    -   [LocalLogging](#LocalLogging) - Optional - **Type:** boolean  
        **Default:** `false`  
    -   [LogDriver](#LogDriver) - Optional - **Type:** string  
        **Possible Values:** `[awslogs, json-file, fluentd]`  
        **Default:** `awslogs`  
    -   [ContainerLogGroup](#ContainerLogGroup) - Optional - **Type:** boolean  
        **Default:** `false`  
    -   [RunCapabilities](#RunCapabilities) - Optional - **Type:** array of string  
    -   [Privileged](#Privileged) - Optional - **Type:** boolean  
        **Default:** `false`  
    -   [MaximumMemory](#MaximumMemory) _(MemoryMaximum, MaxMemory)_ - Optional  
        **Types:** number  
        **Description:** Set to 0 to not set a maximum  
    -   [MemoryReservation](#MemoryReservation) _(Memory, ReservedMemory)_ - Required - **Type:** number  
    -   [Ports](#Ports)
    -   [Container](#Container) - Optional  
    -   [DynamicHostPort](#DynamicHostPort) - Optional - **Type:** boolean  
          **Default:** `false`  
    -   [LB](#LB)
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [LinkName](#LinkName) - Optional - **Type:** string  
             **Default:** `lb`  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [IPAddressGroups](#IPAddressGroups) - Optional - **Type:** array of string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [ContainerNetworkLinks](#ContainerNetworkLinks) - Optional - **Type:** array of string  
-   [DesiredCount](#DesiredCount) - Optional - **Type:** number  
    **Default:** `-1`  
-   [UseTaskRole](#UseTaskRole) - Optional - **Type:** boolean  
    **Default:** `true`  
-   [Permissions](#Permissions)
    -   [Decrypt](#Decrypt) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AsFile](#AsFile) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AppData](#AppData) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AppPublic](#AppPublic) - Optional - **Type:** boolean  
        **Default:** `true`  
-   [TaskLogGroup](#TaskLogGroup) - Optional - **Type:** boolean  
    **Default:** `true`  
-   [NetworkMode](#NetworkMode) - Optional - **Type:** string  
    **Possible Values:** `[none, bridge, awsvpc, host]`  
-   [ContainerNetworkLinks](#ContainerNetworkLinks) - Optional - **Type:** boolean  
    **Default:** `false`  

* * *

# task

A container defintion which is invoked on demand

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"task" : {
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
						"Instance" : "<string>",
						"Version" : "<string>",
						"Role" : "<string>",
						"Direction" : "<string>",
						"Type" : "<string>"
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
}
```

## Attribute Reference

-   [Containers](#Containers)
    -   [Cpu](#Cpu) - Optional - **Type:** number  
    -   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
    -   [LocalLogging](#LocalLogging) - Optional - **Type:** boolean  
        **Default:** `false`  
    -   [LogDriver](#LogDriver) - Optional - **Type:** string  
        **Possible Values:** `[awslogs, json-file, fluentd]`  
        **Default:** `awslogs`  
    -   [ContainerLogGroup](#ContainerLogGroup) - Optional - **Type:** boolean  
        **Default:** `false`  
    -   [RunCapabilities](#RunCapabilities) - Optional - **Type:** array of string  
    -   [Privileged](#Privileged) - Optional - **Type:** boolean  
        **Default:** `false`  
    -   [MaximumMemory](#MaximumMemory) _(MemoryMaximum, MaxMemory)_ - Optional  
        **Types:** number  
        **Description:** Set to 0 to not set a maximum  
    -   [MemoryReservation](#MemoryReservation) _(Memory, ReservedMemory)_ - Required - **Type:** number  
    -   [Ports](#Ports)
    -   [Container](#Container) - Optional  
    -   [DynamicHostPort](#DynamicHostPort) - Optional - **Type:** boolean  
          **Default:** `false`  
    -   [LB](#LB)
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [LinkName](#LinkName) - Optional - **Type:** string  
             **Default:** `lb`  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [IPAddressGroups](#IPAddressGroups) - Optional - **Type:** array of string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [ContainerNetworkLinks](#ContainerNetworkLinks) - Optional - **Type:** array of string  
-   [UseTaskRole](#UseTaskRole) - Optional - **Type:** boolean  
    **Default:** `true`  
-   [Permissions](#Permissions)
    -   [Decrypt](#Decrypt) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AsFile](#AsFile) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AppData](#AppData) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AppPublic](#AppPublic) - Optional - **Type:** boolean  
        **Default:** `true`  
-   [TaskLogGroup](#TaskLogGroup) - Optional - **Type:** boolean  
    **Default:** `true`  
-   [FixedName](#FixedName) - Optional - **Type:** boolean  
    **Default:** `false`  

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
	"efs" : {
		"Encrypted" : true,
		"Mounts" : {
			"example" : "< instance of efsMount>"
		}
	}
}
```

## Attribute Reference

-   [Encrypted](#Encrypted) - Optional - **Type:** boolean  
    **Default:** `true`  

* * *

# efsmount

A specific directory on the share for OS mounting

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"efsMount" : {
		"Directory" : "<string>"
	}
}
```

## Attribute Reference

-   [Directory](#Directory) - Required - **Type:** string  

* * *

# es

A managed ElasticSearch instance

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"es" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
			}
		}
	}
}
```

## Attribute Reference

-   [Authentication](#Authentication) - Optional - **Type:** string  
    **Possible Values:** `[IP, SIG4ORIP, SIG4ANDIP]`  
    **Default:** `IP`  
-   [IPAddressGroups](#IPAddressGroups) - Required - **Type:** array of string  
-   [AdvancedOptions](#AdvancedOptions) - Optional - **Type:** array of string  
-   [Version](#Version) - Optional - **Type:** string  
    **Default:** `2.3`  
-   [Encrypted](#Encrypted) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [Snapshot](#Snapshot)
    -   [Hour](#Hour) - Optional - **Type:** string  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  

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
	"lambda" : {
		"Functions" : {
			"example" : "< instance of function>"
		}
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
	"function" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
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
						"Instance" : "<string>",
						"Version" : "<string>",
						"Role" : "<string>",
						"Direction" : "<string>",
						"Type" : "<string>"
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
}
```

## Attribute Reference

-   [Fragment](#Fragment) _(Container)_ - Optional - **Type:** string  
-   [Handler](#Handler) - Required - **Type:** string  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
-   [LogMetrics](#LogMetrics)
    -   [LogFilter](#LogFilter) - Required - **Type:** string  
-   [LogWatchers](#LogWatchers)
    -   [LogFilter](#LogFilter) - Required - **Type:** string  
    -   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
-   [Alerts](#Alerts)
    -   [Description](#Description) - Optional  
    -   [Name](#Name) - Required - **Type:** string  
    -   [Metric](#Metric)
    -   [Name](#Name) - Required - **Type:** string  
    -   [Type](#Type) - Required - **Type:** string  
    -   [Threshold](#Threshold) - Optional - **Type:** number  
        **Default:** `1`  
    -   [Severity](#Severity) - Optional - **Type:** string  
        **Default:** `Info`  
    -   [Namespace](#Namespace) - Optional - **Type:** string  
    -   [Comparison](#Comparison) - Optional - **Type:** string  
        **Default:** `Threshold`  
    -   [Operator](#Operator) - Optional - **Type:** string  
        **Default:** `GreaterThanOrEqualToThreshold`  
    -   [Time](#Time) - Optional - **Type:** number  
        **Default:** `300`  
    -   [Periods](#Periods) - Optional - **Type:** number  
        **Default:** `1`  
    -   [Statistic](#Statistic) - Optional - **Type:** string  
        **Default:** `Sum`  
    -   [ReportOk](#ReportOk) - Optional - **Type:** boolean  
        **Default:** `false`  
    -   [MissingData](#MissingData) - Optional - **Type:** string  
        **Default:** `notBreaching`  
-   [Memory](#Memory) _(MemorySize)_ - Optional - **Type:** number  
    **Default:** `0`  
-   [RunTime](#RunTime) - Required - **Type:** string  
    **Possible Values:** `[nodejs, nodejs4.3, nodejs6.10, nodejs8.10, java8, python2.7, python3.6, dotnetcore1.0, dotnetcore2.0, dotnetcore2.1, nodejs4.3-edge, go1.x]`  
-   [Schedules](#Schedules)
    -   [Expression](#Expression) - Optional - **Type:** string  
        **Default:** `rate(6 minutes)`  
    -   [InputPath](#InputPath) - Optional - **Type:** string  
        **Default:** `/healthcheck`  
    -   [Input](#Input) - Optional - **Type:** object  
-   [Timeout](#Timeout) - Optional - **Type:** number  
    **Default:** `0`  
-   [VPCAccess](#VPCAccess) - Optional - **Type:** boolean  
    **Default:** `true`  
-   [UseSegmentKey](#UseSegmentKey) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [Permissions](#Permissions)
    -   [Decrypt](#Decrypt) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AsFile](#AsFile) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AppData](#AppData) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AppPublic](#AppPublic) - Optional - **Type:** boolean  
        **Default:** `true`  
-   [PredefineLogGroup](#PredefineLogGroup) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [Environment](#Environment)
    -   [AsFile](#AsFile) - Optional - **Type:** boolean  
        **Default:** `false`  
    -   [Json](#Json)
    -   [Escaped](#Escaped) - Optional - **Type:** boolean  
          **Default:** `true`  
    -   [Prefix](#Prefix) - Optional - **Type:** string  
          **Possible Values:** `[json, ]`  
          **Default:** `json`  

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
	"lb" : {
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
}
```

## Attribute Reference

-   [Logs](#Logs) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [Engine](#Engine) - Optional - **Type:** string  
    **Possible Values:** `[application, network, classic]`  
    **Default:** `application`  
-   [Profiles](#Profiles)
    -   [SecurityProfile](#SecurityProfile) - Optional - **Type:** string  
        **Default:** `default`  
-   [IdleTimeout](#IdleTimeout) - Optional - **Type:** number  
    **Default:** `60`  
-   [HealthCheckPort](#HealthCheckPort) - Optional - **Type:** string  

* * *

# lbport

A specifc listener based on the client side network port

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"lbport" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
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
}
```

## Attribute Reference

-   [IPAddressGroups](#IPAddressGroups) - Optional - **Type:** array of string  
-   [Certificate](#Certificate) - Optional - **Type:** object  
-   [HostFilter](#HostFilter) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [Mapping](#Mapping) - Optional - **Type:** string  
-   [Path](#Path) - Optional - **Type:** string  
    **Default:** `default`  
-   [Priority](#Priority) - Optional - **Type:** number  
    **Default:** `100`  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
-   [Authentication](#Authentication)
    -   [SessionCookieName](#SessionCookieName) - Optional - **Type:** string  
        **Default:** `AWSELBAuthSessionCookie`  
    -   [SessionTimeout](#SessionTimeout) - Optional - **Type:** number  
        **Default:** `604800`  
-   [Redirect](#Redirect)
    -   [Protocol](#Protocol) - Optional - **Type:** string  
        **Possible Values:** `[HTTPS, #{protocol}]`  
        **Default:** `HTTPS`  
    -   [Port](#Port) - Optional - **Type:** string  
        **Default:** `443`  
    -   [Host](#Host) - Optional - **Type:** string  
        **Default:** `#{host}`  
    -   [Path](#Path) - Optional - **Type:** string  
        **Default:** `/#{path}`  
    -   [Query](#Query) - Optional - **Type:** string  
        **Default:** `#{query}`  
    -   [Permanent](#Permanent) - Optional - **Type:** boolean  
        **Default:** `true`  
-   [Fixed](#Fixed)
    -   [Message](#Message) - Optional - **Type:** string  
        **Default:** `This application is currently unavailable. Please try again later.`  
    -   [ContentType](#ContentType) - Optional - **Type:** string  
        **Default:** `text/plain`  
    -   [StatusCode](#StatusCode) - Optional - **Type:** string  
        **Default:** `404`  
-   [Forward](#Forward)
    -   [TargetType](#TargetType) - Optional - **Type:** string  
        **Possible Values:** `[instance, ip]`  
        **Default:** `instance`  
    -   [SlowStartTime](#SlowStartTime) - Optional - **Type:** number  
        **Default:** `-1`  
    -   [StickinessTime](#StickinessTime) - Optional - **Type:** number  
        **Default:** `-1`  
    -   [DeregistrationTimeout](#DeregistrationTimeout) - Optional - **Type:** number  
        **Default:** `30`  

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
	"mobilenotifier" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
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
}
```

## Attribute Reference

-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
-   [SuccessSampleRate](#SuccessSampleRate) - Optional - **Type:** string  
    **Default:** `100`  
-   [Credentials](#Credentials)
    -   [EncryptionScheme](#EncryptionScheme) - Optional - **Type:** string  
        **Possible Values:** `[base64]`  
        **Default:** `base64`  

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
	"mobilenotiferplatform" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
			}
		},
		"LogMetrics" : {
			"example" : {
				"LogFilter" : "<string>"
			}
		}
	}
}
```

## Attribute Reference

-   [Engine](#Engine) - Optional - **Type:** string  
-   [SuccessSampleRate](#SuccessSampleRate) - Optional - **Type:** string  
-   [Credentials](#Credentials)
    -   [EncryptionScheme](#EncryptionScheme) - Optional - **Type:** string  
        **Possible Values:** `[base64]`  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
-   [LogMetrics](#LogMetrics)
    -   [LogFilter](#LogFilter) - Required - **Type:** string  

* * *

# rds

A managed SQL database instance

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"rds" : {
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
}
```

## Attribute Reference

-   [Engine](#Engine) - Required  
-   [EngineVersion](#EngineVersion) - Optional - **Type:** string  
-   [Port](#Port) - Optional - **Type:** string  
-   [Encrypted](#Encrypted) - Optional - **Type:** boolean  
    **Default:** `false`  
-   [GenerateCredentials](#GenerateCredentials)
    -   [Enabled](#Enabled) - Optional - **Type:** boolean  
        **Default:** `false`  
    -   [MasterUserName](#MasterUserName) - Optional - **Type:** string  
        **Default:** `root`  
    -   [CharacterLength](#CharacterLength) - Optional - **Type:** number  
        **Default:** `20`  
    -   [EncryptionScheme](#EncryptionScheme) - Optional - **Type:** string  
        **Possible Values:** `[base64]`  
-   [Size](#Size) - Optional - **Type:** number  
    **Default:** `20`  
-   [Backup](#Backup)
    -   [RetentionPeriod](#RetentionPeriod) - Optional - **Type:** number  
        **Default:** `35`  
    -   [SnapshotOnDeploy](#SnapshotOnDeploy) - Optional - **Type:** boolean  
        **Default:** `true`  
-   [AutoMinorVersionUpgrade](#AutoMinorVersionUpgrade) - Optional - **Type:** boolean  
-   [DatabaseName](#DatabaseName) - Optional - **Type:** string  
-   [DBParameters](#DBParameters) - Optional - **Type:** object  

* * *

# s3

HTTP based object storage service

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"s3" : {
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
}
```

## Attribute Reference

-   [Lifecycle](#Lifecycle)
    -   [Expiration](#Expiration) - Optional  
        **Types:** string, number  
        **Description:** Provide either a date or a number of days  
    -   [Offline](#Offline) - Optional  
        **Types:** string, number  
        **Description:** Provide either a date or a number of days  
    -   [Versioning](#Versioning) - Optional - **Type:** boolean  
        **Default:** `false`  
-   [Website](#Website)
    -   [Index](#Index) - Optional - **Type:** string  
        **Default:** `index.html`  
    -   [Error](#Error) - Optional - **Type:** string  
-   [PublicAccess](#PublicAccess)
    -   [Enabled](#Enabled) - Optional - **Type:** boolean  
        **Default:** `false`  
    -   [Permissions](#Permissions) - Optional - **Type:** string  
        **Possible Values:** `[ro, wo, rw]`  
        **Default:** `ro`  
    -   [IPAddressGroups](#IPAddressGroups) - Optional - **Type:** array of string  
        **Default:** `_localnet`  
    -   [Prefix](#Prefix) - Optional - **Type:** string  
-   [Style](#Style) - Optional - **Type:** string  
    **Description:** TODO(mfl): Think this can be removed  
-   [Notifications](#Notifications) - Optional - **Type:** object  
-   [CORSBehaviours](#CORSBehaviours) - Optional - **Type:** array of string  

* * *

# spa

Object stored hosted web application with content distribution management

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"spa" : {
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
}
```

## Attribute Reference

-   [Fragment](#Fragment) _(Container)_ - Optional - **Type:** string  
-   [Links](#Links) - Optional - **Type:** object  
-   [WAF](#WAF)
    -   [IPAddressGroups](#IPAddressGroups) - Required - **Type:** array of string  
    -   [Default](#Default) - Optional - **Type:** string  
        **Possible Values:** `[ALLOW, BLOCK]`  
        **Default:** `BLOCK`  
    -   [RuleDefault](#RuleDefault) - Optional - **Type:** string  
        **Possible Values:** `[ALLOW, BLOCK]`  
        **Default:** `ALLOW`  
-   [CloudFront](#CloudFront)
    -   [AssumeSNI](#AssumeSNI) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [EnableLogging](#EnableLogging) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [CountryGroups](#CountryGroups) - Optional - **Type:** array of string  
    -   [ErrorPage](#ErrorPage) - Optional - **Type:** string  
        **Default:** `/index.html`  
    -   [DeniedPage](#DeniedPage) - Optional - **Type:** string  
    -   [NotFoundPage](#NotFoundPage) - Optional - **Type:** string  
    -   [CachingTTL](#CachingTTL)
    -   [Default](#Default) - Optional - **Type:** number  
          **Default:** `600`  
    -   [Maximum](#Maximum) - Optional - **Type:** number  
          **Default:** `31536000`  
    -   [Minimum](#Minimum) - Optional - **Type:** number  
          **Default:** `0`  
    -   [Compress](#Compress) - Optional - **Type:** boolean  
        **Default:** `true`  
-   [Certificate](#Certificate)
    -   [\*](#*) - Optional  
-   [Profiles](#Profiles)
    -   [SecurityProfile](#SecurityProfile) - Optional - **Type:** string  
        **Default:** `default`  

* * *

# sqs

Managed worker queue engine

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - solution

## Component Format

```json
{
	"sqs" : {
		"DelaySeconds" : "<number>",
		"MaximumMessageSize" : "<number>",
		"MessageRetentionPeriod" : "<number>",
		"ReceiveMessageWaitTimeSeconds" : "<number>",
		"DeadLetterQueue" : {
			"MaxReceives" : 0
		},
		"VisibilityTimeout" : "<number>"
	}
}
```

## Attribute Reference

-   [DelaySeconds](#DelaySeconds) - Optional - **Type:** number  
-   [MaximumMessageSize](#MaximumMessageSize) - Optional - **Type:** number  
-   [MessageRetentionPeriod](#MessageRetentionPeriod) - Optional - **Type:** number  
-   [ReceiveMessageWaitTimeSeconds](#ReceiveMessageWaitTimeSeconds) - Optional - **Type:** number  
-   [DeadLetterQueue](#DeadLetterQueue)
    -   [MaxReceives](#MaxReceives) - Optional - **Type:** number  
        **Default:** `0`  
-   [VisibilityTimeout](#VisibilityTimeout) - Optional - **Type:** number  

* * *

# user

A user with permissions on components deployed in the solution

## Deployment Properties

-   **Available Providers** - aws
-   **Component Level** - application

## Component Format

```json
{
	"user" : {
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
				"Instance" : "<string>",
				"Version" : "<string>",
				"Role" : "<string>",
				"Direction" : "<string>",
				"Type" : "<string>"
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
}
```

## Attribute Reference

-   [Fragment](#Fragment) _(Container)_ - Optional - **Type:** string  
-   [Links](#Links)
    -   [Any](#Any) - Optional - **Type:** string  
    -   [Tenant](#Tenant) - Optional - **Type:** string  
    -   [Product](#Product) - Optional - **Type:** string  
    -   [Environment](#Environment) - Optional - **Type:** string  
    -   [Segment](#Segment) - Optional - **Type:** string  
    -   [Tier](#Tier) - Required - **Type:** string  
    -   [Component](#Component) - Required - **Type:** string  
    -   [Function](#Function) - Optional - **Type:** string  
    -   [Service](#Service) - Optional - **Type:** string  
    -   [Task](#Task) - Optional - **Type:** string  
    -   [PortMapping](#PortMapping) _(Port)_ - Optional - **Type:** string  
    -   [Mount](#Mount) - Optional - **Type:** string  
    -   [Platform](#Platform) - Optional - **Type:** string  
    -   [Instance](#Instance) - Optional - **Type:** string  
    -   [Version](#Version) - Optional - **Type:** string  
    -   [Role](#Role) - Optional - **Type:** string  
    -   [Direction](#Direction) - Optional - **Type:** string  
    -   [Type](#Type) - Optional - **Type:** string  
-   [GenerateCredentials](#GenerateCredentials)
    -   [Formats](#Formats) - Optional - **Type:** array of string  
        **Possible Values:** `[system, console]`  
        **Default:** `system`  
    -   [EncryptionScheme](#EncryptionScheme) - Optional - **Type:** string  
        **Possible Values:** `[base64]`  
    -   [CharacterLength](#CharacterLength) - Optional - **Type:** number  
        **Default:** `20`  
-   [Permissions](#Permissions)
    -   [Decrypt](#Decrypt) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AsFile](#AsFile) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AppData](#AppData) - Optional - **Type:** boolean  
        **Default:** `true`  
    -   [AppPublic](#AppPublic) - Optional - **Type:** boolean  
        **Default:** `true`  

* * *
