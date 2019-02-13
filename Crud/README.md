# Crud Certificates
## Prerequisitos
Primero necesitamos tener un contenedor de mysql con la base de datos a la cual se conectara el CRUD, para ello generamos un ejecutable con el siguiente contenido:

```bash
#!/bin/bash
MYSQL_INSTANCE_NAME=mysql57

mkdir /var/containers/${MYSQL_INSTANCE_NAME}/{var/log/mysql,var/lib/mysql,var/backups/ejecucionesscript,etc/mysql,tmp} -p
chmod 777 -R /var/containers/${MYSQL_INSTANCE_NAME}/tmp
docker run -td  -v /var/containers/${MYSQL_INSTANCE_NAME}/var/log/mysql/:/var/log/mysql/:z \
                -v /var/containers/${MYSQL_INSTANCE_NAME}/var/lib/mysql/:/var/lib/mysql/:z \
                -v /var/containers/${MYSQL_INSTANCE_NAME}/etc/mysql/:/etc/mysql/:z \
                -v /var/containers/${MYSQL_INSTANCE_NAME}/var/backups/ejecucionesscript/:/var/backups/ejecucionesscript/:z \
                -v /var/containers/${MYSQL_INSTANCE_NAME}/tmp:/tmp/:z \
                --hostname=${MYSQL_INSTANCE_NAME}.service \
                --ulimit nofile=10240:10240 \
                --ulimit nproc=2000:2000 \
                -e TZ=America/Mexico_City \
                -v /etc/localtime:/etc/localtime:ro \
                -e 'MYSQL_ROOT_PASSWORD=crud' \
                --name=${MYSQL_INSTANCE_NAME} \
                mysql:5.7
```

Despues de tener el contenedor de mysql corriendo generamos la base de datos con la siguiente instruccion:

```bash
docker exec -it mysql57 mysql -uroot -pcrud -e "CREATE DATABASE crud_certificates;CREATE TABLE crud_certificates.domains (id INT PRIMARY KEY AUTO_INCREMENT,fulldomain VARCHAR(500), expiration_date DATE, description VARCHAR(1500));"
```

Finalmente levantamos el CRUD utilizando el siguiente comando:

```bash
docker run -d --name crud -p 3000:3000 --link mysql57:mysql57-crud -e MYSQL_HOST=mysql57-crud -e MYSQL_USER=root -e MYSQL_PASSWORD=crud kevout/crud-certificates
```