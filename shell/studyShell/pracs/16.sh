#! /bin/bash
username=$USER
time=`date +%y-%m-%d\ %H:%M:%S`
termenal=`ps | grep bash | grep -v grep | awk '{print $2}'`
location=`w | grep "$termenal" | awk '{print $3}'`
echo -e "$username\t$time\t$location" >> /home/sunjian/Desktop/log
