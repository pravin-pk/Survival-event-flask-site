from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/memoryGame")
def memoryGame():
    pass


if __name__ == "__main__":
    app.run(debug=True)