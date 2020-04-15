#set up sqlalchemy lib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

#set up flask lib
from flask import Flask, render_template, request, redirect, url_for

#for time in notes
import datetime

#set database
DATABASE_URL = "postgresql://pun:pun@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))
#table users {user_id , username, password}
#table notes {ref_id, user_id, note, date}

app = Flask(__name__)

user = None

# index page
@app.route("/")
def index():
    return render_template("index.html")

# login, add note and logout section
@app.route("/login", methods=["POST"])
def login():
    
    username = request.form.get("username")
    password = request.form.get("password")
    
    # global for change value for user var. (global var.)
    global user
    user = db.execute("SELECT * FROM users WHERE username = :username AND password = :password", {"username":username, "password":password}).fetchone()
    
    if user == None:
        return "error, invalid username/password"
    
    return redirect(url_for('note', username=user.username))

@app.route("/note/<username>")
def note(username):
    
    if user != None :
        notes = db.execute("SELECT * FROM notes WHERE user_id = :user_id", {"user_id":user.user_id}).fetchall()
        return render_template("note.html", notes=notes, username=user.username)
    else:
        return "pls, login"

@app.route("/note/<username>/add")
def add(username):

    if user != None:
        return render_template('add.html', username=user.username)
    
    return "pls, login"

@app.route("/note/adding", methods=["POST"])
def adding():

    if user != None:
        note = request.form.get("note")
        date = datetime.datetime.now()
        db.execute("INSERT INTO notes (user_id, note, date) VALUES (:user_id, :note, :date)", {"user_id":user.user_id, "note":note, "date":date})
        db.commit()
        return redirect(url_for('note', username=user.username))

    return "pls, login"

@app.route("/logout")
def logout():

    global user
    user = None

    return redirect(url_for('index'))

# register section
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register/new_user", methods=["POST"])
def new_user():

    username = request.form.get("username")
    password = request.form.get("password")
    con_password = request.form.get("con_password")

    if password != con_password:
        return "invalid password/ password doesn't matched"
    
    check = db.execute("SELECT * FROM users WHERE username = :username AND password = :password", {"username":username, "password":password}).fetchone()

    if check != None:
        return "username already exist"

    db.execute("INSERT INTO users (username, password) VALUES (:username, :password)", {"username":username, "password":password})
    db.commit()

    return "success!!"