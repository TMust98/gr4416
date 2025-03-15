from app import app
from flask import render_template, flash, url_for, redirect
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Timur'}
    return render_template("index.html", user=user)


@app.route("/second")
def second():
    text = "Hello, World"
    return render_template("second.html", text=text)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.submit:
            flash(f'Запрос входа для аккаунта {form.username.data} с паролем {form.password.data}, запомнить - {form.remember_me.data}')
            return redirect(url_for('login'))
    return render_template('login.html', title="Вход", form=form)