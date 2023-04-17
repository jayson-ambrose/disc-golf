from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!

class DefaultMixin(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

class User(DefaultMixin):
    __tablename__ = 'users'

    username = db.Column(db.String)
    password = db.Column(db.String)

    players = db.relationship('Player', backref='user')

class Player(DefaultMixin):
    __tablename__ = 'players'

    name = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    scorecards = db.relationship('Scorecard', backref='player')
    rounds = association_proxy('scorecards', 'round')

class Round(DefaultMixin):
    __tablename__ = 'rounds'

    par = db.Column(db.Integer)
    score = db.Column(db.Integer)
    date = db.Column(db.Date, server_default=db.func.current_date())
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'))

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    scorecards = db.relationship('Scorecard', backref='round')
    players = association_proxy('scorecards', 'player')

class Scorecard(DefaultMixin):
    __tablename__ = 'scorecards'
    
    round_type = db.Column(db.String)
    score_1 = db.Column(db.Integer, default=-1)
    score_2 = db.Column(db.Integer, default=-1)
    score_3 = db.Column(db.Integer, default=-1)
    score_4 = db.Column(db.Integer, default=-1)
    score_5 = db.Column(db.Integer, default=-1)
    score_6 = db.Column(db.Integer, default=-1)
    score_7 = db.Column(db.Integer, default=-1)
    score_8 = db.Column(db.Integer, default=-1)
    score_9 = db.Column(db.Integer, default=-1)
    score_10 = db.Column(db.Integer, default=-1)
    score_11 = db.Column(db.Integer, default=-1)
    score_12 = db.Column(db.Integer, default=-1)
    score_13 = db.Column(db.Integer, default=-1)
    score_14 = db.Column(db.Integer, default=-1)
    score_15 = db.Column(db.Integer, default=-1)
    score_16 = db.Column(db.Integer, default=-1)
    score_17 = db.Column(db.Integer, default=-1)
    score_18 = db.Column(db.Integer, default=-1)

    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    round_id = db.Column(db.Integer, db.ForeignKey('rounds.id'))
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'))

class Course(DefaultMixin):
    __tablename__ = 'courses'

    name = db.Column(db.String)

    holes = db.relationship('Hole', backref='course')
    
    def num_holes(self):
        return len(self.holes)

class Hole(DefaultMixin):
    __tablename__ = 'holes'

    par = db.Column(db.Integer)
    distance = db.Column(db.Integer)
    
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

class Tournament(DefaultMixin):
    __tablename__ = 'tournaments'

    event_name = db.Column(db.String)
    event_date = db.Column(db.Date)
    scorecard_id = db.Column(db.Integer, db.ForeignKey('scorecards.id'))

