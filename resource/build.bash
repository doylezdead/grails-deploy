#!/bin/bash
ssh-agent bash -c "ssh-add $1; git clone git@github.com:/$2.git"
pwd
cd $3
grails clean-all
grails war
mv target/*.war ..

exit
