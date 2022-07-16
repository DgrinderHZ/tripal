from sys import prefix
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from project.home.froms import PostForm
from project import db

# from decorators import login_required
from project.models import BlogPost

bp = Blueprint("home", __name__, template_folder='templates')


@bp.route('/', methods=["GET", "POST"])
def home():
    return render_template('index.html')


@bp.route('/welcome')
def welcome():
    return render_template('welcome.html')