from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os
from flask import url_for, redirect, render_template, request, send_from_directory


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
  filename = db.Column(db.String)
  audio = db.Column(db.String)

  def __init__(self, name, description, artist, album, audio, filename):
    self.name = name
    self.description = description
    self.artist = artist
    self.album = album
    self.filename = filename
    self.audio = audio

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'artist', 'album','filename','audio')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


#Upload Song
@app.route('/uploadMusic')
def uploadMusic():
  return render_template("upload.html")

# Get Home
@app.route('/', methods=['GET'])
def get_home_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return render_template('index.html', title="Products" ,  result = result )

# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  
  return render_template('playlist.html', result = result )
   
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

@app.route("/upload", methods=["POST"])
def upload():
    print("Praisy:"+str(request.form))
    name = request.form["Sname"]
    artist = request.form["Aname"]
    album = request.form["name"]
    description = request.form["Dname"]

    target = os.path.join(basedir, "static/musicuploads/")
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print("ListAudio"+str(request.files.getlist("audiofile")))
    for upload in request.files.getlist("audiofile"):
        print("PraisyUpload1"+str(upload))
        #print("{} is the file name".format(upload.audio))
        audio = upload.filename
        ext = os.path.splitext(audio)[1]
        if (ext == ".mp3"):
            print("File supported moving on...")
        else:
            print("File not supported")
            return
        
        destination = "/".join([target, audio])
        print("Accept incoming file:", audio)
        print("Save it to:", destination)
        upload.save(destination)

  
    target = os.path.join(basedir, "static/imageuploads/")
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print("PraisyUpload1"+str(upload))
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        ext = os.path.splitext(filename)[1]
        if (ext == ".jpg") or (ext == ".png"):
            print("File supported moving on...")
        else:
            print("File not supported")
            return
            
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
        
    new_product = Product(name, description, artist, album, audio, filename)
    db.session.add(new_product)
    db.session.commit()

    return render_template("complete.html", image_name=filename , audio_name=audio)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
