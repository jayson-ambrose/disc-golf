#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import datetime

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Tournament

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        User.query.delete()
        Tournament.query.delete()

        user1 = User(username= 'taco', password= 'password')
        dummy_tourney = Tournament(event_name='placeholder', event_date=datetime.date(1, 1, 1))

        db.session.add(user1)
        db.session.add(dummy_tourney)
        db.session.commit()
        
        # Seed code goes here!
