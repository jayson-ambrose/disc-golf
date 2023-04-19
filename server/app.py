#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api
from models import DefaultBase, User, Player, Round, Tournament, Scorecard, Course, Hole

app.secret_key = "aggabadvffa"

# Views go here!

class Logout(Resource):
    def get(self):
        session['user_id'] = None
        return {}, 204
    
    def delete(self):
        session['user_id'] = None
        return {}, 204

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(users, 200)
    
    def post(self):
        req = request.get_json()

        if req['password'] != req['re_password']:
            return make_response({'error':'401: passwords do not match.'}, 401)
        
        u = User(username=req.get('username'), password=req.get('password'))
        try:
            db.session.add(u)
            db.session.commit()
            return make_response(u.to_dict(), 201)
        except IntegrityError:
            session.rollback()
            return make_response({'error': 'error 400: Username already taken!'}, 400)
        
class Rounds(Resource):
    def get(self):
        round_list = [r.to_dict() for r in Round.query.all()]
        return make_response(round_list, 200)
    def post(self):
        req = request.get_json()
        r = Round(course=req.course, tournament=req.tournament, date={req.date if req.date else db.func.current_date()})
        playerlist = []
        scorelist = []
        for player in req.players:
            player = Player.query.filter(Player.name == player.name).first()
            if not player:
                player = Player(name=player.name, user=session.user)
            playerlist.append(player)
        for player in playerlist:
            new_score = Scorecard(player=player, round=r)
            scorelist.append(new_score)
        try:
            db.session.add_all([r, playerlist, scorelist])
            db.session.commit()
        except:
            db.session.rollback()
            return make_response({'error': 'error 400: Unable to create new game.'}, 400)
        return make_response({'round': r.to_dict(only=('id', 'date', 'course_id', 'tournament_id'))}, 201)

class RoundById(Resource):
    def get(self, id):
        r = Round.query.filter(Round.id == id).first()
        if not r:
            return make_response( {'error': '404 Round not found'}, 404)
        return make_response(r.to_dict(), 200)
    
    def delete(self, id):
        r = Round.query.filter(Round.id == id).first()
        if not r:
            return make_response( {'error': '404 Round not found'}, 404)
        db.session.delete(r)
        db.session.commit()
        return make_response('', 204)
    
class ScorecardByRoundId(Resource):
    def get(self, id):
        score_list = Scorecard.query.filter(Scorecard.round_id == id).all()
        return make_response(list(map(lambda score: score.to_dict(rules=('-children',)), score_list)), 200)
    
    def patch(self, id):
        score_list = Scorecard.query.filter(Scorecard.round_id == id).all()



{'holeid': int(),
 'players': {
    'player1': {'id': 1, 'score': 2},
    'player2': {'id': 2, 'score': 4},
    'player3': {'id': 3, 'score': 3}
 }}

class PlayerByRoundId(Resource):
    def get(self, id):
        player_list = Player.rounds.query.filter.all()
        
class Login(Resource):

    def post(self):
        req_data = request.get_json()
        user = User.query.filter(User.username == req_data['username']).first()

        if user.auth(req_data['password']) == False:
            print ('wrong password')
        
        try:            
            session['user_id'] = user.id
            return make_response(user.to_dict(), 200)
        
        except:
            return make_response( {'error': '404 user not found'}, 404)
        
class CheckSession(Resource):    

    def get(self):
        print (session.get('user_id'))
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            return {'message': '401: Not Authorized'}, 401

api.add_resource(Users, '/users')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Rounds, '/rounds')
api.add_resource(RoundById, '/rounds/<int:id>')
api.add_resource(ScorecardByRoundId,'/rounds/<int:id>/scorecards')


if __name__ == '__main__':
    app.run(port=5555, debug=True)


