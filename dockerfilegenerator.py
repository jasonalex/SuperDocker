import argparse
import CONSTANTS
from string import Template


parser = argparse.ArgumentParser()
parser.add_argument("-o","--os",type=string, choices=['alpine', 'centos', 'debian'], help="Choose OS alpine/centos/ubuntu")
parser.add_argument("-p","--package",type=string, choices=['python', 'java'], help="Choose Package python/java")
parser.parse_args()


with open('{}-{}.template'.format(args.os, args.package), 'r') as file:
    text = file.read()

subd = {
##Python
python-gpg-key = CONSTANTS.python-gpg-key
python-version = CONSTANTS.python-version
pip-version    = CONSTANTS.pip-version
pip-url        = CONSTANTS.pip-url
pip-sha        = CONSTANTS.pip-sha
alpine-version = CONSTANTS.alpine-version
}

with open('{}/Dockerfile'.format(args.package), 'rw') as file:
    file.write(Template(text).safe_substitute(subd))
