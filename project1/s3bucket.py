import boto3
import botocore
import json

s3 = boto3.resource('s3')
bucketName='rlc-app-dev-2021-sajythomas'
response = s3.create_bucket(Bucket=bucketName)
print(response)

response = s3.Object(bucketName, 'sample-data.txt').put(Body=open('./sample-data.txt', 'rb'))

print(response)

