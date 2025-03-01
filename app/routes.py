from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Timur'}
    return render_template("index.html", user=user)


@app.route("/second")
def second():
    text = "Hello, World"
    return render_template("second.html", text=text)