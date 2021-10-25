import requests
from digishop.settings import EMAIL_SENDER_NAME, EMAIL_SENDER_EMAIL, EMAIL_SENDER_PASSWORD
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendemail(name, email, subject, htmlcontent):
    
    message = MIMEMultipart()
    message['From'] = EMAIL_SENDER_NAME
    message['To'] = email
    message['Subject'] = subject   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(htmlcontent, 'html'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(EMAIL_SENDER_EMAIL, EMAIL_SENDER_PASSWORD) #login with mail_id and password
    text = message.as_string()
    session.sendmail(EMAIL_SENDER_EMAIL, email, text)
    session.quit()