#!/usr/bin/env bash
set -x

sed -i "s/__PORT__/${PORT}/g" /etc/nginx/sites-enabled/default

exec nginx-and uwsgi --uid=nobody --socket=/tmp/uwsgi.sock --wsgi-file=wsgi.py --chmod-socket=666
