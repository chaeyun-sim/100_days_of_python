from flask import Flask, render_template, request, redirect, url_for
# import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

all_books = []

with app.app_context():
    class Books(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), unique=True, nullable=False)
        author = db.Column(db.String(50), nullable=False)
        rating = db.Column(db.Float, nullable=False)

        def __repr__(self):
            return f"<Book {self.title}>"

    db.create_all()

# db.create_all()

# db = sqlite3.connect("./day_63/book-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    # id = request.args.get('id')
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        # new_book = {
        #     "title": request.form["title"],
        #     "author": request.form["author"],
        #     "rating": request.form["rating"]
        # }
        # all_books.append(new_book)
        # print(all_books)
        new_book = Books(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit(book_id):
    print(request.method)
    if request.method == "POST":
        print(book_id)
        new_rating = request.form['rating']
        book = Books.query.filter_by(id=book_id).first()
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    book = Books.query.filter_by(id=book_id).first()
    print(book.title, book)
    return render_template('edit.html', book=book)


@app.route('/delete/<book_id>')
def delete(book_id):
    book = Books.query.filter_by(id=book_id).first()
    print(book)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

