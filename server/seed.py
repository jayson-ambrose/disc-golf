#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import datetime

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Tournament, Hole, Course, Player

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():

        print("Removing old data...")        
        User.query.delete()
        Tournament.query.delete()
        Hole.query.delete()
        Course.query.delete()
        Player.query.delete()
        
        print("Starting seed...")

        print('generating Users...')

        for u in range(15):
            user = User(username = fake.first_name(), password='password')
            db.session.add(user)
            db.session.commit()

        print('generating Courses...')

        for c in range (5):
            course = Course(name = fake.company(), city= fake.city(), state = fake.state())
            db.session.add(course)
            db.session.commit()

        print('generating Players...')

        for p in range (30):
            rand_user = randint(1, len(User.query.all()))
            player = Player(name = fake.first_name(), user_id= rand_user)
            
            db.session.add(player)
            db.session.commit()

        print('Generating holes and populating courses...')

        i = 0
        while i < len(Course.query.all()):

            i += 1
            hn = 0

            for h in range (18):

                hn += 1

                hd = randint(190, 1200)

                if hd <= 200:
                    hp = 2
                elif hd <= 510:
                    hp = 3
                elif hd <= 950:
                    hp = 4
                else:
                    hp = 5

                hole = Hole(hole_number = hn, par = hp, distance = hd, course_id = i)
                db.session.add(hole)
                db.session.commit()    

        db.session.commit()
        
        # Seed code goes here!
