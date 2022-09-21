"""Server for lunch planning app"""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

import os
import requests

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

API_KEY = os.environ['SPOONACULAR_KEY']

FAKE_SPOONACULAR = {
    "offset": 0,
    "number": 2,
    "results": [
        {
            "id": 716429,
            "title": "Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs",
            "image": "https://spoonacular.com/recipeImages/716429-312x231.jpg",
            "imageType": "jpg",
        },
        {
            "id": 715538,
            "title": "What to make for dinner tonight?? Bruschetta Style Pork & Pasta",
            "image": "https://spoonacular.com/recipeImages/715538-312x231.jpg",
            "imageType": "jpg",
        }
    ],
    "totalResults": 86
}


@app.route('/')
def homepage():
    """ View homepage """

    return render_template('homepage.html')


@app.route('/create-acct', methods=['POST'])
def create_user():
    """ Create a new user account """

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash("An account with that email already exists. Please try again.")
    else: 
        user = crud.create_user(email, password, name)
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
        

    return redirect('/profile')


@app.route("/profile")
def show_profile():
    """ Display user's profile page """
    if 'user_email' in session:
        email = session['user_email']
        user = crud.get_user_by_email(email)
        return render_template("profile.html", name=user.name)

    else:
        flash("User not logged in")
        return redirect ('/login')


@app.route("/search")
def search_recipes():
    """ Search for recipes """

    return render_template('search.html')


# @app.route("/search-results")
def show_recipes():
    """ Get recipes based on params """

    diet = request.args.get("diet")
    intolerances = request.args.get("intolerances")
    maxReadyTime = request.args.get("max-ready-time")
    exclude = request.args.get("exclude")

    
    endpoint= 'https://api.spoonacular.com/recipes/complexSearch'
    # payload = {
    #     'diet': diet,
    #     'intolerances': intolerances,
    #     'maxReadyTime': maxReadyTime,
    #     'excludeIngredients': exclude}

    # https://api.spoonacular.com/recipes/complexSearch/recipes/complexSearch?diet=vegetarian&intolerances=gluten&maxReadyTime=20&excludeIngredients=eggs

    # query_params = "?diet=" + str(diet) + "&intolerances=" + str(intolerances) + "&maxReadyTime=" + str(maxReadyTime) + "&excludeIngredients=" + str(exclude)
    # query = endpoint + query_params

    # response = requests.get(query)
    # # response = requests.get(endpoint, params=payload)
    # recipes = response.json()
    recipes = FAKE_SPOONACULAR # FIX ME!!!!!

    # if '_embedded' in data:
    #     results = data['_embedded']['results']
    # else:
    #     results = []

    results_dic = {}
    print('recipes is', recipes)

    for recipe in recipes['results']:
        print("recipe is", recipe)
        recipe_id = recipe['id']
        # details = get_recipe_by_id(recipe_id)
        # results_dic[results_dic] = details

    return render_template('search-results.html', recipes=recipes['results'])


@app.route("/api/search-results", methods=['POST'])
def show_results():

    return jsonify(FAKE_SPOONACULAR)


# @app.route("/favorites")
# def saved_recipes():
#     """ Display user's favorite recipes """
#     favorites = Favorite. 
#  need to generate recipes first, creating searcch route first


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

