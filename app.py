from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# SQL:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mall.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), unique=True)

    # This will act like a List of Products objects attached to each Store.
    # The "author" refers to the author property in the BlogPost class.
    products = db.relationship('Product', back_populates='store')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # Create reference to the Store object, the "products" refers to the products properties in the User class
    store = db.relationship('Store', back_populates='products')

    product_name = db.Column(db.String(250), unique=True, nullable=False)
    product_description = db.Column(db.String(100), nullable=False)

# Creating Tables in DB:
# with app.app_context():
#     db.create_all()

# Creating a Store in DB:
# with app.app_context():
#     new_store = Store(store_name='Google')
#     db.session.add(new_store)
#     db.session.commit()

# with app.app_context():
#     store = Store.query.filter_by(store_name='Google').first()
#     new_post = Product(store=store, product_name='Gmail', product_description='Gmail is a great tool for emails.')
#     db.session.add(new_post)
#     db.session.commit()


# with app.app_context():
#     store = Store.query.filter_by(store_name='Google').first()
#     for product in store.products:
#         print(product.product_name)
#         print(product.product_description)




if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
