import json
import boto3

CallingVariable= boto3.client('dynamodb')

def lambda_handler(event, context):
  #data = CallingVariable.scan(
   # TableName='Demo'           #can be used for scanning purpose
  #)
  data = CallingVariable.get_item(
    TableName='Demo',
    Key={
        "Name": {
          'S': 'Jay'
        }
    }
  )

  response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response