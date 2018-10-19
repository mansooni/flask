from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Blogpost
from datetime import datetime

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
	post = Blogpost.query.filter_by(id=post_id).one()
	date_posted = 'January 28, 2018'
	return render_template('post.html', post=post, date_posted=date_posted)

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/add')
def add():
	return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
	title = request.form['title']
	subtitle = request.form['subtitle']
	author = request.form['author']
	content = request.form['content']
	
	post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())
	db.session.add(post)
	db.session.commit()

	return redirect(url_for('index'))
