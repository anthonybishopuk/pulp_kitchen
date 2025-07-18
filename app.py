import json
import smtplib
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/menu")
def menu():
    with open("static/data/menu.json") as f:
        menu_data = json.load(f)
    return render_template("menu.html", menu = menu_data)

if __name__ == "__main__":
    app.run(debug=True)