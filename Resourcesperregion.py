import boto3
client = boto3.client('resourcegroupstaggingapi')
client.get_resources()
#print(client.get_resources()['ResourceTagMappingList'])
for item in client.get_resources()['ResourceTagMappingList']:
    region = str(item).split(':')[4]
    print(region, '---', item['ResourceARN'])
