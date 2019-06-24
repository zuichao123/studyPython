#! /bin/bash
cruser=`who | sed -n '1p' | awk '{print $1}'`
time=`who | sed -n '1p' | awk '{print $3" " $4}'`
#time=$time":00"
curtime=`date "+%Y-%m-%d %H:%M:%S"`

c1=$(date +%s -d "${curtime}")
c2=$(date +%s -d "${time}")

echo -e "user: $cruser\nlogintime: $time"
echo -e "curretime: $curtime"
echo -e "totaltime: $(($c1-$c2))s"
