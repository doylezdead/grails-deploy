# grails-deploy
scripts collection for deploying a grails application from github

##### GETTING STARTED
"./deploy.py init" initialize new ssh key pairs in the conf directory.
- This will also alter the conf/config.json file to reflect the new keys. override them there if you have your own key locations.
- Append the "server_key.pub" to ~/.ssh/authorized_keys on the deployment server
- copy-paste the "git_key.pub" to your github account keys under Profile->Settings->SSH Keys->New SSH Key

###### CONFIG FORMAT
"conf/config.json"
- This file must stay in this location (other things get created here)
- For security purposes, the only authentication method is RSA keys. plaintext passwords not supported.
- serverkey and gitkey  get populated automatically by the init command
- git repo is the last 2 directories of the url of the git repo. i.e. "doylezdead/grails-project" for http://github.com/doylezdead/grails-project
- git user is your github username
- server deploy path is the path to the directory containing the webapps directory (but not including it)
- server user is the username to the deploy server

##### BUILD AND DEPLOY
"./deploy.py" pull project from github, builds, and deploy
- This clones the project and builds from the default branch (usually master)
- Uses config.json["git_key"] to authenticate with github
- Uses config.json["server_key"] to ssh and scp to deployment server
- Requires "git_key" to be set and valid in the config
- Requires "server_key" to be set and valid in the config

##### JUST BUILD
"./deploy.py build" pulls the project github and build
- After the build is complete, the war file is copied to the directory
- Project directory is purged
- Requires "git_key" to be set and valid in the config

##### JUST DEPLOY
"./deploy.py \*.war" deploys the war file to deployment server
- Useful if you need to deploy an old build or grails is not installed on the machine
- Requires "server_key" to be set and valid in the config

    
    
    

