from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/challenge1")
def memoryGame():
    img = ['c.svg','cpp.svg','csharp.svg','css.svg','go.svg','html.svg','java.svg','javascript.svg','php.svg','python.svg','ruby.svg','swift.svg','typescript.svg','haskell.svg''kotlin.svg','lua.svg']
    return render_template("mem.html", logos = img[:10])


if __name__ == "__main__":
    app.run(debug=True)