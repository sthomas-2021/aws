# Code for testing AWS Secrets Manager
# If you get stuck, check the docs: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html
import logging
import json
import boto3

def get_secret():
    logger.debug('getting secret')
    smclient = boto3.client('secretsmanager')
    response = smclient.get_secret_value(
        SecretId='rlc-secret'
    )
    logger.debug(response['SecretString'])
    jsonObject = json.loads(response['SecretString'])
    secret = jsonObject['rlc-password']
    logger.debug(secret)
    return secret
    
def main(secret):
    print(f"Finally, our secret is: {secret}")

logging.basicConfig(
        level=logging.ERROR,
        format=f'%(asctime)s %(levelname)s %(message)s'
    )
logger = logging.getLogger()
    
# Run our code
# First we need to get our secret
our_secret = get_secret()
# Then we can pass it to our other function
main(our_secret)
