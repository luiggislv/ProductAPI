from product_api import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    description = db.Column(db.String(100), unique=False)
    category = db.Column(db.String(100), unique=False)
    price = db.Column(db.String(100), unique=False)
 
