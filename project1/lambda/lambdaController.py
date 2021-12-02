import boto3
import json
import time

def getQueueName():
  #QueueName=os.environ['SQS_QUEUE_NAME']
  queueName = 'backend-queue'
  return queueName
  
def invoke_ec2events_function(receiptHandle, source, instanceId, state):
    payload={'ReceiptHandle':receiptHandle,"Source":source,"state":state}
    print(f'EC2 event detected! Invoking ec2events-function {payload}')

    """
    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
            FunctionName="loadSpotsAroundPoint",
            InvocationType='Event',
            Payload=payload3
    )
    print(response)
    """
    
states = ["shutting-down", "stopped", "terminated"]
sqs_client = boto3.client('sqs')
#queue_url = sqs_client.get_queue_url(QueueName=os.environ['SQS_QUEUE_NAME'])['QueueUrl']
queueName = getQueueName();
try:
    queue_url = sqs_client.get_queue_url(QueueName=queueName)['QueueUrl']

    response = sqs_client.receive_message(
        QueueUrl=queue_url,
        AttributeNames=['All'],
        MaxNumberOfMessages=1
    )
    print(f"Number of messages received: {len(response.get('Messages', []))}")
    for message in response.get("Messages", []):
        message_body = message["Body"]
        receiptHandle= message['ReceiptHandle']
        jsonObject = json.loads(message_body)
        source = jsonObject['source']
        detail= jsonObject['detail']
        instanceId = detail['instance-id']
            
        state = detail['state']

        print(f"****receiptHandle is {receiptHandle}" )
        print(f"****source is {source}" )
        print(f"Instance ID is {instanceId}")
        print(f"State is {state}")
            
        if state in states:
            invoke_ec2events_function(receiptHandle, source, instanceId, state);
            
            #delete the message processed
            response = sqs_client.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receiptHandle,
            )
            break
     
    #return {"status":"success"}
        
except:
    print("error processing Queue message ")
    #return {"status":"error"}
    
