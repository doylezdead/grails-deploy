#!/bin/bash
cd $1/webapps
rm $2

fullfile=$2
dirname=${fullfile%.war}

while [ `ls | grep -i dirname | wc -l` -gt 0 ]; do
    sleep .5;
done

sleep 2;
chmod 644 ../$2
mv ../$2 .
exit
