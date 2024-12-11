from flask import Flask, render_template, request, redirect
from utils.db import db
from models.ecommerce import *
import uuid


flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'


@flask_app.route('/')
def index():
    products = Products.query.all()
    return render_template('index.html', products=products)


@flask_app.route('/about')
def about():
    return render_template('about.html')

@flask_app.route('/groceries')
def groceries():
    products = Products.query.all()
    return render_template('groceries.html', products=products)


@flask_app.route('/mobiles')
def mobiles():
    products = Products.query.all()
    return render_template('mobiles.html', products=products)

@flask_app.route('/fashions')
def fashions():
    products = Products.query.all()
    return render_template('fashions.html', products=products)

@flask_app.route('/home-furniture')
def home_furniture():
    products = Products.query.all()
    return render_template('home_furniture.html', products=products)

@flask_app.route('/electronics')
def electronics():
    products = Products.query.all()
    return render_template('electronics.html', products=products)

@flask_app.route('/appliences')
def appliences():
    products = Products.query.all()
    return render_template('appliences.html', products=products)

@flask_app.route('/add-product')
def add_product():
    return render_template('add_product.html')

@flask_app.route('/cart')
def cart():
    return render_template('cart.html')

@flask_app.route('/wish-list')
def wish_list():
    wish_list = Wishlist.query.all()
    return render_template('wish_list.html', wish_list=wish_list)

@flask_app.route('/add-to-wishlist', methods=['POST'])
def add_to_wishlist():
    return "i will add to wishlist"


@flask_app.route('/update/<int:id>', methods=['POST'])
def update(id):
    print(id)
    return render_template('update.html')



db.init_app(flask_app)


with flask_app.app_context():
    db.create_all()


@flask_app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    id = str(uuid.uuid4())
    product_name = form_data.get('product_name')
    price = form_data.get('price')
    description = form_data.get('description')
    category = form_data.get('category')
    size = form_data.get('size')
    product = Products(
        id=id,
        name=product_name,
        price=price,
        description=description,
        category=category,
        size=size)
    db.session.add(product)
    db.session.commit()
    print("sumitted successfully")
    return redirect('/add-product')


if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=8005,
        debug=True
    )