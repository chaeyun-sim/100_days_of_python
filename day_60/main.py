from flask import Flask, render_template, request
import requests
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = 'send email'
YOUR_EMAIL = 'receive email'
MY_PASSWORD = 'mypassword'
TWILIO_SID = 'AC3f9782873573fdc17b5afd00b5372f21'
TWILIO_NUM = "+19014459477"
TWILIO_AUTH_TOKEN = "bbe34d00bb9bc7b3e9c13f3e9dc143fc"

app = Flask(__name__)


@app.route('/')
def home():
    url_blog = 'https://api.npoint.io/7c108a845f8298adff07'
    posts = requests.get(url_blog).json()
    return render_template('index.html', posts=posts)


@app.route("/<int:index>")
def post(index):
    index = int(index)
    requested = None
    url_blog = 'https://api.npoint.io/7c108a845f8298adff07'
    posts = requests.get(url_blog).json()
    for items in posts:
        if items['id'] == index:
            requested = items
    image = 'img/' + str(index) + '.jpg'
    print(image)
    return render_template('post.html', post=requested, img_src=image)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        article = f"Name: {request.form['username']}\nEmail: {request.form['email']}\nPhone Number: {request.form['phone']}\nMessage: {request.form['message']}"
        msg = MIMEText(article)

        msg['Subject'] = "New Message!"
        msg['From'] = MY_EMAIL
        msg['To'] = YOUR_EMAIL

        connection = smtplib.SMTP('smpt.mail.yahoo.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, YOUR_EMAIL, msg.as_string())
        connection.close()
        return render_template('contact.html', sent=True)
    else:
        return render_template('contact.html', sent=False)


if __name__ == "__main__":
    app.run(debug=True)
