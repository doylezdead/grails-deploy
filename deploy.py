#!/usr/bin/env python

import os
import json
import argparse
import shutil
import subprocess as sp

prefix = os.path.dirname(os.path.realpath(__file__))
config = json.load(open(prefix + '/conf/config.json'))


def init():
    if config.get('server_key') == '':
        os.system('ssh-keygen -b 2048 -t rsa -f conf/server_key -q -N ""')
        config['server_key'] = 'conf/server_key'

    if config.get('git_key') == '':
        os.system('ssh-keygen -b 2048 -t rsa -f conf/git_key -q -N ""')
        config['git_key'] = 'conf/git_key'

    with open(prefix + '/conf/config.json', 'w') as f:
        json.dump(config, f, indent=4)

    print('copy your public keys to their appropriate locations. (Read the README getting started)')


def build():
    git_repo = config.get('git_repo')
    git_project = git_repo.split('/')[1]

    # set up absolute path (ssh-add needs an absolute path)
    if config.get('git_key').startswith('/'):
        pk_path = config.get('git_key')
    else:
        pk_path = prefix + '/' + config.get('git_key')

    # run build
    sp.Popen(['bash', 'resource/build.bash', pk_path, git_repo, git_project]).wait()

    shutil.rmtree(git_project)

    namelist = os.listdir('.')
    project_name = ''
    for x in namelist:
        if '.war' in x:
            project_name = x

    return project_name


def deploy(filename, purge=False):
    sp.Popen(['bash', 'resource/upload.bash', config.get('server_key'), config.get('server_user'), config.get('server_host'), config.get('server_deploy_path'), filename, filename.split('.')[0]]).wait()

    if purge:
        os.remove(filename)


parser = argparse.ArgumentParser()
parser.add_argument('init', nargs='?', default='')
args = parser.parse_args()

if args.init == 'init':
    init()

elif args.init.endswith('.war'):
    deploy(args.init)

elif args.init == 'build':
    build()

else:
    deploy(build(), purge=True)
