# grails-deploy
scripts collection for deploying a grails application from github

GETTING STARTED
===============
"./deploy.py init" initialize new ssh key pairs in the conf directory.
    - This will also alter the conf/config.json file to reflect the new keys. override them there if you have your own key locations.
    - Append the "server_key.pub" to ~/.ssh/authorized_keys on the deployment server
    - copy-paste the "git_key.pub" to your github account keys under Profile->Settings->SSH Keys->New SSH Key

BUILD AND DEPLOY
================
"./deploy.py" pull project from github, build, and deploy
    - This clones the project and builds from the default branch (usually master)
    - Uses config.json["git_key"] to authenticate with github
    - Uses config.json["server_key"] to ssh and scp to deployment server

CONFIG FORMAT
=============
"conf/config.json"
    - This file must stay in this location (other things get created here)
    - For security purposes, the only authentication method is RSA keys. plaintext passwords not supported.
    - serverkey and gitkey  get populated automatically by the init command
    - git repo is the last 2 directories of the url of the git repo. i.e. "doylezdead/grails-project" for http://github.com/doylezdead/grails-project
    - git user is your github username
    - server deploy path is the path to the directory containing the webapps directory (but not including it)
    - server user is the username to the deploy server
    
    
    

