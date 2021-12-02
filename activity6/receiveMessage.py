import boto3

queueUrl = 'https://queue.amazonaws.com/564393646252/sajythomas-queue'
client = boto3.client('sqs')

response = client.receive_message(
    QueueUrl=queueUrl,
    MaxNumberOfMessages=1
)
#print(response)
try:
    messages = response ['Messages'][0]
    messageId = response ['Messages'][0]["MessageId"]
    print('Message Id=',messageId)
    message = response ['Messages'][0]["Body"]
    print('Message=',message)
    response = client.delete_message(
        QueueUrl=queueUrl,
        ReceiptHandle=response["Messages"][0]["ReceiptHandle"]
    )
except KeyError:
    print('No messages on the queue!')
    messages = []