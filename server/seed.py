#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

        user1 = User(username= 'beardman', password= 'password')
        db.session.add(user1)
        db.session.commit()
        
        # Seed code goes here!
