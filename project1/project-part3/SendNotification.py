import boto3

snsClient = boto3.client('sns')

response = snsClient.publish(
    TopicArn='arn:aws:sns:us-east-1:564393646252:ops-notify',
    Message='This is a test',
    Subject='EC2 Critical Event'
)

print(response)