import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText


sendmail = "cysh2635@naver.com"
recvmail = "cysh2635@naver.com"
password = "password"
server = "smtp.naver.com"


url = 'https://www.amazon.com/-/ko/dp/B07MN2NBTT/ref=sr_1_1?keywords=dyson+air+styler&qid=1664262459&qu=eyJxc2MiOiIzLjA2IiwicXNhIjoiMi4zMyIsInFzcCI6IjEuNTkifQ%3D%3D&sprefix=dyson+air+st%2Caps%2C252&sr=8-1'
header = {
    "Accept-Encoding" : "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)Version/15.6.1 Safari/605.1.15",
    "Accept-Language": "ko-KR,ko;q=0.9"
}
response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, 'lxml')

price = soup.find(name="span", class_="a-price").getText().split('$')[2]
name = soup.find(name='title').getText().split(":")[1]


if float(price) < 1000:
    text = f"\n{name}\nis now ${price}!\n\nBUY HERE: {url}"
    msg = MIMEText(text)
    msg['Subject'] = "Amazon Price Alert!"
    msg['From'] = sendmail
    msg['To'] = recvmail
    s = smtplib.SMTP(server)
    s.starttls()
    s.login(sendmail, password)
    s.sendmail(sendmail, recvmail, msg.as_string())
    s.close()

print("Sent!")