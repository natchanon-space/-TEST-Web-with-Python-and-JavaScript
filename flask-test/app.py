from flask import Flask, render_template, request

app = Flask(__name__)

names = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/me", methods=["POST"])
def me():
    name = request.form.get("name")
    names.append(name)
    return render_template("me.html", names=names)

@app.route("/add")
def add():
    return render_template("add.html")
