from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/me")
def me():
    names = ['a', 'e', 'i', 'o', 'u']
    return render_template("me.html", names=names)

@app.route("/add")
def add():
    return render_template("add.html")
