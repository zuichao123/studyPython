#! /bin/bash
free -m | sed -n '/Mem/p' | awk '{print $2}'
