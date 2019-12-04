# Deploy Basic Components

Now that we have the CMDBs in place we should be ready to start deploying our components

## Account Level Components

Deploy the account level components. These components provide shared services that can be used for any product that is deployed into the account, they include auditing and management services.

Hop into the Account context

```bash
cd /var/opt/codeontap/accounts/<Account Name>
```

Repeat the following steps for the following deployment units

- **audit** - deploys an S3 bucket which will store the access log entries of any S3 bucket deployed into this account
- **s3** - deploys a set of S3 buckets that are used during the deployment process. The main bucket is the registry which stores code artefacts when they have been built

Generate the templates used to deploy the services

```bash
${GENERATION_DIR}/createTemplate.sh -l account -u <deployment unit>
```

This should go through a few steps where we generate the cloudformation templates and scripts required to deploy the components

Deploy the unit

```bash
${GENERATION_DIR}/manageStack.sh -l account -u <deployment unit>
```

This should now start to deploy the components into the AWS account that you defined at the start

Repeat these steps for each deployment unit listed above

## Segment Baseline

Now that the account level components are deployed, we now need to deploy the shared components used for a specific deployment of a product's segment. The first deployment is the baseline component. We need this to be deployed before we can continue with the rest of the components

Hop into the segment context

```bash
cd /var/opt/codeontap/automation/config/solutionsv2/shared/default/

export ACCOUNT=<account id>
```

Repeat the following steps for the following deployment units

- **baseline** - Deploys a set of standard services required for any deployment. This includes encryption keys for secret storage, logging buckets etc.

Generate the templates used to deploy the services

```bash
${GENERATION_DIR}/createTemplate.sh -l segment -u <deployment unit>
```

This should go through a few steps where we generate the cloudformation templates and scripts required to deploy the components

Deploy the unit

```bash
${GENERATION_DIR}/manageStack.sh -l segment -u <deployment unit>
```

This should now start to deploy the components into the AWS account that you defined at the start

Repeat these steps for each deployment unit listed above

## Next Step: [Encrypt Secrets](./encrypt-secrets.md)
