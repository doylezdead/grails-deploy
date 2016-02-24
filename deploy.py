import subprocess as sp
import json
import argparse


def init():
    pass

def deploy():
    pass



parser = argparse.ArgumentParser()
parser.add_argument('init', nargs='?', default='')
args = parser.parse_args()
if args.init == 'deploy':
    deploy()
if args.init == 'init':
    init()

