#!/bin/bash
cd $1/webapps
rm $2


while [ `ls | grep $3 | wc -l` -gt 0 ]; do
    sleep .5;
done

sleep 2;
chmod 644 ../$2
mv ../$2 .
exit
