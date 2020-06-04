from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socket = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socket.on("calculation")
def calculate(data):
    
    try:
        a = float(data["a"])
        b = float(data["b"])
        number = {"a": a, "b": b}
    except:
        emit("announce", {"success": False}, broadcast=True)

    calculate = {"plus": a+b, "minus": a-b, "mul": a*b}
    emit("announce", {"success": True, "calculate": calculate, "number": number}, broadcast=True)