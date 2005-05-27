#!/bin/sh -e
# Usage: hsh --rebuild-prog=path_to_this_script

# install source package
rpmi -i -- "$@"

# find specfile
specdir="`rpm --eval %_specdir`"
specfile=`ls "$specdir"/*`
[ -f "$specfile" ]

# increment release
sed -i 's/^release[[:space:]]*:[[:space:]]*\([^[:space:]]\+\)[[:space:]]*$/Release: \1.1/I' "$specfile"

# add changelog entry
d="`LC_TIME=C date '+%a %b %d %Y'`"
n='%|SERIAL?{%{SERIAL}:}|%{VERSION}-%{RELEASE}'
p='Joe Hacker <joe@email.address>'
e='- Rebuilt.'
q="* $d $p $n\n"
add_changelog -e "$e" -a "-q --qf '$q'" "$specfile"

# build source package from specfile
exec nice time rpmbuild -bs --nodeps "$specfile"
