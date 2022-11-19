from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://www.humanesociety.org/sites/default/files/styles/1441x612/public/2022-07/kitten-playing' \
           '-575035.jpg?h=b1b36da8&itok=a0MQL3IM" width=200></img>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200></img>'


@app.route("/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


@app.route("/bye")
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)  # terminal에 작성한 flask run과 같음. # 기존 pycharm 버튼으로 실행된다.
