import smtplib
import ssl
from email.message import EmailMessage
from django.conf import settings
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Email:
    def send_otp_to_email(request, signup_email):
        load_dotenv(find_dotenv())

        email_sender = getattr(settings, "EMAIL_HOST_USER", None)
        email_password = os.environ['EMAIL_HOST_PASSWORD']
        print(email_sender, email_password)
        email_receiver = signup_email
        subject = 'OTP!'
        body = f"""
            {request.session.get('otp')}
        """
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())