#!/bin/bash
set -e
if ! [ -f /etc/rndc.key ] ; then
        rndc-confgen -a -c /etc/rndc.key
        chgrp named /etc/rndc.key
        chmod 640 /etc/rndc.key
fi
if [[ -z ${1} ]]; then
  echo "Starting named..."
  exec $(which named) -u named -g
else
  exec "$@"
fi