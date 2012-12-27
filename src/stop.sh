curdir=$(cd "$(dirname $0)"; pwd)
ps -ef | grep ${start_cmd}/run.py | grep -v grep | cut -c 9-15 | xargs kill
