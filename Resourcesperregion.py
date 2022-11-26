import boto3
#utilizing boto3 api service for ec2. reference https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html
client = boto3.client('resourcegroupstaggingapi')
client.get_resources()
for item in client.get_resources()['ResourceTagMappingList']:
    region = str(item).split(':')[4]
    print(region, '---', item['ResourceARN'])
