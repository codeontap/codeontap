# Creating a Release

1. Determine the version based on our [versioning strategy](./versioning.md)
2. Generate [reference documentation](./creating-references.md)
3. Edit the [train config file](https://github.com/codeontap/docker-gen3/blob/train/base/config.json) and update the version references to the desired train release tag.
4. Tag Gen3 repositories with release tag and push to Github. Annotated tags must be used :-

    ```
    git tag -a v<Version> -m "Q? 20?? Train|Tram Release"
    git push --tags
    ```

    NOTE: Readthedocs expects tags to comply with [PEP 440](https://www.python.org/dev/peps/pep-0440/#version-scheme). Thus the tag used for the CodeOnTap repo MUST omit the "v" prefix.

    [Repositories](./index.md) to be tagged and pushed (in the order shown) are

    1. Gen3 Generation
    2. Gen3 Automation
    3. Gen3 Startup
    4. Gen3
    5. CodeOnTap

6. Confirm that the DockerHub Images have built. Tagging the repositories should trigger DockerHub builds for each of the Images which are listed as Docker Images
7. Activate the Read The Docs Version. Head to the CodeOnTap Docs Admin site and under Versions there should be an entry for your version listed in the Inactive Versions list. Click edit on the Version and then tick Active to publish the new version.

