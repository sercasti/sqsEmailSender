import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def consumer(event, context):
    for record in event['Records']:
        logger.info(f'Message body: {record["body"]}')
        logger.info(
            f'Message attribute: {record["messageAttributes"]["AttributeName"]["stringValue"]}'
        )

        userEmails = record["body"]
        message = "testeando os testes"
        emailId = record["messageAttributes"]["AttributeName"]["stringValue"]
        
        for userEmailAddress in (userEmails):
          ##hubspotClient.marketing.transactional.singleSendApi.sendEmail(...)
          logger.info("sent email to " + userEmailAddress)