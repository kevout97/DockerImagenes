#!/bin/bash
while [ 0 ] ; do
    top -u named -n 1 | grep named
    if [ $? -ne 0 ] ; then
        /usr/sbin/named -g -u named 2> /dev/null &
        if [ $? -eq 0 ]; then
            echo "named runing..."
        else
            echo "The process could not be initialized"
        fi
    fi
fi