from flask_wtf import form
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import RegisterphonenumberForm
#from app.models import User, Post
#from flask_login import login_required, login_user, logout_user, current_user

@app.route('/')
#@login_required
def index():
#    all_posts = Post.query.all()
    return render_template('index.html', form=form)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         # Grab data from our submitted form
#         username = form.username.data
#         email = form.email.data
#         password = form.password.data
#         print(username, email, password)
#         # Create new instance of User
#         new_user = User(username, email, password)

#         # Add new_user to our database
#         db.session.add(new_user)
#         db.session.commit()

#         # Once new_user is added to db, flash success message
#         flash(f'Thank you for signing up {new_user.username}!', 'danger')

#         # Redirect user back to home page
#         return redirect(url_for('index'))

        
#     return render_template('register.html', title='Register for CT Blog', form=form)


# @app.route('/createpost', methods=['GET', 'POST'])
# @login_required
# def createpost():
#     form = CreatePostForm()
#     if form.validate_on_submit():
#         # Grab data from the form
#         title = form.title.data
#         body = form.body.data
#         print(title, body, current_user.id)

#         # Create new instance of Post from form data
#         new_post = Post(title, body, current_user.id)

#         # Add new_post to database
#         db.session.add(new_post)
#         db.session.commit()

#         # Flash message that user successfully created post
#         flash(f'The post {new_post.title} has been created!', 'success')

#         return redirect(url_for('index'))

#     return render_template('createpost.html', form=form)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data
#         user = User.query.filter_by(username=username).first()

#         if user.check_password(password):
#             print("Hello")

#         if user is None or user.check_password(password):
#             flash('wrong', 'danger')
#             return redirect(url_for('login'))

#         login_user(user)
#         flash('You have logged in', 'success')
#         return redirect(url_for('index'))            

#     return render_template('login.html', form=form)

# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     flash('you have logged out', 'primary')
#     return redirect('index')