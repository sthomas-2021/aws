import boto3
import json

queueUrl = 'https://queue.amazonaws.com/564393646252/sajythomas-queue'
client = boto3.client('sqs')

response = client.send_message(
    QueueUrl=queueUrl,
    MessageBody='UwBlAGMAcgBlAHQAIABtAGUAcwBzAGEAZwBlACAAZABlAGMAcgB5AHAAdABlAGQALAAgAGwAZQB0ACAAbQBlACAAawBuAG8AdwAgAHYAaQBhACAAZQBtAGEAaQBsACAAbwByACAAcwBsAGEAYwBrACAAZgBvAHIAIABhAG4AIABlAHgAdAByAGEAIABwAG8AaQBuAHQALgA='
)
print(response)

response = client.send_message(
    QueueUrl=queueUrl,
    MessageBody='Hello, here is a message from the queue!',
)
print(response)

jsonMessage = {"Event": "test123", "Key":"Value"}
#print(json.dumps(jsonMessage))
response = client.send_message(
    QueueUrl=queueUrl,
    MessageBody=json.dumps(jsonMessage),
)
print(response)