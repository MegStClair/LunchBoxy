"""CRUD operations"""

from model import db, User, Recipe, Favorite, connect_to_db
import json
from random import choice 



######### USER CRUD #########

def create_user(email, password, name):
    """Create and return a new user."""

    user = User(email=email, password=password, name=name) 

    return user


def get_user_by_id(user_id):
    """Return user by user_id/primary key"""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return user by email"""

    return User.query.filter(User.email == email).first()


def get_user_name(name):

    return User.query.filter(User.name == name).first()



######### RECIPE CRUD #########

def create_recipe(tag, title, image, ingredients, instructions, tips):
    """Create and return a new recipe."""

    recipe = Recipe(tag=tag, 
                    title=title, 
                    image=image, 
                    ingredients=ingredients, 
                    instructions=instructions, 
                    tips=tips
    ) 

    return recipe


def get_recipes():
    """ Return all recipes """

    return Recipe.query.all()


def get_recipe_by_id(recipe_id):
    """ Return recipe by primary key """

    return Recipe.query.get(recipe_id)


def get_recipe_by_tag(tag):
    """ Return recipe by tag """

    return Recipe.query.get(tag)


def get_all_by_tag(tag):
    """ Return all recipes by tag """

    all_by_tag = Recipe.query.filter(Recipe.tag == tag).all()

    meals_list = []
    
    for recipe in all_by_tag:
        meal = {
            "recipe_id": recipe.recipe_id,
            "title": recipe.title, 
            "image": recipe.image, 
            "ingredients": recipe.ingredients, 
            "instructions": recipe.instructions,
            "tips": recipe.tips
            }
        meals_list.append(meal)

    # instead of returning list of object, 
    # will return list of dicts

    return meals_list


def get_random_by_tag(tag):
    """ Return random object by tag """

    food = Recipe.query.filter(Recipe.tag == tag).all()

    random_food = choice(food)

    return random_food


######### FAVORITES CRUD #########

def create_favorite(user_id, recipe_id):
    """Create and return a new favorite."""

    favorite = Favorite(user_id=user_id, recipe_id=recipe_id) 

    return favorite


def get_favorite(user_id, recipe_id):
    """ Return user's favorite by recipe id """

    return Favorite.query.get(user_id=user_id, recipe_id=recipe_id)


def get_user_favs_as_dict(user_id):
    """ Return all of user's favorite recipes """

    # get all of users favs 
    favorites = Favorite.query.filter_by(user_id = user_id).all()

    print("*"*20, "favorites: " , favorites)

    jsonifiable_favs = []

    for favorite in favorites:
        favorite = {
            "user_id": favorite.user_id,
            "favorite_id": favorite.favorite_id,
            "recipe": {
                    "recipe_id": favorite.recipe_id,
                    "title": favorite.recipe.title, 
                    "image": favorite.recipe.image, 
                    "ingredients": favorite.recipe.ingredients, 
                    "instructions": favorite.recipe.instructions,
                    "tips": favorite.recipe.tips
                    }
        }

        jsonifiable_favs.append(favorite)

    print("*"*20, "jsonifiable_favs: " , jsonifiable_favs)
     
    return jsonifiable_favs



if __name__ == '__main__':
    from server import app
    connect_to_db(app)