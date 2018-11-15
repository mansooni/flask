from flask import render_template, redirect, url_for, request
from app import app, photos, login_manager
from app.forms import RegisterForm, LoginForm, TweetForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Tweet
from flask_login import login_user, login_required, current_user, logout_user
from datetime import datetime


@app.route('/')
def index():
    form = LoginForm()
    return render_template('index.html', form=form)

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()

        if not user:
            return render_template('index.html', form=form, message='Login Failed!')

        if check_password_hash(user['password'], form.password.data):
            login_user(user, remember=form.remember.data)

            return redirect(url_for('profile'))
        return render_template('index.html', form=form, message='Login Failed!')

    return render_template('index.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', current_user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/timeline')
def timeline():
    form = TweetForm()
    return render_template('timeline.html', form=form)

@app.route('/post_tweet', methods=['POST'])
@login_required
def post_tweet():
    form = TweetForm()
    if form.validate():
        tweet = Tweet(user_id=current_user.id, text=form.text.data, date_created=datetime.now()).save()
        return redirect(url_for('timeline'))
    return 'Something went wrong'


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        image_filename =photos.save(form.image.data)
        image_url = photos.url(image_filename)

        new_user = User(name=form.name.data, username=form.username.data, image=image_url, password=generate_password_hash(form.password.data), join_date=datetime.now()).save()

        return redirect(url_for('profile'))

    return render_template('register.html', form=form)
