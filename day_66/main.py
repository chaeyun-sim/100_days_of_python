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
        has_toilet = db.Column(db.String(50), nullable=False)
        has_wifi = db.Column(db.String(50), nullable=False)
        has_sockets = db.Column(db.String(50), nullable=False)
        can_take_calls = db.Column(db.String(50), nullable=False)
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
@app.route("/add", methods=["GET", "POST"])
def post_new_cafe():
    if request.method == 'POST':
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=["GET", "PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).filter_by(id=cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


## HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    if request.method == 'DELETE':
        api_key = request.args.get("api-key")
        if api_key == "TopSecretAPIKey":
            cafe = db.session.query(Cafe).filter_by(id=cafe_id)
            if cafe:
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
            else:
                return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."})




if __name__ == '__main__':
    app.run(debug=True)
