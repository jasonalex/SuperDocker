import boto3
import argparse
from string import Template
import json

parser = argparse.ArgumentParser()
parser.add_argument("-c","--cx", help="customer account", required=True)
parser.add_argument("-o","--os", choices=['alpine','debian'], help="Choose OS alpine/debian", required=True)
parser.add_argument("-p","--package", choices=['python', 'java'], help="Choose Package python/java", required=True)
args=parser.parse_args()

session = boto3.session.Session()
ecr = session.client('ecr')

try:
    response = ecr.describe_repositories(repositoryNames=['{}-{}-{}'.format(args.os,args.package,args.cx)])
    print('Using Existing Repo')
except ecr.exceptions.RepositoryNotFoundException as e:
    print('Creating New Repo')
    ecr.create_repository(  repositoryName='{}-{}-{}'.format(args.os,args.package,args.cx),
                            imageTagMutability='MUTABLE',
                            imageScanningConfiguration={'scanOnPush': True})
    print('Setting Repo Policies')
    with open('aws_resources/ecr_policy.json','r') as file:
        text = file.read()
    temp = Template(text)
    ecr.set_repository_policy(
                                repositoryName='{}-{}-{}'.format(args.os,args.package,args.cx),
                                policyText=str(temp.substitute(account_id=args.cx)),
                                force= False
                            )
except:
    exit(1)
