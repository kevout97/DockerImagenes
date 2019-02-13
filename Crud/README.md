# Crud Certificates

# install dependencies
- pip install flask
- pip install flask-mysqldb

# issues
- sudo yum install mariadb-devel

docker run -d --name crud -p 3000:3000 --link mysql57:mysql57-crud -e MYSQL_HOST=mysql57-crud -e MYSQL_USER=root -e MYSQL_PASSWORD=crud kevout/crud-certificates
