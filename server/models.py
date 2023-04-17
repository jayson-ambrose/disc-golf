from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

# Models go here!

class DefaultBase(db.Model, SerializerMixin):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Instance of {self.__class__.__name__}, ID {self.id}>'

class User(DefaultBase):
    __tablename__ = 'users'

    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String, nullable=False)

    players = db.relationship('Player', backref='user')

    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def auth(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

class Player(DefaultBase):
    __tablename__ = 'players'

    name = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    scorecards = db.relationship('Scorecard', backref='player')
    rounds = association_proxy('scorecards', 'round')

class Round(DefaultBase):
    __tablename__ = 'rounds'

    par = db.Column(db.Integer)
    score = db.Column(db.Integer)
    date = db.Column(db.Date, server_default=db.func.current_date())

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    scorecards = db.relationship('Scorecard', backref='round')
    players = association_proxy('scorecards', 'player')

class Scorecard(DefaultBase):
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

    tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'))
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    round_id = db.Column(db.Integer, db.ForeignKey('rounds.id'))

    def get_score_from_hole(self, hole_number):
        score_dict = {
            '1': self.score_1,
            '2': self.score_2,
            '3': self.score_3,
            '4': self.score_4,
            '5': self.score_5,
            '6': self.score_6,
            '7': self.score_7,
            '8': self.score_8,
            '9': self.score_9,
            '10': self.score_10,
            '11': self.score_11,
            '12': self.score_12,
            '13': self.score_13,
            '14': self.score_14,
            '15': self.score_15,
            '16': self.score_16,
            '17': self.score_17,
            '18': self.score_18
        }
        return score_dict[str(hole_number)]

class Course(DefaultBase):
    __tablename__ = 'courses'

    name = db.Column(db.String)

    holes = db.relationship('Hole', backref='course')
    rounds = db.relationship('Round', backref='course')
    
    def num_holes(self):
        return len(self.holes)

class Hole(DefaultBase):
    __tablename__ = 'holes'

    hole_number = db.Column(db.Integer)
    par = db.Column(db.Integer)
    distance = db.Column(db.Integer)
    
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    @validates('hole_number')
    def validate_number(self, key, hole_number):
        if type(hole_number) is not int:
            raise TypeError('Hole number must be an integer.')
        course_holes = self.course.holes
        course_hole_nums = map(lambda obj: obj.hole_number, course_holes)
        if hole_number in course_hole_nums:
            raise ValueError('This course already has a hole with this number.')
        elif hole_number < 1 or hole_number > 18:
            raise ValueError('Hole number must be between 1 and 18')
        else:
            return hole_number
        
    def average_score(self):
        scorecards = self.course.scorecards
        scores = list(map(lambda scorecard: scorecard.get_score_from_hole(self.hole_number), scorecards))
        return sum(scores)/len(scores)

class Tournament(DefaultBase):
    __tablename__ = 'tournaments'

    event_name = db.Column(db.String)
    event_date = db.Column(db.Date)
    
    scorecards = db.relationship('Scorecard', backref='tournament')
    rounds = association_proxy('scorecards', 'round')
    players = association_proxy('scorecards', 'player')

