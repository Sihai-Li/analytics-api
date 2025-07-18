#!/bin/bash

cd /code

RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}

exec gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT main:app
