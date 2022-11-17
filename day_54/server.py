from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hello, World!'


@app.route("/bye")
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run()  # terminal에 작성한 flask run과 같다. # 기존 pycharm 버튼으로 실행된다.
