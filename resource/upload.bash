#!/bin/bash

# 1 = server key full path
# 2 = server user
# 3 = server host
# 4 = server path
# 5 = project filename

scp -i $1 resources/replace.bash $2@$3:$4

scp -i $1 $5 $2@$3:$4

ssh $2@$3 -i $1 "cd $4; bash replace.bash $4 $5"&&

exit