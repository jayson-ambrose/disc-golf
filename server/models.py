from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    date_of_birth = db.Column(db.String)
    
    scorecards = db.relationship('Scorecard', backref='player')
    rounds = association_proxy('scorecards', 'round')

class Round(db.Model, SerializerMixin):
    __tablename__ = 'rounds'

    id = db.Column(db.Integer, primary_key = True)
    course_name = db.Column(db.String)
    par = db.Column(db.Integer)
    score = db.Column(db.Integer)
    over_under = db.Column(db.Integer)

    scorecards = db.relationship('Scorecard', backref='round')
    players = db.association_proxy('scorecards', 'player')

class Scorecard(db.Model, SerializerMixin):
    __tablename__ = 'scorecards'
    
    id = db.Column(db.Integer, primary_key = True)
    round_type = db.Column(db.String)

    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    round_id = db.Column(db.Integer, db.ForeignKey('rounds.id')

