
from sys import prefix
from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from project import db
from project.experience.forms import ExperienceForm

# from decorators import login_required
from project.models import Experience, Reservation

bp = Blueprint("experience", __name__, template_folder='templates', url_prefix='/experience')

def getExperiences():
    # cur = db.execute("SELECT * FROM posts;")
    # posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    # db.close()
    posts = []
    posts = Experience.query.all()
    return posts

@bp.route('/')
def show_experiences():
    posts = getExperiences()
    return render_template('show_experiences.html', experiences=posts)


@bp.route('/experience/add', methods=['GET', 'POST'])
@login_required
def create_experience():
    form = ExperienceForm(request.form)
    if form.validate_on_submit():
        post = Experience( 
                        title=form.title.data,
                        description=form.description.data,
                        price = form.price.data
                        )
        
        db.session.add(post)

        try:
            db.session.commit()
            return redirect(url_for('home.home'))
        except Exception:
            db.session.rollback()
        finally:
            db.session.close()
    
    return render_template('create_experience.html', form=form)


