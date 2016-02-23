#!/usr/bin/env bash

export PATH=/app/bin:$PATH
NGINX_PATH=/tmp/nginx
mkdir -p ${NGINX_PATH}/config/ $NGINX_PATH/logs

cp -r /app/config/ ${NGINX_PATH}/config/
sed -i "s/__PORT__/${PORT}/g" ${NGINX_PATH}/config/sites-enabled/default

exec /app/bin/nginx-and \
    uwsgi \
    --uid=nobody \
    --socket=/tmp/uwsgi.sock \
    --wsgi-file=wsgi.py \
    --chmod-socket=666
