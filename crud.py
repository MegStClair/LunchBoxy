"""CRUD operations."""

from model import db, User, Recipe, Favorite, connect_to_db

import json

from random import choice 



def create_user(email, password, name):
    """Create and return a new user."""

    user = User(email=email, password=password, name=name) 

    return user


def get_user_by_id(user_id):
    """Return user by user_id/primary key"""

    return User.query.get(user_id)

    # return a user by their user_id


def get_user_by_email(email):
    """Return user by email"""

    return User.query.filter(User.email == email).first()

    # return a user with that email if it exists; otherwise return None


def get_user_name(name):

    return User.query.filter(User.name == name).first()


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


def get_random_by_tag(tag):
    """ Return random object by tag """

    food = Recipe.query.filter(Recipe.tag == tag).all()

    random_food = choice(food)

    return random_food


def create_favorite(user_id, recipe_id):
    """Create and return a new favorite."""

    favorite = Favorite(user_id=user_id, recipe_id=recipe_id) 

    return favorite


# def remove_favorite(user_id, recipe_id):
#     """ Remove a favorite """

#    return 



if __name__ == '__main__':
    from server import app
    connect_to_db(app)