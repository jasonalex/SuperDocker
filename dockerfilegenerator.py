import argparse
from string import Template


parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",type=string, choices=['alpine', 'centos', 'ubuntu'], help="Choose OS alpine/centos/ubuntu")
parser.add_argument("-p","--package",type=string, choices=['python', 'java'], help="Choose Package python/java")
parser.parse_args()


with open('{}-{}.template'.format(args.image, args.package), 'r') as file:
    template = file.read()
