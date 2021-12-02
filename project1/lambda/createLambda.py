import boto3


ZIPNAME = "lambdaController.zip"

def aws_file():
    with open(ZIPNAME, 'rb') as file_data:
        bytes_content = file_data.read()
    return bytes_content


def lambda_creator(name):
    lambda_client = boto3.client('lambda')
    response = lambda_client.create_function(
        Code={
            'ZipFile': aws_file()
        },
        Description='Lambda Controller',
        FunctionName='lambdaController',
        Handler='lambda_function.lambda_handler',
        Publish=True,
        Role='arn:aws:iam::564393646252:role/LabRole',
        Runtime='python3.7',
    )
    return response

lambda_creator("lambdaController")