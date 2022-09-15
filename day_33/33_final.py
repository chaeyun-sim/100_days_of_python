import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import time

seoul_lat = 37.566536
seoul_long = 126.977966


def error_range_calculation():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])


    if seoul_lat-5 <= latitude <= seoul_lat+5 and seoul_long-5 <= longitude <= seoul_long+5:
        return True


def is_night():
    parameters = {"lat" : seoul_lat, "long" : seoul_long, "formatted" : 0}
    response = requests.get(url="http://api.sunrise-sunset.org/json?lat=37.566536&lng=126.977966", params=parameters)

    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise_result = sunrise.split('T')
    sunrise_time = sunrise_result[1].split(":")
    sunrise_hour = int(sunrise_time[0])

    sunset_result = sunset.split('T')
    sunset_time = sunset_result[1].split(":")
    sunset_hour = int(sunset_time[0])

    time_now = datetime.now().hour

    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True



sendEmail = 'myemail@gmail.com'
recvEmail = 'youremail.sim@yahoo.com'
password = 'mypassword'
smtpName = 'smtp.gmail.com'


while True: # if the iss is over your head
    time.sleep(5)
    if error_range_calculation() and is_night():
    # if datetime.now().hour == 23 and datetime.now().minute == 7:
        text = "The ISS is above you in the sky."
        msg = MIMEText(text)

        msg['Subject'] = "🌟🌟🌟 Look up the stars now! 🌟🌟🌟"
        msg['From'] = sendEmail
        msg['To'] = recvEmail

        connection = smtplib.SMTP(smtpName)
        connection.starttls()
        connection.login(sendEmail, password)
        connection.sendmail(sendEmail, recvEmail, msg.as_string())
        connection.close()