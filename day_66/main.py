from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy(app)


##Cafe TABLE Configuration
with app.app_context():
    class Cafe(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(250), unique=True, nullable=False)
        map_url = db.Column(db.String(500), nullable=False)
        img_url = db.Column(db.String(500), nullable=False)
        location = db.Column(db.String(250), nullable=False)
        seats = db.Column(db.String(250), nullable=False)
        has_toilet = db.Column(db.Boolean, nullable=False)
        has_wifi = db.Column(db.Boolean, nullable=False)
        has_sockets = db.Column(db.Boolean, nullable=False)
        can_take_calls = db.Column(db.Boolean, nullable=False)
        coffee_price = db.Column(db.String(250), nullable=True)

        def to_dict(self):
        #Method 1. 
            dictionary = {}
            # Loop through each column in the data record
            for column in self.__table__.columns:
                #Create a new dictionary entry;
                # where the key is the name of the column
                # and the value is the value of the column
                dictionary[column.name] = getattr(self, column.name)
            return dictionary
        
            # #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
            # return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    # db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

# ## HTTP GET - Read Record
@app.route('/random')
def random_cafe():
    if request.method == "GET":
        cafes = Cafe.query.all()
        random_cafe = random.choice(cafes)
        return jsonify(id=random_cafe.id,
                       name = random_cafe.name,
                       map_url = random_cafe.map_url,
                       location = random_cafe.location,
                       has_sockets = random_cafe.has_sockets,
                       has_toilet = random_cafe.has_toilet,
                       has_wifi = random_cafe.has_wifi,
                       can_take_calls=random_cafe.can_take_calls,
                       seats = random_cafe.seats,
                       coffee_price = random_cafe.coffee_price
                       )


@app.route('/all')
def all_cafe():
    if request.method == 'GET':
        all_cafes = db.session.query(Cafe).all()
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route('/search')
def search_cafe():
    if request.method == 'GET':
        searched_location = request.args.get("location")
        cafe = db.session.query(Cafe).filter_by(location=searched_location).all()
        if len(cafe) > 0:
            return jsonify(cafes=[item.to_dict() for item in cafe])
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
