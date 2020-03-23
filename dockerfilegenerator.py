import argparse
import CONSTANTS
from string import Template


parser = argparse.ArgumentParser()
parser.add_argument("-o","--os", choices=['alpine','debian'], help="Choose OS alpine/debian", required=True)
parser.add_argument("-p","--package", choices=['python', 'java'], help="Choose Package python/java", required=True)
args=parser.parse_args()


with open('templates/{}-{}.template'.format(args.os, args.package), 'r') as file:
    text = file.read()

subd = {
            "python_gpg_key" : CONSTANTS.python_gpg_key,
            "python_version" : CONSTANTS.python_version,
            "pip_version"    : CONSTANTS.pip_version,
            "pip_url"        : CONSTANTS.pip_url,
            "pip_sha"        : CONSTANTS.pip_sha,
            "alpine_version" : CONSTANTS.alpine_version,
            "debian_version" : CONSTANTS.debian_version
        }

with open('build/Dockerfile', 'w') as file:
    file.write(Template(text).safe_substitute(subd))
