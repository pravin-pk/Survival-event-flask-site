from flask import Flask, render_template, url_for, redirect, request, session
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true

app = Flask(__name__)
app.secret_key = "pk"

# Setting up a Database with SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] =  False

db = SQLAlchemy(app)

class Participants(db.Model):
    __tablename__ = "PARTICIPANTS"
    id_ = db.Column("id_", db.Integer, primary_key = true)
    teamName = db.Column("TEAMNAME", db.String(50))
    scores = db.Column("SCORES", db.Integer)

    def __init__(self, teamName, score):
        self.teamName = teamName
        self.scores = score

@app.route("/")
def login():
    session.clear()
    return render_template("login.html")

@app.route("/home", methods = ["GET", "POST"])
def home():
    session["teamName"] = request.form.get("teamName")
    print(session["teamName"])
    return render_template("homepage.html")

@app.route("/challenge1", methods = ["POST", "GET"])
def memoryGame():
    if request.method != 'POST':
        return redirect('/')
    img = ['c.svg','cpp.svg','csharp.svg','css.svg','go.svg','html.svg','java.svg','javascript.svg','php.svg','python.svg','ruby.svg','swift.svg','typescript.svg','haskell.svg''kotlin.svg','lua.svg']
    return render_template("mem.html", logos = img[:1])

@app.route("/challenge2")
def quiz():
    return render_template("quiz.html")


if __name__ == "__main__":
    app.run(debug=True)