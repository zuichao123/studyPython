# coding:utf-8
"""
# 1、两个数相加

    #! /bin/bash
    first=0
    second=0
    read -p "Input the first number:" first
    read -p "Input the second number:" second
    result=$[$first+$second]
    echo "result is : $result"
    exit 0

# 2、1--100的和

    #! /bin/bash
    SUM=0
    I=0
    while [ $I -le 100 ]; do
            SUM=$((SUM+I))
            I=$((I+1))
    done
    echo "1+2+3+...+100=$SUM"

# 3、修改当前路径下所有的后缀名

    #! /bin/bash
    for i in *.*; do
            mv $i ${i%%.*}.bak
    done

# 4、编译当前路径下所有的.c文件
    #! /bin/bash
    for file in *.c; do echo $file ; gcc -o $(basename $file .c) $file ; sleep 2; done > compile 2>&1

# 5、打印root用户可执行的文件数
    #! /bin/bash
    echo "root's bins: $(find ./ -type f | xargs ls -l | sed '/-..x/p' | wc -l)"

# 6、打印当前sshd的端口和进程id，处理结果：sshd Port && pid:22 5412
    #! /bin/bash
    netstat -apn | grep sshd | sed -n 's/.*:::\([0-9]*\)\ .* \ \([0-9]*\)\/sshd/\1 \2/p'

# 7、输出本机创建2000个目录所用的时间
    #! /bin/bash
    time (
    for i in {1..2000} ; do
        mkdir /tmp/nnn$i
    done
    )

# 8、输出本机的交换分区大小
    #! /bin/bash
    free -m | sed -n '/Swap/p' | awk '{ print $2}'

# 9、文本分析，取出/etc/password中的shell出现的次数
    #! /bin/sh
    cat /etc/passwd | awk -F: '{if ($7!="") print $7}' | sort | uniq -c
    # cat /etc/passwd|awk -F: '{if ($7!="") print $7}'| sort | uniq -c | awk '{print $2,$1}'

# 10、将两个文件中的内容合并（-k 2表示：根据第二列排序）
    #! /bin/bash
    join employee.txt bonus.txt | sort -k 2

# 11、使用shell脚本来得到当前日期、时间、用户名和当前工作路径
    #!/bin/bash
    echo "Hello, $LOGNAME"
    echo "Current date is `date`"
    echo "User is `who i am`"
    echo "Current directory `pwd`"

# 12、编写一个shell获得本机的网络地址
    #!/bin/bash

    #This script print ip and network
    IP=`ifconfig eth0 | grep 'inet ' | sed 's/^.*addr://g' | sed 's/ Bcast.*$//g'`
    NETMASK=`ifconfig eth0 | grep 'inet '| sed 's/^.*Mask://g'`

    #echo "$IP/$NETMASK"
    echo "$IP"
    exit 0

    --------------------------------
    #! /bin/bash
    IP=`cat /etc/network/interfaces | grep 'address ' | sed 's/[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/ /g'`

    NETMASK=`cat /etc/network/interfaces | grep 'netmask ' | sed 's/[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/ /g'`

    GATEWAY=`cat /etc/network/interfaces | grep 'gateway ' | sed 's/[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/ /g'`

    echo "IP--> $IP"
    echo "Mask--> $NETMASK"
    echo "GATEWAY--> $GATEWAY"
    exit 0

# 13、编写个shell脚本将当前目录下大于10K的文件转移到/tmp目录下
    #/bin/bash
    # Using for move currently directory lt 10k file to /tmp

    for FileName in `ls -l | awk '$5>10240 {print $9}'`; do
        mv $FileName /tmp
    done

    ls -al /tmp

    echo "Done! "

# 14、编写一个名为myfirstshell.sh的脚本，它包括以下内容。
    a) 包含一段注释，列出您的姓名、脚本的名称和编写这个脚本的目的。
    b) 问候用户。
    c) 显示日期和时间。
    d) 显示这个月的日历。
    e) 显示您的机器名。
    f) 显示当前这个操作系统的名称和版本。
    g) 显示父目录中的所有文件的列表。
    h) 显示root正在运行的所有进程。
    i) 显示变量TERM、PATH和HOME的值。
    j) 显示磁盘使用情况。
    k) 用id命令打印出您的组ID。
    m) 跟用户说“Good bye”

    #!/bin/bash
    user=`whoami`
    case $user in
        root)
            echo "hello root";;
        sunjian)
            echo "hello sunjian";;
        *)
            echo "hello $user,welcome"
    esac

    echo "日期和时间: `date`"
    echo "本月的日历: `cal`"
    echo "本机的机器名:`uname -n`"
    echo "当前这个操作系统的名称和版本:`uname -s;uname -r`"
    echo "父目录中的所有文件的列表:`ls ../`"
    echo "root正在运行的所有进程:` ps -u root`"
    echo "变数TERM的值:$TERM"
    echo "变数PATH的值:$PATH"
    echo "变数HOME的值:$HOME"
    echo "磁盘的使用情况:`df`"
    echo "用id命令打印出你的组ID:`id -g`"
    echo "Good bye!"
    exit 0

# 15、文件拷贝到名称对应的目录中
    #!/bin/bash
    touch m1.txt m2.txt m3.txt m4.txt
    I=1

    while [ $I -le 4 ]; do
        mkdir m$I
        mv m$I.txt m$I
        I=$((I+1))
    done

# 16、root用户今天登陆了多长时间
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

# 17、终端输入一个文件名，判断是否是设备文件
    #/bin/bash
    echo -e "The program will Judge a file is or not a device file.\n\n"
    read -p "Input a filename:" filename

    if [ -b $filename -o -c $filename ]; then
        echo "$filename is a device file"
        exit 0
    else
        echo "$filename is not a device file"
        exit 1
    fi

# 18、统计IP访问：要求分析apache访问日志，找出访问页面数量在前100位的IP数。日志大小在78M左右。以下是apache的访问日志节选
    #! /bin/bash
    # $1 为要测试的日志文件
    awk '{print $1}' $1 | sort | uniq -c | sort -k1nr | head -n3

# 19、设计一个Shell程序，在/userdata目录下建立50个目录，即user1～user50，并设置每个目录的权限，其中其他用户的权限为：读；文件所有者的权限为：读、写、执行；文件所有者所在组的权限为：读、执行。
    #!/bin/bash
    # 需要root权限
    echo "create /usrdata"
    mkdir usrdata
    if [ $? -eq 0 ]; then
            i=1
            while [ $i -le 50 ]; do
                    mkdir -p usrdata/user$i
                    chmod 754 usrdata/user$i
                    let i++
            done
    else
            echo "bye"
            exit 1
    fi
    exit 0

# 20、设计一个shell程序，添加一个新组为class1，然后添加属于这个组的30个用户，用户名的形式为sjxx，其中xx从01到30，并设置密码为对应的sjxx。
    #!/bin/bash
    #设计一个shell程序，添加一个新组为class1，然后添加属于这个组的30个用户，用户名的形式
    为sjxx，其中xx从01到30。
    #请 su root  或者 sudo su  变成root用户

    groupadd class1
    for i in {9901..9930}; do
        xx=`echo $i | sed 's/99//g'`
        useradd -g class1 -s /bin/bash -d /home/sj$xx -m sj$xx
        echo -e "sj$xx\nsj$xx" | passwd sj$xx
        echo -e "user sj$xx password is sj$xx" >> /home/sunjian/Desktop/newuser.txt
    done

# 21、













"""
