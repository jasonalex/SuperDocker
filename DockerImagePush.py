import boto3
import argparse
from string import Template
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument("-c","--cx", help="customer account", required=True)
parser.add_argument("-o","--os", choices=['alpine','debian'], help="Choose OS alpine/debian", required=True)
parser.add_argument("-p","--package", choices=['python', 'java'], help="Choose Package python/java", required=True)
args=parser.parse_args()

session = boto3.session.Session()
ecr = session.client('ecr')

try:
    response = ecr.describe_repositories(repositoryNames=['{}-{}-{}'.format(args.os,args.package,args.cx)])
    uri = response['repositories'][0]['repositoryUri']
    print('Logging in to ECR')
    os.system('aws ecr get-login-password | docker login --username AWS --password-stdin {}'.format(uri))
    os.system('docker tag {}-{}-{}:latest')
    os.system('docker tag {}-{}:latest {}:latest'.format(args.os,args.package,uri))
    os.system('docker push {}:latest'.format(uri))
    
except:
    exit(1)
