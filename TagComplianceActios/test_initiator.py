from modules.ebs import *
from modules.ec2 import *

# ebsDataDump = getEBSMetaData()
# ebsIdList = getEBSIdList(ebsDataDump)
# ebsVolumeData = ebsDataDump[7]
# res = check_if_tag_exists_on_EBS(ebsVolumeData , 'OWNER')
# print('result ', res)

# tagNames = ['PURPOSE' , 'ENV' , 'WNER' ]

# check_EBS_compliance(ebsVolumeData , tagNames)

ec2DataDump = getEC2MetaData()
#print(ec2DataDump)

#print(ec2DataDump[0]['Instances'])
data = ec2DataDump[0]['Instances']
# print(data)
tagList = getTagList(data)
# print(tagList)

#tagValue = getValueOfTag(data , 'stopDate')
# print(tagValue)

# checkIfNonCompliantEC2(data)

nonCompliantEC2List = getAllNonCompliantEC2ForStopping(ec2DataDump)

print(nonCompliantEC2List)

stopAllNonCompliantEC2(nonCompliantEC2List)
