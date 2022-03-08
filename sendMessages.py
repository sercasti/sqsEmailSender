import os
import boto3
import json
import random
import string
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

SQS_CLIENT = boto3.client('sqs')
QUEUE_URL = os.getenv('SQS_URL')

def btwob(idList: str, idOffset:int):
  return contacts[idOffset:500]

def producer(event, context):
  currentOffset = 0
  areThereMoreContacts = True
  while areThereMoreContacts:
    emailAddresses = btwob('3627', currentOffset)
    if len(emailAddresses) < 1:
       areThereMoreContacts = False
       logger.info("pushed up to " + str(currentOffset) + " SQS messaged on " + QUEUE_URL)
    else:
      currentOffset = currentOffset + 500
      SQS_CLIENT.send_message(
          QueueUrl=QUEUE_URL,
          MessageBody=','.join(emailAddresses),
          MessageAttributes= {
              'emailId': {
                  'StringValue': '67054744499',
                  'DataType': 'String'
              }
          }
      )  
  return {'statusCode': 200, 'body': json.dumps({'message': "OK"})}


### Dummy values generation
contacts = []
for _ in range(10000):
  contacts.append(''.join(random.choice(string.ascii_letters) for _ in range(7))+"@gmail.com")