# Generating Documentation References

Since CodeOnTap is primarily a templating engine we can use it to generate documentation using the CodeOnTap code.
We use this process to generate reference templates in markdown that are then published to our documentation site.

## Reference Types

The following reference types are available

- **component** - Generates a reference document outlining the components available in codeontap and their configuration options

## Generating a Reference

!!! note "Pre-requisites"
    To generate the reference you will need to be setup to run CodeOnTap

    - A clone of the [generation repo](https://github.com/codeontap/gen3)  
    - A clone of the [documentation repo](https://github.com/codeontap/codeontap)  
    - `GENERATION_DIR` environment variable configured to the clone location  
    - Access to docker for the markdown clean-up process  
    - This process does not require a cmdb or `ACCOUNT` configured

1. cd into the `GENERATION_DIR`
2. Run the template generation process `${GENERATION_DIR}/createReference.sh -t <reference type>`
3. The generation process will run and the file will be available in `${GENERATION_DIR}\dist\reference\<reference type>-reference.md`
4. Confirm that it is ok and then replace the existing reference document in the documenation repo under `docs/reference`
5. Commit the docs repo changes and the reference will be published
