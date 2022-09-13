"""Server for lunch planning app"""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """ View homepage """

    return render_template("homepage.html")


@app.route("/login")
def user_login():
    """ Show login form """

    return render_template("login.html")

# login route will pull info from login form


if __name__ == "__main__":
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

