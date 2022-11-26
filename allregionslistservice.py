import boto3
client = boto3.client('ec2')
all_regions = client.describe_regions()
region_lists=[]
for reg in all_regions['Regions']:
    region_lists.append(reg['RegionName'])
    for reg in region_lists:
        ec2client = boto3.client('ec2',region_name=reg)
        print("list of ec2", reg)
        instanceresponse = ec2client.describe_instances()
        for reservation in instanceresponse["Reservations"]:
            #for instance in reservation["Instances"]:
                print(reservation["Instances"])
