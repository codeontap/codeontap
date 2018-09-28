# Deploy Components

Now that we have the CMDBs in place we should be ready to start deploying our components

## Account Level Components

Deploy the account level components. Account level components are services which are generic services which can be used by any service deployed into an account. 

Hop into the Account context

```bash
cd /var/opt/codeontap/accounts/<Account Name>
```

Repeat the following steps for the following deployment units

- **audit** - deploys an S3 bucket which will store the access log entries of any S3 bucket deployed into this account
- **s3** - deploys a set of S3 buckets that are used during the deployment process. The main bucket is the registry which stores code artefacts when they have been built

Generate the templates used to deploy the services

```bash
${GENERATION_DIR}/createAccountTemplate.sh -u <deployment unit>
```

This should go through a few steps where we generate the cloudformation templates and scripts required to deploy the components

Deploy the unit

```bash
${GENERATION_DIR}/manageStack.sh -l account -u <deployment unit>
```

This should now start to deploy the components into the AWS account that you defined at the start

Repeat these steps for each deployment unit listed above

## Deploy Product Components

3. Create and deploy segment level components
   1. cmk
   2. vpc
   3. s3
   4. eip
   5. nat
   6. ssh
4. Encrypt Credentials
   - Github Client Secret
   - Github Credentials
5. Create and deploy solution level components
   1. iam
   2. lg
   3. alm-lb
   4. alm-efs
   5. alm-ecs
6. Deploy docker images to AWS ECR instance
   1. codeontap/jenkins-master
   2. codeontap/gen3-jenkins-slave
   3. codeontap/redirector
7. Deploy application level components
   1. codeontap
   2. jenkins