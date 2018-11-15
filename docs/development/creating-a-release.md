# Creating a Release

1. Determine the version based on our [versioning strategy](./versioning.md)
2. Generate [reference documentation](./creating-references.md)
3. Tag github repositories with release tag. For the following repositories add an annotated tag to the repo and push to GitHub

```bash
git tag -a v<Version>
git push --tags
```

4. Confirm that the DockerHub Images have built. Tagging the repositories should trigger DockerHub builds for each of the Images which are listed as Docker Images
5. Activate the Read The Docs Version . Head to the CodeOnTap Docs Admin site and under versions there should be an entry for your version listed in the Inactive Versions list. Click edit on the Version and then tick Active to publish the new version
