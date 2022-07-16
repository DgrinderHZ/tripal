
from sys import prefix
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from project.home.froms import PostForm
from project import db

# from decorators import login_required
from project.models import BlogPost

bp = Blueprint("blog", __name__, template_folder='templates', url_prefix='/blog')

def getPosts():
    # cur = db.execute("SELECT * FROM posts;")
    # posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    # db.close()
    posts = []
    posts = BlogPost.query.all()
    return posts

@bp.route('/')
def show_posts():
    posts = getPosts()
    return render_template('show_posts.html', posts=posts)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm(request.form)
    if form.validate_on_submit():
        post = BlogPost( 
                        title=form.title.data,
                        description=form.description.data,
                        author_id=current_user.id
                        )
        
        db.session.add(post)

        try:
            db.session.commit()
            return redirect(url_for('home.home'))
        except Exception:
            db.session.rollback()
        finally:
            db.session.close()
    
    return render_template('create.html', form=form)
