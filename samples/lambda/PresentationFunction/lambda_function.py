import time
import boto3
import redis
import json
import base64
from botocore.exceptions import ClientError


def get_secret():
    secret_name = "presentation/redis/password"
    region_name = "eu-central-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])

    return json.loads(secret)


def query():
    secret_dict = get_secret()
    secret = secret_dict.get('PresentationAuth')
    redis_client = redis.Redis(host='redis-host.example.com', port=6379, db=0, password=secret)
    return int(redis_client.get('transaction_count')), redis_client.get('important_data')


def send_to_queue(data):
    sqs = boto3.client('sqs', region_name='eu-central-1')
    sqs.send_message(
        QueueUrl='https://sqs.url/Queue',
        MessageBody=json.dumps(data)
    )


def main(event, context):
    start = time.time()
    count, data = query()
    end = time.time()
    json_data = json.loads(data)
    return_value = {
        "returncode": 0,
        "stdout": "lambda stdout",
        "stderr": "lambda stderr",
        "start_time": start,
        "end_time": end,
        "message": f'Transaction count: {count}.',
        "unit": "ms",
        "value": count,
        "metrics": {
            "transaction_count": count
        }
    }

    return_value.update(json_data)
    send_to_queue(return_value)
    return return_value


if __name__ == "__main__":
    main('', '')
