#! /bin/bash
IP=`cat /etc/network/interfaces | grep 'address ' | sed 's/[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/ /g'`

NETMASK=`cat /etc/network/interfaces | grep 'netmask ' | sed 's/[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/ /g'`

GATEWAY=`cat /etc/network/interfaces | grep 'gateway ' | sed 's/[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/ /g'`

echo "IP--> $IP"
echo "Mask--> $NETMASK"
echo "GATEWAY--> $GATEWAY"
exit 0
