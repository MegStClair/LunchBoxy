"""Script to seed database."""

import os 
import json

import crud
from model import db, User, Recipe, Favorite, connect_to_db
from server import app 


def load_data():
    # Load lunch data from JSON file
    with open("data/lunch_db.json") as f:
        lunch_data = json.loads(f.read())

    # Create items, store them in list so we can use them to create meals
    lunches_in_db = []
    for recipe in lunch_data:
        tag, title, image, ingredients, instructions, tips = (
            recipe["tag"],
            recipe["title"],
            recipe["image"],
            recipe["ingredients"],
            recipe["instructions"],
            recipe["tips"],
        )

        db_lunch = crud.create_recipe(tag, title, image, ingredients, instructions, tips)
        lunches_in_db.append(db_lunch)

    db.session.add_all(lunches_in_db)
    db.session.commit()



def example_data():
    aiden = User(email="aiden@email.com", password="password", name="Aiden")
    sandwich = Recipe(title="sandwich")
    aiden_fav = Favorite(user=aiden, recipe=sandwich)
    db.session.add_all([aiden, sandwich])

    soup = Recipe(title="soup")
    db.session.add(soup)
    adrian = User(email="adrian@email.com", password="password", name="Adrian")
    db.session.add(adrian)
    aiden_fav = Favorite(user=adrian, recipe=soup)
    db.session.add(aiden_fav)

    db.session.commit()

    
if __name__ == "__main__":
    os.system("dropdb lunchdb")
    os.system("createdb lunchdb")

    connect_to_db(app)
    db.drop_all()
    db.create_all()
    load_data()
    example_data()
  
