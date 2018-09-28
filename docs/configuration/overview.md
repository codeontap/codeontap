# Code On Tap Configuration Files

## Configuration Files

### domains.json

* Repository - AccountCMDB
* Scope - Tenant
* Type - Config
* Example:
    ````JSON
    {
        "Domains" : {
            "Validation" : "codeontap.io",
            "cot" : {
                "Stem": "codeontap.io"
            },
            "syd1" : {
                "Stem": "syd1.codeontap.io"
                }
            }
    }
    ````

### tenant.json

* Repository - AccountCMDB
* Scope - Tenant
* Type - Config
* Example:
    ````JSON
    {
        "Tenant" : {
            "Title" : "Code on Tap",
            "Id" : "cot",
            "Domain" : "cot"
        },
        "Account" : {
            "Region" : "ap-southeast-2",
            "Domain" : "syd1"
        },
        "Product" : {
            "Region" : "ap-southeast-2",
            "SES" : {
                "Region" : "us-west-2"
            }
        },
        "Segment" : {
            "SSH" : {
                "IPAddressGroups" : ["cbroffice"]
            }
        }
    }
    ````

### ipaddressgroups.json

* Repository - AccountCMDB
* Scope - Tenant
* Type - Config
* Example:
    ````JSON
    {
        "IPAddressGroups" : {
            "cbroffice" : {
                "access" : {
                    "Description" : "Canberra Office",
                    "CIDR" : [
                        "123.123.123.123/32"
                    ]
                }
            }
        }
    }
    ````

### countrygroups.json

* Repository - AccountCMDB
* Scope - Tenant
* Type - Config
* Example:
    ````JSON
    {
        "CountryGroups" : {
            "Australia" : {
                "Locations" : "AU"
            }
        }
    }
    ````

### account.json

* Repository - AccountCMDB
* Scope - Account
* Type - Config
* Example:
    ````JSON
    {
        "Account" : {
            "Title" : "Development Account",
            "Id" : "cotdev01",
            "AWSId" : "1234567890",
            "Seed" : "ab2401"
        }
    }
    ````

### appsettings.json

* Repository - AccountCMDB, ProductCMDB
* Scope - product, segment, app
* Type - Config
* Example:
    ````JSON
    {
        "ChatBot" : {
            "Rest" : {
                "Url" : "https://bot.skynet.com/dev/api"
            }
        },
        "MAINTENANCE_START" : "2017-11-16T21:00:00+11:00",
        "MAINTENANCE_END" : "2017-11-18T09:00:00+11:00"
    }
    ````

### build.json

* Repository - ProductCMDB
* Scope - app
* Type - Config
* Example:
    ````JSON
    {
        "Commit": "1730ad1e0dc0cb84a066f43836c45409212394a6a",
        "Formats": ["docker" ]
    }
    ````

### segment.json

* Repository - ProductCMDB
* Scope - segment
* Type - Config
* Example:
    ````JSON
    {
        "Segment" : {
            "Title" : "Development",
            "Environment" : "dev",
            "Id" : "dev",
            "Name" : "dev"
        }
    }
    ````

### solution.json

* Repository - ProductCMDB
* Scope - product, segment, app
* Type - Config
* Example:
    ````JSON
    {
        "Solution" : {
            "Id" : "bdd"
        },
        "Tiers": {
            "web" : {
                "Components" : {
                    "bdd" : {
                        "Title" : "BDD Server",
                        "Role" : "ALM",
                        "DeploymentUnits" : ["bdd"],
                        "EC2" : {
                            "Ports" : [
                                {
                                    "Port" : "3000"
                                }
                            ],
                            "LoadBalanced": true
                        },
                        "MultiAZ" : false
                    }
                }
            }
        },
        "Segment": {
            "SSH": {
                "Active": true
            }
        },
        "Processors": {
            "default": {
                "EC2": {
                    "Processor": "t2.medium"
                }
            }
        },
        "Storage" : {
            "default" : {
                "EC2" : {
                    "Volumes" : {
                        "codeontap": {
                            "Device" : "/dev/sdp",
                            "Size" : "100"
                        }
                    }
                }
            }
        }
    }
    ````

### deployment_unit.json

* Repository - AppCode
* Scope - product, implementation
* Type - Config
* Example:
    ````JSON
    {
        "Units" : ["cotapp-v1"],
        "Formats" : ["spa"]
    }
    ````

### \<resource\>.json

* Repository - AppCode
* Scope - implementation
* Type - Config
* Example - apigw.json
    ````JSON
    {
        "Accounts" : ["1234567890"],
        "Regions" : ["ap-southeast-2"],
        "ApiKey" : true,
        "Type" : "lambda",
        "Variable" : "COTAPP_COTAPI_LAMBDA"
    }
    ````

## Artefacts

### credentials.json

* Repository - AccountCMDB
* Scope - Account, segment, app
* Type - Artefact
* Example:
    ````JSON
    {
        "Credentials": {
            "ChatBot": {
                "RESTAPI": {
                    "Username": "User01",
                    "Password": ""
                }
            }
        }
    }
    ````

### template.json

* Repository - ProductCMDB
* Scope - provider templates
* Type - Artefact

### stack.json

* Repository - ProductCMDB
* Scope - provider templates
* Type - Artefact

### epilogue.sh

* Repository - ProductCMDB
* Scope - provider templates
* Type - Artefact

### prologue.sh

* Repository - ProductCMDB
* Scope - provider templates
* Type - Artefact