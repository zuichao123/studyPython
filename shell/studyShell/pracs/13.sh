#! /bin/bash
IP=`ifconfig eth0 | grep 'inet ' | sed 's/^.*addr://g' | sed 's/ Bcast.*$//g'`
Bcast=`ifconfig eth0 | grep 'inet ' | sed 's/^.*Bcast://g' | sed 's/ Mask.*$//g'`
NETMASK=`ifconfig eth0 | grep 'inet ' | sed 's/^.*Mask://g'`

echo "IP--> $IP"
echo "Bcast--> $Bcast"
echo "Mask--> $NETMASK"
exit 0
