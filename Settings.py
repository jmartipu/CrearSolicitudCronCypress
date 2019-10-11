import os

MEDIA_DIR = '/home/ec2-user/apps/Cron/'
CYPRESS_PATH = os.environ.get('CYPRESS_PATH')
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_SMTP_HOST = os.environ.get('EMAIL_SMTP_HOST')
EMAIL_SMTP_PORT = os.environ.get('EMAIL_SMTP_PORT')
AWS_ACCESS_KEY_ID_SQS = os.environ.get('AWS_ACCESS_KEY_ID_SQS')
AWS_SECRET_ACCESS_KEY_SQS = os.environ.get('AWS_SECRET_ACCESS_KEY_SQS')
AWS_REGION_SQS = os.environ.get('AWS_REGION_SQS')
AWS_QUEUE_URL_IN = os.environ.get('AWS_QUEUE_URL_IN')
AWS_QUEUE_URL_OUT = os.environ.get('AWS_QUEUE_URL_OUT')
EMAIL_SEND = 'Y'
SLEEP_TIME = 5
