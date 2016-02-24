#!/bin/env python

import subprocess as sp
import os
import json
import argparse
import shutil

prefix = os.path.dirname(os.path.realpath(__file__))

def init():
    print prefix


def deploy():

    config = json.load(open(prefix + '/conf/config.json'))
    git_repo = config.get('git_repo')
    git_project = git_repo.split('/')[1]

    if config.get('git_password') == '':
        os.system('ssh-agent $(ssh-add ' + prefix + '/' + config.get('git_private_key') + '; git clone git@github.com:/' + git_repo + '.git)')
        print 'done'
    else:
        os.system('git clone https://' + config.get('git_user') + ':' + config.get('git_password') + '@github.com/' + git_repo)

    os.system('cd ' + git_project + '; grails clean-all; grails war; cp target/*.war ..')
    namelist = os.listdir('.')
    project_name = ''
    for x in namelist:
        if '.war' in x:
            project_name = x.split('.')[0]
    print project_name

    shutil.rmtree(git_project)

    os.system('scp -i ' + config.get('server_private_key') + ' resources/replace.bash ' + config.get('server_username') + '@' + config.get('server_host') + ':' + config.get('server_deploy_path'))
    os.system('scp -i ' + config.get('server_private_key') + ' ' + project_name + '.war ' + config.get('server_username') + '@' + config.get('server_host') + ':' + config.get('server_deploy_path'))
    os.system("ssh " + config.get('server_username') + '@' + config.get('server_host') + " -i " + config.get('server_private_key') + "'cd " + config.get('server_deploy_path') + "; bash replace.bash'&&")

    os.remove(project_name + '.war')


parser = argparse.ArgumentParser()
parser.add_argument('init', nargs='?', default='')
args = parser.parse_args()

if args.init == 'init':
    init()

else:
    deploy()

