import boto3
from pprint import pprint

ec2_client = boto3.client('ec2', region_name='us-east-1')
