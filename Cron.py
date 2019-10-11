import decimal
import os
from time import sleep
import datetime
import Settings
import json
import subprocess
from Email import Email
from SQSConnection import SQSConnection
from threading import Thread


def execute_test(script):
    print('Se ejecuta la prueba')
    txt = """
    describe('Prueba Cypress', function() {

    it('una Prueba', function() {
        cy.visit('https://losestudiantes.co');
        cy.contains('Cerrar').click();
    })

    });
    """

    with open(Settings.CYPRESS_PATH + "/cypress/integration/test.js", "w+") as file:
        file.write(txt)

    output = subprocess.call(['npm','run', 'test'])
    if output < 0:
        print('error en ejecución de prueba')

def process():
    try:
        sqs_connection = SQSConnection(Settings.AWS_QUEUE_URL_OUT)

        with sqs_connection:
            sqs_connection.receive()
            if sqs_connection.message is not '':
                message_body = sqs_connection.message.get('MessageBody')
                #Aqui va la conversion del json
                script = message_body
                sqs_connection.delete()
                execute_test(script)
                # if Settings.EMAIL_SEND == 'Y':
                #     Email.send_email(email=email, tittle=tittle, name=user_first_name)
                
                
    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        Thread(target=process).start()
        st = str(datetime.datetime.now())
        print(st + ' : alive')
        sleep(Settings.SLEEP_TIME)
