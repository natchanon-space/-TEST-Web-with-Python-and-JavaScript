import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

# flask_socketio is a library that allows for websockets inside a Flask application. 
# This library allows for the web server and client to be emitting events to all other users, 
# while also listening for and receiving events being broadcasted by others.

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    emit("announce vote", {"selection": selection}, broadcast=True)

# submit vote is an event that will be broadcasted whenever a vote is submitted. The code for this will be in JavaScript.
