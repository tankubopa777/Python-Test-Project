# send email with python 
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "tankubopa77@gmail.com"
email_password = "mvprbytrglyqcvat"

# temp email
email_receiver = "fivix19598@prolug.com"

subject = "Never stop coding"
body = """
Try hard bro
"""

em = EmailMessage
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())