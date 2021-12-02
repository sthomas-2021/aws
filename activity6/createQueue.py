import boto3


client = boto3.client('sqs')

response = client.create_queue(
    QueueName='sajythomas-queue',
    Attributes={
        'DelaySeconds': '10'
    }
)

print(response)