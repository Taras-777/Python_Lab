from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://myuser:****@localhost:3306/studentdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, unique=True)
    brand = db.Column(db.String(10), unique=True)
    origin_country = db.Column(db.String(10), unique=True)
    category = db.Column(db.String(10), unique=True)
    producer = db.Column(db.String(10), unique=True)

    def __init__(self, price=0, brand="", origin_country="", category="", producer=""):
        self.price = price
        self.brand = brand
        self.origin_country = origin_country
        self.category = category
        self.producer = producer


class UserSchema(ma.Schema):
    class Meta:
        fields = ('price', 'brand', 'origin_country', 'category', 'producer')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route("/user", methods=["POST"])
def add_user():
    price = request.json['price']
    brand = request.json['brand']
    origin_country = request.json['origin_country']
    category = request.json['category']
    producer = request.json['producer']

    new_user = User(price, brand, origin_country, category, producer)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)


@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    if not result:
        abort(404)
    return users_schema.jsonify(result)


@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    price = request.json['price']
    brand = request.json['brand']
    origin_country = request.json['origin_country']
    category = request.json['category']
    producer = request.json['producer']

    user.price = price
    user.brand = brand
    user.origin_country = origin_country
    user.category = category
    user.producer = producer

    db.session.commit()
    return user_schema.jsonify(user)


@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
