import random
import datetime as dt
import smtplib
from email.mime.text import MIMEText


now = dt.datetime.now()
weekday = now.weekday()

sendEmail = "myemail@naver.com"
password= "password"
smtpName = "smtp.naver.com"

if weekday == 2: #wednesday (today is 2022/09/14)
    with open("./day_32/quotes.txt", 'r') as data_file:
        quote_lines = data_file.readlines()
        todays_random_quote = random.choice(quote_lines)

    text = todays_random_quote
    msg = MIMEText(text)

    msg['Subject'] = "Monday Motivation Quote!"
    msg['From'] = sendEmail
    msg['To'] = sendEmail

    connection = smtplib.SMTP(smtpName)
    connection.starttls()
    connection.login(sendEmail, password)
    connection.sendmail(sendEmail, sendEmail, msg.as_string())
    connection.close()