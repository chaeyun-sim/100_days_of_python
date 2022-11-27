from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

# @app.route("/")
# def home():
#     random_number = random.randint(1, 10)
#     year = datetime.date.today().year
#     name = 'Chaeyun Sim'
#     return render_template('./templates/index.html', num=random_number, current_year=year, your_name=name)


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
    image = 'img/'+str(index)+'.jpg'
    print(image)
    return render_template('post.html', post=requested, img_src=image)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
