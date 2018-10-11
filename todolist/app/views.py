from flask import Flask, render_template, url_for, request, redirect
from app.models import TodoList
from app import app,db
	
@app.route('/')
def index():
	todo = TodoList.query.filter_by(chk=False).all()
	return render_template('index.html', todo=todo)


@app.route('/add', methods=['POST'])
def add():
	todo = TodoList(content = request.form['todoitem'], chk = False)
	db.session.add(todo)
	db.session.commit()
	return redirect(url_for('index'))

@app.route('/update/<int:id>',methods=['POST'])
def update(id):
	todo = TodoList.query.get(id)
	todo.chk = True
	db.session.commit()
	return redirect(url_for('index'))
