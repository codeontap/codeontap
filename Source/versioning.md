---
layout: page
title: Versioning
category: home
---
CodeOnTap releases follow the release train concept where releases are made at schedudled intervals. Two train releases are currently used, the tram and the train.

# Releases

### Tram Releases

The Tram release is the collection of all changes performed during the schedule time frame. CodeOnTap tram schedules are currently performed weekly.

### Train Releases

The train release is the latest stable release of CodeOnTap. Scheuled for every 3 months

### Patch Releases

Bug fix releases for train releases. Will be released as required.

# Feature Tags

Since releases are schedule based, a feature or change to CodeOnTap might not always be ready to go. To work within this process changes should be submitted with the ability to toggle the new change on or off, off by default. This toggle is called a Feature Tag. Feature tags are named based on the feature that is being added and feature tags are enabled in CodeOnTap via an environment variable FEATURE_TAG for bash scripts and featureTag in freemarker templates.

When a change is ready to go the feature tag logic and the legacy code are removed as part of the next scheduled train release. Until the change is ready, the change can only be enabled with the use of feature tags.

# Versioning

CodeOnTap follows semver 2.0.0 (https://semver.org/spec/v2.0.0.html) with alignment to our release schedules

- **Major - 1.x.x** When the CodeOnTap team determine that a significant or breaking change is being introduced
- **Minor - x.1.x** Each train release increments the minor version number
- **Patch - x.x.1** Urgent fixes for the most recent train release
- **Release Candidate - x.x.x-rc1** Each tram release is treated as a release candidate

With this format the release candidate and minor versions will increment on a regular basis and the major and path releases are managed by the CodeOnTap team
