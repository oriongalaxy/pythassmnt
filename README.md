
## AWS API CALL USING PYTHON 

# Prerequisites 
* AWS Acccount
* Git 
* Python 
* BOTO3

## Authentication for permissions
The following are options for providing permissions to the aws.

**Utilize IAM Roles**
* Create IAM Role With Required Policies.
* * VPCFullAccess
* * EC2FullAcces
* * S3FullAccess ..etc
* Attach IAM Role to EC2 Instance.

**Utilize AWS Vault** 
 ```
 #Guideline shown
 https://github.com/99designs/aws-vault/
```
**Utilize AWS configure**
```
Aws configure
Enter Access Key Id: %%%
Enter Secret Key: %%% 
```
## Guidelines to install python and BOTO3 
 ```
 https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
```

## Get configuration files from REPO
Utilize the command below to clone the repo
 ```
 git clone "https://github.com/oriongalaxy/pythassmnt" 
 ```
