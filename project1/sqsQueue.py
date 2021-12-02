import boto3

sqs_client = boto3.client("sqs", region_name="us-east-1")

response = sqs_client.create_queue(
    QueueName='backend-queue',
    Attributes={
        'DelaySeconds': '10'
    }
)

print(response)
