#!/bin/bash

# 1 = server key full path
# 2 = server user
# 3 = server host
# 4 = server path
# 5 = project filename
# 6 = project dirname

scp -i $1 resource/replace.bash $2@$3:$4

scp -i $1 $5 $2@$3:$4

echo "Deploying war to tomcat..."
echo "This may take a while... be patient"
ssh $2@$3 -i $1 "cd $4; bash replace.bash $4 $5 $6"
echo "Done!"
exit
