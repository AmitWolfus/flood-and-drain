import smtplib
import os

SMTP_SERVER = 'smtp.gmail.com'  #Email Server (don't change!)
SMTP_PORT = 587  #Server Port (don't change!)


class Emailer:
  def sendmail(self, recipient, subject, content):
    gmail_username = os.environ.get('EMAIL_ADDRESS')
    gmail_password = os.environ.get('EMAIL_PASSWORD')
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
  sender.sendmail(os.environ.get('EMAIL_RECIPIENT'), subject, text)