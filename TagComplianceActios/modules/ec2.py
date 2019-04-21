import generic.connections as con
from generic.variables import *
import botocore
import boto3
from botocore.exceptions import ClientError

nonCompliantEC2List = []

def getEC2MetaData():
    ec2DataDump = con.ec2_client.describe_instances()['Reservations']
    return ec2DataDump

def getTagList(ec2Data):
    tagList = []
    for ec2 in ec2Data:
        if 'Tags' in ec2:
            tagList = ec2['Tags']

    return tagList

def getValueOfTag(tagList , tagName):
    tagValue = ""
    
    for tag in tagList:
        if tag['Key'] == tagName:
            tagValue = tag['Value']

    return tagValue

def checkIfNonCompliantEC2(ec2Data):
    tagList = getTagList(ec2Data)

    if getValueOfTag(tagList , 'compliant') == 'no':
        print('hi')
        if getValueOfTag(tagList, 'stopDate') == curDate:
            print('Need to be stopped')
            return True
    else:
        print('hello')
        return False

def getAllNonCompliantEC2ForStopping(ec2DataDump):
    for ec2 in ec2DataDump:
        ec2Data = ec2['Instances']
        if checkIfNonCompliantEC2(ec2Data):
            nonCompliantEC2List.append(ec2Data[0]['InstanceId'])

    return nonCompliantEC2List

def stopAllNonCompliantEC2(ec2List):
    try:
        con.ec2_client.stop_instances(InstanceIds=ec2List)
        print('stopped instances')

    except ClientError as e:
        print(e)  
    