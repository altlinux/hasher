#!/bin/sh -e
# Usage: hsh --query-req-prog=path_to_this_script

TMPDIR="$HOME/tmp"
export TMPDIR
cd /.in

rpmquery -pR -- "$@"
