#!/usr/bin/env bash
set -x

sed -i "s/__PORT__/${PORT}/g" /etc/nginx/sites-enabled/default

if [ $# -eq 0 ] ; then
    exec nginx-and uwsgi --uid=nobody --socket=/tmp/uwsgi.sock --wsgi-file=wsgi.py --chmod-socket=666
else
    exec "$@"
fi

