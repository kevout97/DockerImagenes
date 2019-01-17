FROM centos:7
MAINTAINER kevin-gomez <kev.gomez97@hotmail.com>
RUN yum update -y && yum upgrade -y && yum install bind which vim -y
EXPOSE 53
COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
ENTRYPOINT /entrypoint.sh