#!/bin/bash
#设计一个shell程序，添加一个新组为class1，然后添加属于这个组的30个用户，用户名的形式为stdxx，其中xx从01到30。
#请 su root  或者 sudo su  变成root用户

groupadd class1
for i in {9901..9930}; do
    xx=`echo $i | sed 's/99//g'`
    useradd -g class1 -s /bin/bash -d /home/sj$xx -m sj$xx
    echo -e "sj$xx\nsj$xx" | passwd sj$xx 
    echo -e "user sj$xx password is sj$xx" >> /home/sunjian/Desktop/newuser.txt
done
