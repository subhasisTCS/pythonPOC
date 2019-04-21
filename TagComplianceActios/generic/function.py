import boto3
from pprint import pprint
import connections as con
# ebsVolumeData =  {'Attachments': [{'AttachTime': datetime.datetime(2019, 2, 14, 6, 54, 28, tzinfo=tzutc()),
#                    'DeleteOnTermination': True,
#                    'Device': '/dev/sda1',
#                    'InstanceId': 'i-0ca202573ae7562ba',
#                    'State': 'attached',
#                    'VolumeId': 'vol-075ba8e2136c45fc4'}],
#   'AvailabilityZone': 'us-east-1c',
#   'CreateTime': datetime.datetime(2019, 2, 14, 6, 54, 28, 128000, tzinfo=tzutc()),
#   'Encrypted': False,
#   'Iops': 100,
#   'Size': 20,
#   'SnapshotId': 'snap-0f08fe61aa57fc583',
#   'State': 'in-use',
#   'Tags': [{'Key': 'OWNER ', 'Value': 'SIDD'},
#            {'Key': 'PURPOSE', 'Value': 'POC'},
#            {'Key': 'ENV', 'Value': 'DEV'}],
#   'VolumeId': 'vol-075ba8e2136c45fc4',
#   'VolumeType': 'gp2'}

#ec2_client = boto3.client('ec2', region_name='us-east-1')

def getEBSMetaData():
    ebsDataDump = con.ec2_client.describe_volumes()['Volumes']
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