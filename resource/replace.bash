#!/bin/bash
cd $1/webapps
rm $2.war

while [ `ls | grep -i $2 | wc -l` -gt 0 ]; do
    sleep 1;
done

sleep 2;
chmod 644 ../$2.war
mv ../$2.war .
exit
