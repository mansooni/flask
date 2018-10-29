from flask import render_template
from app import app
from app.forms import MyForm


@app.route('/', methods=['GET','POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        return render_template('result.html', email=form.email.data, password=form.password.data, textarea=form.textarea.data, radios=form.radios.data, selects=form.selects.data)
    return render_template('form.html', form=form)

