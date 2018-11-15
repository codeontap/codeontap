# Creating a Release

1. Determine the version based on our [versioning strategy](./versioning.md)
2. Generate [reference documentation](./creating-references.md)
3. Tag Gen3 repositories with release tag and push to Github. Annotated tags must be used :-

    ```bash
    git tag -a v<Version> -m "Q? 20?? Train|Tram Release"
    git push --tags
    ```

    [Repositories](./index.md) to be tagged are 

    1. Gen3 Generation
    2. Gen3 Automation
    3. Gen3 Startup

    Next edit the [train config file](https://github.com/codeontap/docker-gen3/blob/train/base/config.json), update the version references to the desired train release tag, and push to Github.

4. Confirm that the DockerHub Images have built. Tagging the repositories should trigger DockerHub builds for each of the Images which are listed as Docker Images
5. Activate the Read The Docs Version . Head to the CodeOnTap Docs Admin site and under versions there should be an entry for your version listed in the Inactive Versions list. Click edit on the Version and then tick Active to publish the new version
) and update the version references to the train release tag, and push to Github.
