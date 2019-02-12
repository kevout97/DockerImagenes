FROM centos:latest
MAINTAINER Kev Gomez
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
WORKDIR /opt/crud-certificates
COPY crud-certificates /opt/crud-certificates
RUN yum update -y && yum upgrade -y && \
    yum install epel-release -y && \
    yum install gcc -y && \
    yum install python-devel -y && \
    yum install python -y && \
    yum install python-pip -y && \
    yum install mariadb-devel -y && \
    pip install --upgrade pip && \
    pip install flask && \
    pip install flask-mysqldb
ENTRYPOINT [ "/entrypoint.sh" ]
EXPOSE 3000, 3306