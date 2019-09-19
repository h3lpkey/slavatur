#!/bin/bash
set -e
SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LOGFILE=$SCRIPTPATH/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=root
GROUP=root
PORT=8010
cd /sites/slavatur_site/slavatur
source /sites/slavatur_env/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec /sites/slavatur_env/bin/gunicorn slavatur.wsgi:application -w $NUM_WORKERS \
--user=$USER --group=$GROUP --log-level=debug \
--log-file=$LOGFILE  \
--bind 127.0.0.1:$PORT
