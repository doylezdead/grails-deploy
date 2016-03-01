# grails-deploy
script collection for deploying a grails application from github. Runs only on linux machines in MTU network. Use a vpn to run on a linux machine remotely. 

##### GETTING STARTED
1. Clone me to a linux machine on MTU network.
2. Edit "conf/config.json"
   - Edit the "sever_host" value to the tomcat server host domainname (probably "cshci-dev.mtu.edu")  
   - Edit the "server_deploy_path" value to the web-app path on the server (probably something like /usr/share/tomcat_*team name*, look in your credential file)
   - Edit the "sever_user" value to sever value (look in your credential file)
   - Edit git_user value to your github account username
3. Run "./deploy.py init" initialize new ssh key pairs in the conf directory.
  - This will also alter the conf/config.json file to reflect the new keys. override them there if you have your own key locations.
4. Append the "server_key.pub" to ~/.ssh/authorized_keys on the deployment server
5. Copy-paste the "git_key.pub" to your github account keys under Profile->Settings->SSH Keys->New SSH Key

##### BUILD AND DEPLOY
Run "./deploy.py" pulls project from github, builds, and deploys
- This clones the project and builds from the default branch (usually master)
- Uses config.json["git_key"] to authenticate with github
- Uses config.json["server_key"] to ssh and scp to deployment server
- Requires "git_key" to be set and valid in the config
- Requires "server_key" to be set and valid in the config

##### JUST BUILD
Run "./deploy.py build" pulls the project github and builds
- After the build is complete, the war file is copied to the directory
- Project directory is purged
- Requires "git_key" to be set and valid in the config

##### JUST DEPLOY
"./deploy.py \*.war" deploys the war file to deployment server
- Useful if you need to deploy an old build or grails is not installed on the machine
- Requires "server_key" to be set and valid in the config

##### CONFIG FORMAT
"conf/config.json"
- This file must stay in this location (other things get created here)
- For security purposes, the only authentication method is RSA keys. plaintext passwords not supported.
- serverkey and gitkey  get populated automatically by the init command
- git repo is the last 2 directories of the url of the git repo. i.e. "doylezdead/grails-project" for http://github.com/doylezdead/grails-project
- git user is your github username
- server deploy path is the path to the directory containing the webapps directory (but not including it)
- server user is the username for the deploy server   
    
    

