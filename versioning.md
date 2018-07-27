---
layout: page
title: Release Models
category: home
---
CodeOnTap releases follow the release train model [Spotify Example](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/) [Agile Description](https://www.scaledagileframework.com/agile-release-train/) where releases are made at scheduled intervals. With this model all commits to the master branch should be considered release candidates.

# Releases

Our release cycle is structured into three stages. The releases are structured this way to ensure that there is a stable deployment model in place for infrastructure deployments.

## Train

The train release is the stable product release which is the recommended release of CodeOnTap. The train is scheduled quarterly and the timetable is available here: https://github.com/codeontap/codeontap/milestones

## Tram

The tram release is a rollup of the work completed between train releases. The tram release is intended for the testing of new features which are intended for the next tram but with less risk of running into issues with actively developed work. The trams are scheduled to run every two weeks and will be treated as release candidates for the next train release.

## Unicycle

The unicylce release is our latest development code and is generally the master branch of code in the CodeOnTap code repositories. Builds of the unicylce release are triggered on each commit to the code repositories.

## Patch Releases

Patch releases releases are bugfix releases for a train release. They are not scheduled and will be released when possible.

# Feature Tags

Since releases are schedule based, a feature or change to CodeOnTap might not always be ready to go. To work within this process changes should be submitted with the ability to toggle the new change on or off, off by default. This toggle is called a Feature Tag. Feature tags are named based on the feature that is being added and feature tags are enabled in CodeOnTap via an environment variable FEATURE_TAG for bash scripts and featureTag in freemarker templates.

When a change is ready to go the feature tag logic and the legacy code are removed as part of the next scheduled train release. Until the change is ready, the change can only be enabled with the use of feature tags.

# Versioning

CodeOnTap follows semver 2.0.0 (https://semver.org/spec/v2.0.0.html) with alignment to our release schedules

- **Major - v1.x.x** When the CodeOnTap team determine that a significant or breaking change is being introduced
- **Minor - vx.1.x** Each train release increments the minor version number
- **Patch - vx.x.1** Urgent fixes for the most recent train release
- **Release Candidate - vx.2.x-rc1** Each tram release is treated as a release candidate for the next train release

With this format the release candidate and minor versions will increment on a regular basis and the major and patch releases are managed by the CodeOnTap team
