import smtplib
import os
import json

SMTP_SERVER = 'smtp.gmail.com'  #Email Server (don't change!)
SMTP_PORT = 587  #Server Port (don't change!)

with open(os.path.expanduser('~/env'), 'r') as env_file:
  env = json.loads(env_file.read())


class Emailer:
  def sendmail(self, recipient, subject, content):
    gmail_username = env.get('EMAIL_ADDRESS')
    gmail_password = env.get('EMAIL_PASSWORD')
    #Create Headers
    headers = [
        "From: " + gmail_username, "Subject: " + subject, "To: " + recipient,
        "MIME-Version: 1.0", "Content-Type: text/html"
    ]
    headers = "\r\n".join(headers)

    #Connect to Gmail Server
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()

    #Login to Gmail
    session.login(gmail_username, gmail_password)

    #Send Email & Exit
    session.sendmail(gmail_username, recipient, headers + "\r\n\r\n" + content)
    session.quit()


def notify(subject, text):
  sender = Emailer()
  sender.sendmail(env.get('EMAIL_RECIPIENT'), subject, text)