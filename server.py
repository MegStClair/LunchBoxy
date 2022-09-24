"""Server for lunch planning app"""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
import crud
from random import choice 
import json 

from jinja2 import StrictUndefined

import os
import requests

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

LUNCH_DB = [
    {
        "tag": "filling",
        "title": "Veggie Sushi",
        "image": "https://cleanfoodcrush.com/wp-content/uploads/2018/09/Clean-Veggie-Sushi-lunchbox.jpg",
        "ingredients": "tortillas, hummus, bell peppers, green onions, carrots, avocado",
        "instructions": "1. Place tortillas on a cutting board and spread the hummus over them equally. 2. Top with bell peppers, green onions, carrots and avocado. 3. Roll the tortilla tightly around the vegetables, then slice crosswise into 1.5-inch slices.",
        "tips": "Null"  
    },
    {
        "tag": "filling",
        "title": "Actual Fruit Rollups",
        "image": "https://i.pinimg.com/564x/ad/29/46/ad2946ffcc3097105c50171a8d76ace4.jpg",
        "ingredients": "tortillas, fruit, nut butter",
        "instructions": "1. Spread nut butter over the entire surface of the tortilla. Go heavy! 2. Place the fruit in the middle of the tortilla and roll the tortilla around it. 3. Cut into slices.",
        "tips": "Null"  
    },
    {
        "tag": "filling",
        "title": "Ham & Cheese Pinwheels",
        "image": "https://sweetpeaskitchen.com/wp-content/uploads/2019/01/Ham-And-Cheese-Pin-Wheels-1.jpg",
        "ingredients": "tortillas, deli meat, cheese, cream cheese, lettuce",
        "instructions": "1. Spread a light layer of cream cheese (mayo is a good alternative!) on each tortilla. 2. Add layer of deli meat, lettuce, and any additional veggies you'd like. Top veggies with cheese. 3. Carefully roll the tortilla, using toothpicks to help keep everything in place. 4. Cut into slices.",
        "tips": "Serve with the toothpicks for grab-and-go ease and to keep everything in place."  
    },
    {
        "tag": "filling",
        "title": "Crossiant Sandwich",
        "image": "https://simplyhomecooked.com/wp-content/uploads/2022/06/croissant-sandwich-3.jpg",
        "ingredients": "crossiant, deli meat, cheese, lettuce, mayo",
        "instructions": "1. Slice open the crossiant and spread layer of mayo (or preferred condiment). 2. Fill with layers of deli meat, cheese, lettuce (or spinach!), and any additional veggies you'd like. 3. Close sandwich and slice in half.",
        "tips": "Try adding some microwavable bacon or avocado for extra goodness!"  
    },
    {
        "tag": "filling",
        "title": "Chicken Nugget Wrap",
        "image": "https://i.pinimg.com/564x/65/fa/28/65fa28c7b77cf1f855e6c74ca6948138.jpg",
        "ingredients": "tortilla, chicken nuggets, dressing, lettuce, shredded cheese",
        "instructions": "1. Spread light layer of ranch (we like ceaser too!) over tortilla. 2. Add lettuce, cooked nuggets, cheese, and any additonal veggies you'd like. 3. Wrap and cut in half for easy eating.",
        "tips": "Null"  
    },
    {
        "tag": "filling",
        "title": "Hard Boiled Eggs & Salami",
        "image": "https://www.andianne.com/wp-content/uploads/2021/07/bento-box-lunches-02.jpg.webp",
        "ingredients": "eggs, deli meat",
        "instructions": "1. Hard boil some eggs. 2. Roll up some deli meat (we recommend salami).",
        "tips": "Null"  
    },
    {
        "tag": "filling",
        "title": "DIY Lunchables",
        "image": "https://www.eatingonadime.com/wp-content/uploads/2016/08/homemade-lunchables-3.jpg.webp",
        "ingredients": "crackers, deli meat, cheese",
        "instructions": "1. Well, this one's pretty self-explanatory.",
        "tips": "Null"  
    },
    {
        "tag": "filling",
        "title": "Pesto Pasta",
        "image": "https://www.healthylifetrainer.com/wp-content/uploads/2021/03/Pesto-Pasta-With-Homemade-Pesto-Sauce-3.jpg",
        "ingredients": "pasta, pesto, parmesan cheese",
        "instructions": "1. Cook pasta according to package directions. 2. Coat in pesto (prepackaged is just fine). 3. Sprinkle parmesan cheese and mix.",
        "tips": "Add some crumbled microwave bacon for extra yums!"  
    },
    {
        "tag": "filling",
        "title": "Pizza Pasta",
        "image": "https://sofabfood.com/wp-content/uploads/2018/09/pasta_salad_-e1537402741222.jpg",
        "ingredients": "pasta, pepperoni, mozzarella cheese, parmesan cheese, italian dressing, catalina dressing, oregano",
        "instructions": "1. Start by cooking pasta according to package directions. 2. In a small bowl, combine the Italian dressing, Catalina dressing, and oregano. Set aside. 3. While the pasta is still cooking, prep the pepperoni, and cheese (we also recommend cherry tomatoes!). 4. Once the pasta is cooled, toss in all of the ingredients and mix well. Be sure that the pasta gets a generous coat of the grated parmesan cheese.",
        "tips": "This tastes great cold, so feel free to prep the night before!"  
    },
    {
        "tag": "crunchy",
        "title": "Crackers",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null"  
    },
    {
        "tag": "crunchy",
        "title": "Pretzels",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null"  
    },
    {
        "tag": "crunchy",
        "title": "Popcorn",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null"  
    },
    {
        "tag": "crunchy",
        "title": "Nuts",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null"  
    },
    {
        "tag": "crunchy",
        "title": "Tortilla Chips",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null" 
    },
    {
        "tag": "fresh",
        "title": "Cherry Tomatoes ",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null" 
    },
    {
        "tag": "fresh",
        "title": "Bell Peppers",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null" 
    }, 
    {
        "tag": "fresh",
        "title": "Grapes",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null" 
    },
    {
        "tag": "fresh",
        "title": "Strawberries",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null"  
    },
    {
        "tag": "fresh",
        "title": "Blueberries",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null" 
    },
    {
        "tag": "fresh",
        "title": "Mandarin Oranges",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null"  
    },
    {
        "tag": "fresh",
        "title": "Watermelon",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null" 
    },
    {
        "tag": "fresh",
        "title": "Pears",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null"  
    },
    {
        "tag": "fresh",
        "title": "Banana",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null" 
    },
    {
        "tag": "fresh",
        "title": "Carrots",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null"  
    }, 
    {
        "tag": "fresh",
        "title": "Cucumber",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null"  
    },
    {
        "tag": "fresh",
        "title": "Celery",
        "image": "",
        "ingredients": "Null",
        "instructions": "Null",
        "tips": "Null"  
    }
]


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


