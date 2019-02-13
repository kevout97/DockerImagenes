#!/bin/bash
if [ -z "$MYSQL_HOST" ]; then
    echo "Specify the host of the database"
    exit 1
elif [ -z "$MYSQL_USER" ]; then
    echo "Specify the user for the connection to the database"
    exit 1
elif [ -z "$MYSQL_PASSWORD" ]; then
    echo "WARNING: Empty password"
    echo "Runnig server...."
    python Crud.py $MYSQL_HOST $MYSQL_USER $MYSQL_PASSWORD
else
    echo "Runnig server...."
    python Crud.py $MYSQL_HOST $MYSQL_USER $MYSQL_PASSWORD
    exec "$@"
fi