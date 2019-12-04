# CMDB Creation

Now we need to create our CMDB, we will use [cookie cutter](https://github.com/audreyr/cookiecutter) to bootstrap this process.

We will be creating two CMDBs, during a deployment these CMDBs are combined to build the information required to deploy the product

## Accounts

This contains the enterprise level information, Cloud Provider Accounts, DNS Domains, Environments etc.

## ALM Product

This contains the configuration for the ALM product itself.

## Create your Accounts CMDB and set up your tenant

```bash
cookiecutter /opt/codeontap/patterns/cmdb/tenant
```

Follow the prompts to create your Accounts CMDB and the tenant

- **tenant_id** - This is a short ID of your overall enterprise
- **tenant_name** - This is a longer name of your enterprise
- **domain_stem** - The base level DNS domain name that you would use for products that you deploy
- **default_region** - The default AWS region that you would like to deploy services to

cd into the new accounts directory

```bash
cd accounts
```

## Create your first Account

Once you have an accounts CMDB it needs an account. If you haven't already you will need to setup an AWS Account that will be used host our product.

!!! info
  Once you have an account note the Account ID as we will need that in this step

```bash
cookiecutter /opt/codeontap/patterns/cmdb/account
```

Follow the prompts to create your new account

- **account_id** - A short Id of the account in the CMDB. This must be unique in your CMDB
- **account_name** - The name can be a longer, more descriptive name of the account compared to your Id
- **account_seed** - This is a random seed string we use to ensure that global AWS components are unique. You should not need to change this
- **aws_account_id** - The AWS Account Id that you noted earlier

## Create your first Product

Now that you have a tenant and an account we need to create a product that will be deployed into the account. In this case we will be using a template to deploy our recommended application lifecycle management deployment

Head back to the root of your CMDB

```bash
cd /var/opt/codeontap
```

Run the ALM cookie cutter template

```bash
cookiecutter /opt/codeontap/patterns/products/app-lifecylce-mgmt
```

Follow through the prompts to generate the CMDB. Leave any predefined values as they are for now

- **domain_id** - Your tenant Id. This is the name of the DNS domain that you would like to use. The tenant creation sets a default domain to the same as the tenant so we can use that for now
- **product_id/name** - The short Id of your product and a more descriptive name
- **solution_id/name** - The short Id of the solution for the product and a more descriptive name
- **environment_id/name** - The short Id of the initial environment for this product and a more descriptive name
- **segment_id/name** - The short Id of the initial environment segment and a more descriptive name
- **multi_az** - Enable HA deployments across multiple AWS Availability Zones (Az)
- **source_ip_network** - IP Address Filtering for access to the jenkins server
- **certificate_arn** - The ARN of the AWS ACM Certificate you created earlier
- **certificate_cn** - The CN of the ACM Certificate you created `*.<domainname>`
- **certificate_region** - The region the ACM Certificate was created in
- **slave_provider** - The container service that will be used to build Jenkins Agents
- **ecs_instance_type** - If you are using ECS what instance type would you like to use
- **security_realm** - The authentication provider that users will use to log into Jenkins - Select local for now
- **auth_local_user** - An initial admin user id
- **auth_local_pass** - An initial admin user password
- **auth_github_client_id** - A Github oAuth clientId
- **auth_github_client_secret** - A Github oAuth Secret
- **auth_github_admin_role** - A Github Org Team that will be given initial admin access format `<org id >#<team id>`
- **github_repo_user** - A userid that jenkins will use to pull github repos ( if you have one use your Id)
- **github_repo_pass** - The password for the github user. You can also use personal access tokens if you have MFA enabled

After running this template you will have a new folder in the CMDB called automation. Have a look around through this directory to see what has been created

Key files are:

- `/var/opt/codeontap/automation/config/solutionsv2/shared/default/solution.json` - The solution shows you the infrastructure components that will be deployed to create your product
- `/var/opt/codeontap/automation/config/solutionsv2/alm/default/jenkins/settings.json` - Contains the environment specific settings for your Jenkins deployment

## Add a certificate mapping for the product

Now that we have a product we need to configure its domain name in the enterprise domain register

Edit the domains.json file `/var/opt/codeontap/accounts/<tenantname>/domains.json`

```diff
{
    "Domains" : {
        "Validation" : "<root DNS domain>,
        "<tenant id>" : {
            "Stem": "<root DNS domain>"
        }
    },
    "Certificates" : {
++        "automation" : {
++            "Domain" : "<tenant id>"
++        }
    }
}
```

## Next Step: [Deploy Basic Components](./deploy-basic-components.md)
