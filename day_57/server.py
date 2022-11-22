from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = datetime.date.today().year
    name = 'Chaeyun Sim'
    return render_template('index.html', num=random_number, current_year=year, your_name=name)


@app.route("/guess/<name>")
def guess(name):
    url_gen = f"https://api.genderize.io?name={name}"
    gender = requests.get(url_gen).json()['gender']
    url_age = f"https://api.agify.io?name={name}"
    age = requests.get(url_age).json()['age']
    return render_template('guess.html', name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    url_blog = 'https://api.npoint.io/c790b4d5cab58020d391'
    all_posts = requests.get(url_blog).json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
