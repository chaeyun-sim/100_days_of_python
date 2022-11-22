from flask import Flask, render_template
import requests


app = Flask(__name__)
url = 'https://api.npoint.io/c790b4d5cab58020d391'
posts = requests.get(url).json()


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:index>')
def blog(index):
    wanted_post = None
    for post in posts:
        if post['id'] == int(index):
            wanted_post = post
    return render_template("post.html", post=wanted_post)


if __name__ == "__main__":
    app.run(debug=True)
