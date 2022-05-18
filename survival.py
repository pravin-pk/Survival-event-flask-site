from datetime import datetime
from flask import Flask, render_template, url_for, redirect, request, session
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import webbrowser
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
    time = db.Column("TIME", db.String(10))

    def __init__(self, teamName, score, time):
        self.teamName = teamName
        self.scores = score
        self.time = time

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session["teamName"] = request.form.get("teamName")
        print(session["teamName"])
        return redirect(url_for('memoryGame'))

    return render_template("login.html")

@app.route("/", methods = ["GET", "POST"])
def home():
    session.clear()
    return render_template("homepage.html")

@app.route("/challenge1", methods = ["POST", "GET"])
def memoryGame():
    # if request.method != 'POST':
    #     return redirect('/')
    img = ['c.svg','cpp.svg','csharp.svg','css.svg','go.svg','html.svg','java.svg','javascript.svg','php.svg','python.svg','ruby.svg','swift.svg','typescript.svg','haskell.svg''kotlin.svg','lua.svg']
    return render_template("mem.html", logos = img[:10])

@app.route("/challenge2", methods = ["GET", "POST"])
def quiz():
    if request.method != 'POST':
        return render_template("quiz.html")

    scores = request.form.get("scores")
    # print(scores)

    p = Participants(teamName = session["teamName"],
                    score = request.form.get('scores'),
                    time = datetime.now().strftime("%H:%M:%S"))
    db.session.add(p)
    db.session.commit()

    webbrowser.open_new_tab("https://www.hackerrank.com/survival-round-1")

    return redirect(url_for("links"))

@app.route("/links")
def links():
    return "<script> alert('Hello world'); </script>"

if __name__ == "__main__":
    db.create_all() # creates a db if it does not exists
    app.run(debug=True)