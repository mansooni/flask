from flask import render_template, request, redirect
from app import app

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/post')
def post():
	return render_template('post.html')

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

	return '<h1>Title : {}, Subtitle : {}, Author : {}, Content : {}</h1>'.format(title, subtitle, author, content)
