# codeontap
top level summary of how to use the codeontap framework.

See https://github.com/codeontap/codeontap/wiki for documentation

## Promoting changes to component 'visualiser' (aka data-browser) from environment 'sandpit' to environment 'discovery'

Obviously, this process would be analogous for different components and/or environments.

### Pre-requisites
#### AWS Workspaces client
#### Changes already present in environment 'sandpit'
#### GoSource GitHub credentials

### Procedure

#### Start AWS Workspaces client and log in to workspace.
#### In AWS Workspace, start web browser by clicking the Mozilla Firefox icon at bottom. Firefox window will appear.
#### In Firefox, go to the automation page, at: https://automation.cp1.border.gov.au/job/cotw-trade/job/cotp-blockchain/
#### At time of writing, a warning about invalid HTTPS certificates appeared. Dismiss this warning by doing:
##### Click 'Add exception...'. A dialog will appear.
##### Deselect the checkbox labeled 'Permanently store this exception'.
##### Click the button labeled 'Confirm Security Exception'.
#### A page reading in part 'Sign in to GitHub to continue to DIBP Automation' will appear.
#### Log in with your GoSource GitHub credentials
#### If a page entitled 'Authorize DIBP Automation' appears, click the green button labeled 'Authorize gs-immi' at bottom of page.
#### Click on component 'Discovery - Data Evaluation', then 'Consumer Segment', then '1-Prepare Release'. A page entitled 'Project 1-Prepare-Release' will appear.
#### In the menu at left of page, click on 'Build with Parameters'. A list of deployable components will appear.
#### In the textfield labeled 'DEPLOYMENT_UNITS', locate the line reading 'visualiser-v1-web!. Immediately after the '!' at the end of this line, paste the git commit hash of the code version you wish to deploy.
#### In the textfield labeled 'RELEASE_IDENTIFIER', enter the text 'r24-cnsmr'.
#### Click the grey-blue button labelled 'Build' below the textfield. You will be returned to the 'Project 1-Prepare-Release' page.
#### At left, there is a box labeled 'Build History'. At top of this box is the most recent build which you just began. Click the hyperlinked integer preceded by a '#' character to the left of this most recent, topmost build. A 'Build #123' page will appear.
#### At left of this page, there is a hyperlink 'Console Output'. Click this. A 'Console Output' page will appear.
#### Scroll to the bottom of the page. When the build has finished, you will either see a line including the text 'Finished: SUCCESS', or a failure which you must fix, and which invalidates the remainder of this procedure.
#### At top of page, click 'Consumer Segment'. You will be returned to the 'Consumer Segment' page.
#### Click on the job '2-Deploy-Release'. A job details page will appear.
#### At left, click 'Build with Parameters'. A page entitled 'Project 2-Deploy-Release' will appear.
#### In the textfield labeled 'RELEASE_IDENTIFIER', enter the text 'r24-cnsmr'.
#### Ensure all checkboxes are checked, then click the grey-blue 'Build' button at bottom of page. A page entitled 'Project 2-Deploy-Release' will appear.
#### At left, in the box labeled 'Build History', click the hyperlinked, topmost, most recent build ID. A page entitled 'Build #123' (or similar) will appear.
#### At left, click 'Console Output'. A page entitled 'Console Output' will appear.
#### Scroll to bottom of the page and review the output. You should eventually see either 'Finished: SUCCESS', or a failure, which (again) you must fix and which invalidates the remainder of this process.
