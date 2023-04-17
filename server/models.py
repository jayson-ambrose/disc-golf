from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!

class TimeStampMixin:
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

class User(db.Model, SerializerMixin, TimeStampMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    players = db.relationship('Player', backref='user')

class Player(db.Model, SerializerMixin, TimeStampMixin):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    date_of_birth = db.Column(db.String)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    scorecards = db.relationship('Scorecard', backref='player')
    rounds = association_proxy('scorecards', 'round')

class Round(db.Model, SerializerMixin, TimeStampMixin):
    __tablename__ = 'rounds'

    id = db.Column(db.Integer, primary_key = True)
    par = db.Column(db.Integer)
    score = db.Column(db.Integer)
    over_under = db.Column(db.Integer)

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    scorecards = db.relationship('Scorecard', backref='round')
    players = association_proxy('scorecards', 'player')

class Scorecard(db.Model, SerializerMixin, TimeStampMixin):
    __tablename__ = 'scorecards'
    
    id = db.Column(db.Integer, primary_key = True)
    round_type = db.Column(db.String)

    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    round_id = db.Column(db.Integer, db.ForeignKey('rounds.id'))

