"""CRUD operations."""

from model import db, User, Recipe, Favorite, connect_to_db


def create_user(email, password)
    """Create and return a new user."""

    user = User(email=email, password=password) 

    return user


def create_recipe(spoonacular_id, title)
    """Create and return a new recipe."""

    recipe = Recipe(spoonacular_id=spoonacular_id, title=title) 

    return recipe


def create_favorite(user_id, spoonacular_id)
    """Create and return a new recipe."""

    favorite = Favorite(user_id=user_id, spoonacular_id=spoonacular_id) 

    return favorite



if __name__ == '__main__':
    from server import app
    connect_to_db(app)