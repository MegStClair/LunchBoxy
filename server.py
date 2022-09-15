"""Server for lunch planning app"""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """ View homepage """

    return render_template('homepage.html')


@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user account"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash("An account with that email already exists. Please try again.")
    else: 
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
    
    return redirect('/')


@app.route("/login", methods=['POST'])
def user_login():
    """ Show login form
    
    Pull data from login form """

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user email in session
        session['user_email'] = user.email 
        flash("Logged In!")
        # flash(F"Welcome back, {user.email}!") # save user by primary key, greet user by name??

    return redirect('/profile')


@app.route("/profile")
def show_profile(user_id):
    """Display user's profile page"""

    user = crud.get_user_by_id(user_id)

    return render_template("user-profile.html", user=user)




if __name__ == "__main__":
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

