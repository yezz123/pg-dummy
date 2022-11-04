#!/usr/bin/env bash

set -e
set -x

python -m pg_dummy --host localhost --database postgres --user postgres --password postgres --table data --length 120