from utils.db import db


# parent table
class Products(db.Model):
    id = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(100), nullable=True)
    #
    wishlists = db.relationship('Wishlist', backref='products', lazy=True)

# child table
class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String, db.ForeignKey('products.id'), nullable=True)
