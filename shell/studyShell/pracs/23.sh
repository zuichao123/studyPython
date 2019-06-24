#! /bin/bash
filename=`date +%Y%m%d`_shell.tar.gz
#cd /etc
tar -zcvf $filename *
mv $filename /home/sunjian/Desktop/
