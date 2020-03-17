import smtplib
import os

SMTP_SERVER = 'smtp.gmail.com'  #Email Server (don't change!)
SMTP_PORT = 587  #Server Port (don't change!)

GMAIL_USERNAME = os.environ.get('EMAIL_ADDRESS')
GMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
RECIPIENT = os.environ.get('EMAIL_RECIPIENT')


class Emailer:
  def sendmail(self, recipient, subject, content):

    #Create Headers
    headers = [
        "From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
        "MIME-Version: 1.0", "Content-Type: text/html"
    ]
    headers = "\r\n".join(headers)

    #Connect to Gmail Server
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()

    #Login to Gmail
    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    #Send Email & Exit
    session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
    session.quit()


def notify(subject, text):
  sender = Emailer()
  sender.sendmail(RECIPIENT, subject, text)