#! /bin/bash
cat /etc/passwd | awk -F: '{if ($7!="") print $7}' | sort | uniq -c
