#!/usr/bin/python3
from email.message import EmailMessage
from threading import Thread
import ssl
import os
import smtplib

email_sender = os.getenv('EMAIL_SENDER')
email_password = os.getenv('EMAIL_PWD')

def send_async_email(subject, email, url_str):

    if subject == 'Confirm your email account':
        instruction = 'Click on link to verify email on meal magic'
    else:
        instruction = 'New password'
    body = """
    {}
    {}
    """.format(instruction, url_str)
    email_receiver = email
    em = EmailMessage()

    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    except smtplib.SMTPException:
        print('Error: could not send email')
    except smtplib.socket.error:
        print('Error: could not connect to server')
        


def send_email(subject, email, url_str):
    Thread(target=send_async_email, args=(subject, email, url_str)).start()
