import json
import boto3
from botocore.exceptions import BotoCoreError, NoCredentialsError

# Initialize the S3 and Bedrock clients
s3 = boto3.client('s3')
bedrock = boto3.client('bedrock', region_name='us-east-1')

def lambda_handler(event, context):
    # Check if input event contains the 'query' key
    if 'query' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid input: missing query')
        }

    query = event['query']

    # Define the S3 bucket and object key
    bucket_name = 'foxwidthtest1'
    object_key = 'input/query.txt'

    try:
        # Upload the query to S3
        s3.put_object(Bucket=bucket_name, Key=object_key, Body=query)

        # Call Bedrock with the query
        response = bedrock.invoke_endpoint(
            EndpointName='your-bedrock-endpoint',
            ContentType='application/json',
            Body=json.dumps({'query': query})
        )

        # Read and parse the response from Bedrock
        bedrock_response = json.loads(response['Body'].read().decode('utf-8'))

        # Assuming Bedrock response has a 'result' key
        result = bedrock_response.get('result', 'No result found')

        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except (BotoCoreError, NoCredentialsError) as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error calling Bedrock or S3: {str(e)}')
        }