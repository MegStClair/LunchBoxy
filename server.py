"""Server for lunch planning app"""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, Favorite
import crud
from random import choice 
import json 

from jinja2 import StrictUndefined

import os
import requests

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """ View homepage """

    return render_template('homepage.html')



########### USER ROUTES ###########

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
        # Log in user by storing the user id in session
        session['user_id'] = user.user_id 
        flash("Logged In!")
        

    return redirect('/profile')


@app.route("/profile", methods=['GET'])
def show_profile():
    """ Display user's profile page """
    
    if 'user_id' in session:
        user_id = session['user_id']
        user = crud.get_user_by_id(user_id)
        return render_template("profile.html", name=user.name)

    else:
        flash("Please log in")
        return redirect ('/login')



########### LUNCH IDEA ROUTES ###########

@app.route("/lunch-idea")     
def show_lunch():
    """ Show lunch idea """

    return render_template('lunch-idea.html')


@app.route("/lunch-idea.json")     
def show_lunch_json():

    recipes = {
    "filling": crud.get_random_by_tag("filling"),
    "crunchy": crud.get_random_by_tag("crunchy"),
    "fresh": crud.get_random_by_tag("fresh"),
    "fresh2": crud.get_random_by_tag("fresh")
    }

    for tag, recipe in recipes.items():
        prop = {
            "title": recipe.title,
            "image": recipe.image, 
            "ingredients": recipe.ingredients, 
            "instructions": recipe.instructions,
            "tips": recipe.tips
        }
        recipes[tag]=prop

    return jsonify(recipes)



########### VIEW ALL ROUTES ###########

@app.route("/view-all")
def view_all():
    """ Show lunch idea """

    return render_template('view-all.html')


@app.route("/view-all.json")     
def view_all_json():

    all_recipes = crud.get_all_by_tag("filling")
    
    return jsonify(all_recipes)



########### FAVORITES ROUTES ###########

@app.route("/favorites")
def favorite_recipes():
    """ Display all of user's favorite recipes """

    # check user is logged in, redirect if not
    if 'user_id' in session:
        user_id = session['user_id']
        user = crud.get_user_by_id(user_id)
        return render_template('/favorites.html', name=user.name)
        
    else:
        flash("Please log in.")
        return redirect('/')
    

@app.route("/favorites.json")
def favorite_recipes_json():

    favorites = crud.get_user_favs_as_dict(session["user_id"])
    
    print(favorites)

    return jsonify(favorites)


    #  """
    # jsaonifiable_favs = [
    #     {"user_id": 
    #     "favorite_id":
    #     "recipe": {"title":..., "recipe_id":...}}
    # ]
    # """


# add to favorites:
#     fav_recipe = Favorite.query.filter_by(user_id=session["user_id"], recipe_id=recipe_id).first()

#     #  check if already in favs, add to favorites table if not 
#     if not fav_recipe:    
#         fav_recipe = 
#         db.session.add(fav_recipe)
#         db.session.commit()

#     result = {"message": "Your recipe saved.", "recipe_id": recipe_id}

#     return jsonify(result) 








# @app.route("/alternate-food")
# def change_food():

#     tag = request.args.get("tag")
#     exclude = request.args.get("exclude")

#     new_food = crud.get_random_tag(tag)


#     return render_template('lunch-idea.html', filling=new_food, crunchy=new_food, fresh=new_food)


# @app.route("/alternate-food.json")
# def change_food_json():

#     tag = request.args.get("tag")
#     exclude = request.args.get("exclude")

#     new_food = crud.get_random_tag(tag)

#     props = {
#         "title": new_food.title,
#         "image": new_food.image, 
#         "ingredients": new_food.ingredients, 
#         "instructions": new_food.instructions,
#         "tips": new_food.tips
#     }

#     return jsonify(props)









if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

