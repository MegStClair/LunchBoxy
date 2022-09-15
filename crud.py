"""CRUD operations."""

from model import db, User, Recipe, Favorite, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password) 

    return user


def get_user(user_id):
    """Return user by user_id"""

    return User.query.get(user_id)

    # return a user by their user_id
    

def get_user_by_email(email):
    """Return user by email"""

    return User.query.filter(User.email == email).first()

    # return a user with that email if it exists; otherwise return None


def create_recipe(spoonacular_id, title):
    """Create and return a new recipe."""

    recipe = Recipe(spoonacular_id=spoonacular_id, title=title) 

    return recipe


def create_favorite(user_id, spoonacular_id):
    """Create and return a new recipe."""

    favorite = Favorite(user_id=user_id, spoonacular_id=spoonacular_id) 

    return favorite



if __name__ == '__main__':
    from server import app
    connect_to_db(app)