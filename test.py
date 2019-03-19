import boto3
from pprint import pprint

ec2_client = boto3.client('ec2', region_name='us-east-1')

def getEBSMetaData():
    ebsDataDump = ec2_client.describe_volumes()['Volumes']
    # pprint(ebsDataDump)
    return ebsDataDump

def getEBSIdList(ebsDataDump):
    ebsIdList = []
    for ebs in ebsDataDump:
        ebsIdList.append(ebs['VolumeId'])

    print(ebsIdList)
    return ebsIdList

def check_if_tag_exists_on_EBS(ebsVolumeData , tagName):
    if 'Tags' in ebsVolumeData:
        for tag in ebsVolumeData['Tags']:
            if tag['Key'] == tagName:
                print(tagName, 'tag exists')
                return True
        print(tagName , 'tag not exists')
        return False
    else:
        print('No Tags exists')
        return False

def check_EBS_compliance(ebsVolumeData , tagNames):
    tagCount = 0
    for tagName in tagNames:
        if check_if_tag_exists_on_EBS(ebsVolumeData , tagName):
            tagCount += 1

    if len(tagNames) == tagCount:
        print('Compliant')
    else:
        print('Non Compliant')


    
ebsDataDump = getEBSMetaData()
ebsIdList = getEBSIdList(ebsDataDump)
ebsVolumeData = ebsDataDump[7]
res = check_if_tag_exists_on_EBS(ebsVolumeData , 'OWNER')
print('result ', res)

tagNames = ['PURPOSE' , 'ENV' , 'WNER' ]

check_EBS_compliance(ebsVolumeData , tagNames)
