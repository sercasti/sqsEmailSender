import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def consumer(event, context):
    for record in event['Records']:
        logger.info(f'Message body: {record["body"]}')
        logger.info(
            f'Message attribute: {record["messageAttributes"]["emailId"]["stringValue"]}'
        )

        userEmails = record["body"].split(",")
        message = "testeando os testes"
        emailId = record["messageAttributes"]["emailId"]["stringValue"]
        
        for userEmailAddress in (userEmails):
          ##hubspotClient.marketing.transactional.singleSendApi.sendEmail(...)
          logger.info("sent email to " + userEmailAddress)