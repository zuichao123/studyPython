#! /bin/bash
for i in (9901..9930); do
	xx=`echo $i | sed 's/99//g'`
		userdel -r sj$xx
done
