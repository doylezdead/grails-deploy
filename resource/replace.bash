#!/bin/bash
cd $1/webapps
rm $2
echo $3


while [ `ls | grep $3 | wc -l` -gt 0 ]; do
    continue
done

sleep 2;
chmod 644 ../$2
mv ../$2 .

while [ `ls | grep $3 | wc -l` -lt 1 ]; do
    continue
done

exit
