import datetime as dt
import smtplib
from email.mime.text import MIMEText
import random
import os
import pandas

os.chdir("/Users/chaeyunsim/Documents/100_days_of_python/day_32")

sendEmail = "myemail@naver.com"
password = "mypassword"
smtpName = "smtp.naver.com"

data = pandas.read_csv("./birthdays.csv")
new_dict = {(data_row['month'], data_row['day']):data_row for (index, data_row) in data.iterrows()}

now = dt.datetime.now()
if (now.month, now.day) in new_dict:
    birthday_person = new_dict[(now.month, now.day)]


name_to_send = birthday_person['name']
my_name = 'myname'

if now.month == 9 and now.day == 15:
    letter_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_path, 'r') as letter_file:
        lines = letter_file.read()
        change_recv_name = lines.split('[NAME]')
        after_name = lines.split('[NAME]')[1]
        change_send_name = after_name.split('Angela')

    text = change_recv_name[0] + name_to_send + change_send_name[0] + my_name
    msg = MIMEText(text)

    msg['Subject'] = "Happy Birthday!"
    msg['From'] = sendEmail
    msg['To'] = sendEmail

    connection = smtplib.SMTP(smtpName)
    connection.starttls()
    connection.login(sendEmail, password)
    connection.sendmail(sendEmail, sendEmail, msg.as_string())
    connection.close()
