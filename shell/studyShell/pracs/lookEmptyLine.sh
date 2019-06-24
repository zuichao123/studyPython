#! /bin/sh
awk '/^ *$/ {x=x+1;} END {print x}' $1
