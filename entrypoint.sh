#!/bin/sh

set -ex

if [ "$1" = 'test' ]; then
  # Run tests (if any)
  exec python -m unittest
elif [ "$1" = 'dev' ]; then
  # Run in port 8080 (which usually is available) and enable uWSGI "hot-reload"
  uwsgi --http-socket :8080 --py-autoreload 1 --wsgi-file service.py --callable app
else
  # Start HTTP service
  # uWSGI command as per https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
  uwsgi --http-socket :80 --wsgi-file service.py --callable app
fi