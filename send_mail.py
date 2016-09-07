#!/usr/bin/python2
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText


def send_mail(to_addr, subject, text):
    from_addr = "jme.ct.de@gmail.com"
    google_username = "jme.ct.de@gmail.com"
    google_app_password = "xxxxxxxxxxxxxxx"
    message = MIMEText(text, 'plain', 'UTF-8')
    message['Subject'] = subject
    message['From'] = from_addr
    message['To'] = to_addr

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(google_username, google_app_password)
    server.sendmail(from_addr, to_addr, message.as_string())
    server.quit()


if __name__ == "__main__":
    send_mail("jme@ct.de", "Test", "Ein Test \nmit einfachen \nZeilenumbrüchen.\n So ist es.")