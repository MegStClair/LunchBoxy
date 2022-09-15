"""Script to seed database."""

import os 
import json
from random import choice, randint
from datetime import datetime

import crud
from model import db, User, Recipe, Favorite, connect_to_db
import server

os.system("dropdb lunchdb")
os.system("createdb lunchdb")

connect_to_db(server.app)
db.create_all()


def example_data():
    aiden = User(email="aiden@email.com", password="password")
    sandwich = Recipe(title="sandwich")
    aiden_fav = Favorite(user=aiden, recipe=sandwich)
    db.session.add_all([aiden, sandwich])

    soup = Recipe(title="soup")
    db.session.add(soup)
    adrian = User(email="adrian@email.com", password="password")
    db.session.add(adrian)
    aiden_fav = Favorite(user=adrian, recipe=soup)
    db.session.add(aiden_fav)

    db.session.commit()

    
if __name__ == "__main__":
    example_data()
