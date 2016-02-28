#!/usr/bin/env bash
set -x

echo `bin/nginx -V`

if [ $# -eq 0 ] ; then
    exec bin/start-nginx uwsgi --uid=nobody --ini=config/uwsgi.ini --wsgi=lindy.special920.wsgi:application
else
    exec "$@"
fi

