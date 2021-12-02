import boto3

#Set the ARM EC2 Instance Role heres
Role_ARN= 'arn:aws:iam::564393646252:instance-profile/LabInstanceProfile'
ec2_client = boto3.resource('ec2','us-east-1')
response = ec2_client.create_instances(
    ImageId='ami-0b1d9960f2367ccd2',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=2,
    IamInstanceProfile={
            'Arn': Role_ARN
    },
    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': False,
            'DeviceIndex': 0
        }
    ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'DataServer'
                },
            ]
        },
    ],
)

instance_id1 = response[0].instance_id
print(instance_id1)
instance_id2 = response[1].instance_id
print(instance_id2)

