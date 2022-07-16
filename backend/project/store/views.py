
from itertools import product
from sys import prefix
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from project import db

# from decorators import login_required
from project.models import Product
from project.store.forms import ProductForm

bp = Blueprint("store", __name__, template_folder='templates', url_prefix='/store')

def getProducts():
    # cur = db.execute("SELECT * FROM posts;")
    # posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    # db.close()
    products = []
    products = Product.query.all()
    return products

@bp.route('/')
def show_products():
    products = getProducts()
    return render_template('show_products.html', products=products)


@bp.route('/product/add', methods=['GET', 'POST'])
def create_product():
    form = ProductForm(request.form)
    if form.validate_on_submit():
        product = Product( 
                        title=form.title.data,
                        description=form.description.data,
                        price=form.price.data
                        )
        
        db.session.add(product)

        try:
            db.session.commit()
            return redirect(url_for('home.home'))
        except Exception:
            db.session.rollback()
        finally:
            db.session.close()
    
    return render_template('create_product.html', form=form)
