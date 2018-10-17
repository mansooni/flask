from tinydb import TinyDB, Query
from flask import Flask, render_template, url_for, redirect, request, g, flash
import sys

app = Flask(__name__)
app.secret_key = 'todolist'

db = TinyDB('todo.json')
todo = Query()

a = list(db.all())
user = a[-1]['id'] + 1

################### Firstpage ##############
@app.route('/')
def index():
	todolist = db.search(todo.id == user)
	print("now user = %d"%user,file=sys.stderr)
	return render_template('index.html', todolist=todolist)


################ add list ####################
@app.route('/add',methods=['POST'])
def add():
	db.insert({'id' : user, 'content' : request.form['todoitem']})
	return redirect(url_for('index'))

################# update id ########################
@app.route('/create', methods=['POST'])
def create():
	global user
	url = "https://127.0.0.1:5000/%d"%user
	user += 1
	print("create user = %d"%user,file=sys.stderr)
	print("url = " + url, file=sys.stderr)
	flash('Your url is '+url)
	return redirect(url_for('index'))

############# mytodo list ##########################
@app.route('/mytodolist/<int:user>',methods=['GET','POST'])
def todolist(user):
	todolist = db.search(todo.id==user)
	return render_template('index.html', todolist=todolist)

if __name__=="__main__":
	app.run(debug=True)
