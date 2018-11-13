from flask import render_template
from app import app
from app.forms import RegisterForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        return '<h1>name:{}, username:{}, password:{}</h1>'.format(form.name.data, form.username.data,form.password.data)
    return render_template('register.html', form=form)
