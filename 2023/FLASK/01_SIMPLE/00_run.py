from flask import flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hellow, world!"

@app.route("/anas")
def anas():
    return "Anas!"

@app.route("/html")
def more_html():
    return "<h1> Hellow, Buddy!</h1>"

app.run(debug=True) #host="0.0.0.0", port="8000"
