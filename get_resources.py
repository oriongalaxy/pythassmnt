import boto3
client = boto3.client('resourcegroupstaggingapi')
client.get_resources()
responses = client.get_resources()

for response in responses['ResourceTagMappingList']:
    print(response['ResourceARN'])