"""" Model classes """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """ A user. """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    

    favorites = db.relationship('Favorite', back_populates='user')

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}"


class Recipe(db.Model):
    """ A recipe. """

    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tag = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    ingredients = db.Column(db.String)
    instructions = db.Column(db.String)
    tips = db.Column(db.String)

    favorites = db.relationship('Favorite', back_populates='recipe')

    def __repr__(self):
        return f"<Recipe recipe_id={self.recipe_id} title={self.title}"


class Favorite(db.Model):
    """ A favorite. """ 

    __tablename__ = 'favorites'

    favorite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))

    user = db.relationship('User', back_populates='favorites')
    recipe = db.relationship('Recipe', back_populates='favorites')

    def __repr__(self):
        return f"<Favorite recipe_id={self.recipe_id} user_id={self.user_id}"



def connect_to_db(app, db_name="lunchdb"):
    """Connect database to Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Connecting instance of SQLAlchemy to database & Flask
    db.app = app
    db.init_app(app)

    print("Connected to database!")


if __name__ == "__main__":
    # from flask import Flask
    from server import app 

    # app = Flask(__name__)
    connect_to_db(app)

