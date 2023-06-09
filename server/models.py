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

    serialize_rules = ('-created_at', '-updated_at')

    def __repr__(self):
        return f'<Instance of {self.__class__.__name__}, ID {self.id}>'

class User(DefaultBase):
    __tablename__ = 'users'

    username = db.Column(db.String, unique=True)
    _password = db.Column(db.String, nullable=False)

    players = db.relationship('Player', backref='user', cascade='all, delete')
    rounds = db.relationship('Round', backref='user', cascade='all, delete')

    serialize_rules = ('-_password', '-password', '-players','-created_at', '-updated_at', '-rounds')

    @hybrid_property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        self._password = password_hash

    def auth(self, password):
        return bcrypt.check_password_hash(self.password, password)

class Player(DefaultBase):
    __tablename__ = 'players'

    name = db.Column(db.String)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    scorecards = db.relationship('Scorecard', backref='player')
    rounds = association_proxy('scorecards', 'round')

    def newScorecard (self, round_id):
        scorecard = Scorecard(self.id, round_id)
        try:
            db.session.add(scorecard)
            db.session.commit()
            return(scorecard) 
        except: print("hello")


class Round(DefaultBase):
    __tablename__ = 'rounds'

    date = db.Column(db.Date, server_default=db.func.current_date())

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    scorecards = db.relationship('Scorecard', backref='round', cascade='all, delete-orphan')
    players = association_proxy('scorecards', 'player')

    serialize_rules = ('-created_at', '-updated_at', '-scorecards', '-players')

class Scorecard(DefaultBase):
    __tablename__ = 'scorecards'
    
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
    
    def set_score_from_hole(self, hole_number, new_score):
        score_dict = {
        '1': 'score_1',
        '2': 'score_2',
        '3': 'score_3',
        '4': 'score_4',
        '5': 'score_5',
        '6': 'score_6',
        '7': 'score_7',
        '8': 'score_8',
        '9': 'score_9',
        '10': 'score_10',
        '11': 'score_11',
        '12': 'score_12',
        '13': 'score_13',
        '14': 'score_14',
        '15': 'score_15',
        '16': 'score_16',
        '17': 'score_17',
        '18': 'score_18'
    }
        h = score_dict[str(hole_number)]
        setattr(self, h, new_score)

    def total_score(self):
        holes = range(1, 18)
        sum = 0
        for n in holes:
            if self.get_score_from_hole(n) != -1:
                sum += self.get_score_from_hole(n)
        return sum

class Course(DefaultBase):
    __tablename__ = 'courses'

    name = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)

    holes = db.relationship('Hole', backref='course', cascade='all, delete-orphan')
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
        # course_holes = self.course.holes
        # course_hole_nums = map(lambda obj: obj.hole_number, course_holes)
        # if hole_number in course_hole_nums:
        #     raise ValueError('This course already has a hole with this number.')
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
    
    rounds = db.relationship('Round', backref='tournament')
    scorecards = association_proxy('rounds', 'scorecard')
    players = association_proxy('scorecards', 'player')

