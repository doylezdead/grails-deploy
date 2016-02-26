#!/bin/bash
ssh-agent $(ssh-add $1; git clone git@github.com:/$2.git)
cd $3
grails clean-all
grails war
mv target/*.war ..

exit
