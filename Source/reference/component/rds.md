---

title: RDS
layout: reference_component
category: reference_component
description: Relational Database Instance
provider: aws
deployment levels: solution
properties:
    -
        name: Engine
        required: true
        default: mysql
        type: string
        source: solution
        value: 
            - mysql
            - postgres
        description: The database engine used to run the instance
        properties:
    -
        name: EngineVersion
        required: true
        default:
        type: string
        source: solution
        value: 
        description: The major version of the database engine 
        properties:
    -
        name: Size
        required: true
        default: 5
        type: int
        source: solution
        value: 
        description: The size ( in Gb ) of the instance
        properties:
    -
        name: Port
        required: true
        default: 20
        type: string
        source: solution
        value: 
        description: The TCP port the RDS instance listens on
        properties:
    -
        name: Encrypted
        required: false
        default: false
        type: boolean
        source: solution
        value:
        description: Encrypt the RDS instance at rest using the segment KMS key
        properties:
    -
        name: Backup
        required: 
        default:
        type: properties
        source: solution
        value:
        description: RDS instance backup configuration
        properties:
            -
                name: RetentionPeriod
                required:
                default: 35
                type: int
                source: solution
                value:
                description: Automated snapshot retention period in days
                properties:
            -
                name: SnapShotOnDeploy
                required: 
                default:
                type: boolean
                source: solution
                value:
                description: Create a manual snapshot whenever the instance is deployed
                properties:
    -
        name: Login
        required: true
        default:
        type: properties
        source: credentials
        value:
        description: The master login credentials for the database
        properties:
            -
                name: Username
                required: yes
                default:
                type: string
                source: credentials
                value:
                description: The master username for the database
                properties:
            -
                name: Password
                required: yes
                default:
                type: string
                source: credentials
                value:
                description: The master password for the database
                properties:
attributes:
    -
        name: FQDN
        description: The fully qualified domain name of the RDS instance
    -
        name: PORT
        description: The TCP port the RDS instance listens on
    -
        name: NAME
        description: The name of the database hosted on the RDS instance
    -
        name: PASSWORD
        description: The master password for the database
    -
        name: USERNAME
        description: The master username for the database
---