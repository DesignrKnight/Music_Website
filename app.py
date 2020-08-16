from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os
from flask import url_for, redirect, render_template, request

app = Flask(__name__)
app.static_folder = 'static'


# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  artist = db.Column(db.String)
  album = db.Column(db.String)

  def __init__(self, name, description, artist, album):
    self.name = name
    self.description = description
    self.artist = artist
    self.album = album

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'artist', 'album')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
  name = request.json['name']
  description = request.json['description']
  artist = request.json['artist']
  album = request.json['album']

  new_product = Product(name, description, artist, album)
  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)
  

# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return render_template('playlist.html', title="Products" ,  result = result )


# Get Single Products
@app.route('/product/<id>', methods=['GET']) 
def get_product(id):
  product = Product.query.get(id)
  return render_template('song.html', title="Product(ID)" ,  product =product )
     
# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)

  name = request.json['name']
  description = request.json['description']
  artist = request.json['artist']
  album = request.json['album']

  product.name = name
  product.description = description
  product.artist = artist
  product.album = album

  db.session.commit()
  return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)

@app.route("/")
def home():
    return render_template("index.html")

# Run Server
if __name__ == '__main__':
  app.run(debug=True)