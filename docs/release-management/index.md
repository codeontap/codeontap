# Release Management

The CodeOnTap release management process provides a controlled approach to managing the life cycle of your code. By integrating code release management into CodeOnTap we can ensure that the infrastructure always as the appropriate code version and that roll backs are simple to manage

CodeOnTap has two release management modes:

- **Continuous Deployment**
    In the majority of your products you will have an environment which always runs the latest version of code which has been committed to your source code repository. This is generally known as an integration environment, and is used to verify from a technical perspective that the code is working as expected. Webhooks on your source control repository notify the automation server that changes have been made to the repository and the automation server then builds and test the code. If this all goes well a deployment to the nominated environment is started.
- **Approval Based Deployment**
    Approval based deployments are used to deploy code to environments where you want to control which code versions are deployed. The approval process is managed using commit hashes/tags on the code repository and a set of jobs on your automation server. The approval based process follows the idea of promoting a code commit from a lower environment to a higher environment and once it has been tested it is accepted into the environment. You define a order of environments and repeat the promotion and acceptance  process until you run out of environments.

With these two release modes you can combine a continuous integration and deployment process while still ensuring that code is verified and managed when being released to production.

The standard release workflow that we recommend is to have continuous deployment to an integration environment and approval based deployment to a preproduction and then through to production.

1. Code updated in repository
2. Code repository notifies automation server through a webhook event
3. Automation server clones the updated repository and runs a build and appropriate testing of the code
4. If the build and testing is successful a deployment job is triggered
5. The automation server deploys the code into the integration environment
6. When the deploy has completed the automation server updates the CMDB with the latest commit reference which was used in the environment
7. The integration environment is checked to make sure it is working as expected
8. On the Automation server a product team member goes to the environment they want to release code into
9. Prepare a release which tells the environment which code commit that will be deployed
10. Deploy the release to the new environment
11. Test the deployment has worked as expected
12. Accept the release which then makes it available to the environment "above it"

This workflow seems long but this covers a full release from code commit through to production release