@app.route("/lunch-idea")     # NEED TO PRINT RANDOM OF EACH TAG!!!
def show_lunch():
    """ Show 1 lunch idea """

    recipes = LUNCH_DB

    results_dic = {}
    print('recipes is', recipes)

    for recipe in recipes:
        print("recipe is", recipe)

        # recipe = crud.get_recipe_by_tag("filling") ---programmingerror: "recipes.recipe_id does not exist"
        # print("filling is", recipe)
        

    # filling = crud.get_random_tag(tag=="filling")
    # crunchy = crud.get_random_tag(tag=="crunchy")
    # fresh = crud.get_random_tag(tag=="fresh")

    return render_template('lunch-idea.html', recipe=recipe)


# @app.route("/lunch-idea")
# def show_recipes():
#     """ Get recipes based on params """

#     recipes = LUNCH_DB


#     results_dic = {}
#     print('recipes is', recipes)

#     for recipe in recipes['results']:
#         print("recipe is", recipe)
#         recipe_id = recipe['id']
#         tag = recipe["tag"],
#         title = recipe["title"],
#         image = recipe["image"],
#         ingredients = recipe["ingredients"],
#         instructions = recipe["instructions"],
#         tips = recipe["tips"]
        

#     return render_template('search-results.html', recipes=recipes['results'])


# @app.route("/api/search-results", methods=['POST'])
# def show_results():

#     return jsonify(FAKE_SPOONACULAR)


# @app.route("/favorites")
# def saved_recipes():
#     """ Display user's favorite recipes """
#     favorites = Favorite. 
#  need to generate recipes first, creating searcch route first


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

