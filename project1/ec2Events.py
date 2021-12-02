import boto3
import json

#***Set ec2 instance ids here before executing the code***
#------------------------------------------
eC2Instance1 =  '"i-0d0eed37f4e7c9a1e"'
eC2Instance2= '"i-0a336fb0fe8edaec5"'
SQS_ARN ="arn:aws:sqs:us-east-1:564393646252:backend-queue";
#----------------------------------------

eC2Instances = eC2Instance1 + "," + eC2Instance2

#Set the ARM EC2 Instance Role heres
Role_ARN= 'arn:aws:iam::564393646252:instance-profile/LabInstanceProfile'
Role_ARN1='arn:aws:events:us-east-1:564393646252:rule/S3BucketEvents'

QueueUrl = 'https://queue.amazonaws.com/564393646252/backend-queue'
bucketName='rlc-app-dev-2021-sajythomas'

#Create cloudwatch rule and associated event for ec2 instances
client = boto3.client('events')

eventPattern = """{
                     "source": ["aws.ec2"],
                     "region": ["us-east-1"],
                     "detail-type": ["EC2 Instance State-change Notification"],
                     "detail": {
                        "instance-id":[""" + eC2Instances + """ ],
                        "state": ["shutting-down", "stopped", "terminated"]
                     }
                }"""

response = client.put_rule(
    Name='ec2EventsRule',
    EventPattern=eventPattern,
    State='ENABLED',
    Description='ec2EventsRule'
)

print (response)

# Create SQS client
sqs = boto3.client('sqs')
#Send events to sqs queue
response = client.put_targets(
    Rule='ec2EventsRule',
    Targets=[
        {
            'Arn': '' +  SQS_ARN + '',
            'Id': 'myCloudWatchEventsEC2Events',
        }   
    ]
)

print(response)