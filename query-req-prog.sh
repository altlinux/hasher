#!/bin/sh -e
# Usage: hsh --query-req-prog=path_to_this_script

rpmquery -pR -- "$@"
