from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        text = request.form.get("text")
        number = request.form.get("number")
        return "your text:{}, your number: {}".format(text, number)

    return render_template("index.html")