# Encrypt Secrets

Next up we need to encrypt the secret data (passwords, keys, certificates etc. ), that we need to deploy with the application. This allows us to store the secrets in the CMDB so that they can be easily accessed during a deployment.

## Identify Secrets to Encrypt

Our ALM service has a number of secrets that we have picked up a long the way that need to be encrypted

- Github oAuth App Secret
- Jenkins local admin password
- Github repository access account password

Each of these will need to be encrypted before we can store them in the CMDB. You should hopefully have them noted somewhere from our last steps

## Encrypting the Secrets

Hop into the segment context

```bash
cd /var/opt/codeontap/automation/config/solutionsv2/shared/default/

export ACCOUNT=<account id>
```

Repeat the following command for each of the secrets

```bash
${GENERATION_DIR}/manageCrypto.sh -e -t '<secret>'
```

When the script has completed you should receive a base64 encoded string that begins with AQ. Note this string down and we will update the CMDB with the encrypted values

## Update the CMDB

Now that we have encrypted values we need to update the CMDB to secure the secrets. Secrets are stored as special set of settings in a dedicated settings file, the credentials file.

Open the credentials file  `/var/opt/codeontap/automation/infrastructure/operations/alm/default/jenkins/credentials.json`

Update the following values with the base64 sting

- `JenkinsEnv -> Credentials -> github ->  Password` = GitHub repository access account password
- `JenkinsEnv -> Pass` = Jenkins local administrator password
- `GitHubAuth -> Secret` = GitHub oAuth App Secret

With this complete we can safely commit this repository to a centralised git repository

## Next Step: [Deploy Product Components](./deploy-product-components.md)
