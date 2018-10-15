# Accessing Jenkins

Now that we have deployed all of the components lets, start using them.

## DNS Registration

!!! info
    Codeontap currently doesn't support automated DNS registration. This needs to be done manually

Log into the AWS Console and switch role ( if required ) into your automation server account

Head to `EC2 -> Load Balancers` in the console.

In the list of load balancers there should be a classic load balancer deployed, under the properties of this load balancer not the DNS name property

Head to `Route53 -> Hosted Zones -> <Your Tenant DNS domain name from [CMDB Setup](./cmdb-setup)`

Add the following record for you automation server

- Name: automation
- Alias: Yes
- Value: the DNS Name noted earlier

## Log into Jenkins

Once the DNS record is in place we should be able to log into Jenkins

From your browser head to `https://automation.<your tenant dns domain>`

You should be prompted for your github credentials and after supplying them get the Jenkins Home page

## You Made It

Using codeontap you have now configured and built a scalable, highly available CICD pipeline service which can be used to deploy your own products. The next step is to setup the Jenkins jobs which will build, test, and deploy your products, we will cover this off as a new guide.
