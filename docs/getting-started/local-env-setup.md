# Local Environment Setup

The first thing we need to is create a CMDB, the CMDB is the core of CodeOnTap and is used to define your product and how it is deployed. We have a set of templates available to get you started.

Create a directory that will be used to store the CMDB and change into it

```bash
mkdir ~/msw
cd ~/msw
```

Pull down the [CodeOnTap docker image](https://hub.docker.com/r/codeontap/gen3/)

```bash
  docker image pull codeontap/gen3
```

Run the codeontap container as an interactive session. This will provide you with a terminal session with all dependencies installed and ready to go

!!! info
  Your AWS profile might be in a different location

```bash
  docker run -it --rm --volume $(pwd):/var/opt/codeontap --volume ~/.aws:/root/.aws codeontap/gen3
```

Change into the CMDB directory and create the root marker file ( this file is used to define where the CMDB starts)

```bash
cd /var/opt/codeontap
touch ./root.json
```

## Next Step: [Create the CMDB](./cmdb-setup.md)