#!/bin/bash
ssh-agent bash -c "ssh-add $1; git clone git@github.com:/$2.git"
pwd
cd $3
grails clean-all --stacktrace
grails war --stacktrace
mv target/*.war ..
