# Environment Variables

Environment variables are used for a number of functions within codeontap. This allows them to be easily defined across multiple environments and easily shared between different components in the generation, automation and build process.

## Generation Variables

* **GENERATION_DIR** - The local copy of the generation framework repository
* **ACCOUNT** - The name of the cloud provider account that the segment will be deployed to
* **GENERATION_DEBUG** - Enable debug level output from all scripts running for generation
        * **-x** - base level debug - all outputs printed
        * **+x** - same as -x but all temp files retained

## Automation Variables

* **AUTOMATION_DEBUG** - Enable debug level output from all scripts running for automation
