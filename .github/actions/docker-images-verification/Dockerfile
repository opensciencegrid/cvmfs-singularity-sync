# Container image that runs your code
#FROM alpine:3.10
FROM python

# Copies your code file from your action repository to the filesystem path `/` of the container
# COPY entrypoint.sh /entrypoint.sh
COPY docker-images-verify /docker-images-verify
COPY dockerhub.py /dockerhub.py
COPY entrypoint.sh /entrypoint.sh
COPY ../../../docker_images.txt /docker_images.txt

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
