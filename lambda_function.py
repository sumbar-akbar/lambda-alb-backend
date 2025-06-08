import boto3
import botocore

def lambda_handler(event, context):
    client = boto3.client('s3')

    html = get_object(client)

    response = {
        'statusCode': 200,
        'statusDescription': '200 OK',
        'isBase64Encoded': False,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': html
    }

    return response

def get_object(client):
    response = client.get_object(
        Bucket='<s3_bucket>',
        Key='index.html'
    )

    body = response['Body'].read()
    return body