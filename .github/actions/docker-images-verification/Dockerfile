# Container image that runs your code
#FROM alpine:3.10
FROM python

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN pip install requests
# Copies your code file from your action repository to the filesystem path `/` of the container

COPY entrypoint.sh /entrypoint.sh


# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
