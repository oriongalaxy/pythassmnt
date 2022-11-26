import boto3

ec2client = boto3.client('ec2')
regionresponse = ec2client.describe_regions()
for region in regionresponse["Regions"]:
    regionname = region["RegionName"] 
    print(regionname) 

ec2client = boto3.client('ec2', region_name=regionname)
instanceresponse = ec2client.describe_instances()
for reservation in instanceresponse["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"])