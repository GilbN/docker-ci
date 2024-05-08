<!-- DO NOT EDIT THIS FILE MANUALLY -->
<!-- Please read https://github.com/linuxserver/docker-ci/blob/master/.github/CONTRIBUTING.md -->
[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[huburl]: https://hub.docker.com/r/linuxserver/ci/
[pipelineurl]: https://github.com/linuxserver/pipeline-triggers

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png?v=4&s=4000)][linuxserverurl]


## Contact information:-

| Type | Address/Details |
| :---: | --- |
| Discord | [Discord](https://discord.gg/YWrKVTn) |
| Forum | [Linuserver.io forum][forumurl] |
| IRC | freenode at `#linuxserver.io` more information at:- [IRC][ircurl]
| Podcast | Covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation! [Linuxserver.io Podcast][podcasturl] |

# [linuxserver/ci][huburl]

**This container is not meant for public consumption as it is hard coded to LinuxServer endpoints for storage of resulting reports**

The purpose of this container is to accept environment variables from our build system [linuxserver/pipeline-triggers][pipelineurl] to perform basic continuous integration on the software being built.

## Usage

The container can be run locally, but it is meant to be integrated into the LinuxServer build process:

```
sudo docker run --rm -i \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /host/path:/ci/output:rw `#Optional, will contain all the files the container creates.` \
-e IMAGE="linuxserver/<dockerimage>" \
-e TAGS="<single tag or array separated by |>" \
-e META_TAG=<manifest main dockerhub tag> \
-e BASE=<alpine or debian based distro> \
-e SECRET_KEY=<S3 secret> \
-e ACCESS_KEY=<S3 key> \
-e DOCKER_ENV="<optional, Array of env vars separated by | IE test=test|test2=test2 or single var. Defaults to ''>" \
-e WEB_AUTH="<optional, format user:passord. Defaults to 'user:password'>" \
-e WEB_PATH="<optional, format /yourpath>. Defaults to ''." \
-e S3_REGION=<optional, custom S3 Region. Defaults to 'us-east-1'> \
-e S3_BUCKET=<optional, custom S3 Bucket. Defaults to 'ci-tests.linuxserver.io'> \
-e WEB_SCREENSHOT_TIMEOUT=<optional, time in seconds before timing out trying to take a screenshot. Defaults to '120'>
-e WEB_SCREENSHOT_DELAY=<optional, time in seconds to delay before taking a screenshot after loading the web page. Defaults to '10'> \
-e SBOM_TIMEOUT=<optional, time in seconds before timing out trying to generate a SBOM. Defaults to '900'>
-e WEB_SCREENSHOT=<optional, set to false if not a web app. Defaults to 'false'> \
-e PORT=<optional, port web application listens on internal docker port. Defaults to '80'> \
-e SSL=<optional , use ssl for the screenshot true/false. Defaults to 'false'> \
-e CI_S6_VERBOSITY=<optional, Updates the S6_VERBOSITY env. Defaults to '2'> \
-e CI_LOG_LEVEL=<optional, Sets the ci logging level. Defaults to 'INFO'> \
-e DOCKER_LOGS_TIMEOUT=<optional, How long to wait in seconds while tailing the container logs before timing out. Defaults to '120'> \
-e DRY_RUN=<optional, Set to 'true' when you don't want to upload files to S3 when testing>
-t lsiodev/ci:latest \
python3 test_build.py
```

The following line is only in this repo for loop testing:

- { date: "01.01.50:", desc: "I am the release message for this internal repo." }
