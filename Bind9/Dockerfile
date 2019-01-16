FROM centos:7
MAINTAINER kevin-gomez <kev.gomez97@hotmail.com>
RUN yum update -y && yum upgrade -y && yum install bind -y
EXPOSE 53
ENTRYPOINT entrypoint.sh