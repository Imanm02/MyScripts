import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import Messages
import win32com.client as win32



def mail2(src, dest, subject, plain_text, html):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = dest
    mail.Subject = subject
    mail.Body = plain_text
    mail.HTMLBody = html

    mail.Send()
