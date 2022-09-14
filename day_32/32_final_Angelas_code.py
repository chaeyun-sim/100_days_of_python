import datetime
import pandas
import os
import random
import smtplib

print(os.chdir("/Users/chaeyunsim/Documents/100_days_of_python/"))

my_email = "myemail@naver.com"
my_pw = 'mypassword'

today = datetime.datetime.now()
today_tup = (today.month, today.day)

data = pandas.read_csv("./day_32/birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']):data_row for (index, data_row) in data.iterrows()}

if today_tup in birthdays_dict:
    birthday_person = birthdays_dict[today_tup]
    file_path = f"./day_32/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.naver.com") as connection:
        connection.starttls()
        connection.login(my_email, my_pw)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person['email'], msg = f"Subject:Happy Birthday!\n\n{contents}")