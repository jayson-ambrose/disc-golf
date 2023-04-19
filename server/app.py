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

api.add_resource(Logout, '/logout')

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
        
api.add_resource(Login, '/login')

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
        
api.add_resource(Users, '/users')

class UserById(Resource):
    def get(self, id):
        res = User.query.filter(User.id == id).first()
        if not res:
            return make_response({'error': 'error 404 User not found.'}, 404)
        return make_response(res.to_dict(), 200)
    def delete(self, id):
        user = User.query.filter(User.id == id).first()
        if user.id == session.get('user_id'):
            db.session.delete(user)
            db.session.commit()
            return make_response('', 204)
        else:
            return make_response({'error': 'error 401 Unauthorized.'}, 401)
        
api.add_resource(UserById, '/users/<int:id>')
        
class Rounds(Resource):

    def get(self):
        round_list = [r.to_dict() for r in Round.query.all()]
        return make_response(round_list, 200)
    
    def post(self):
        req = request.get_json()
        print (req)
        r = Round(course_id=req['course'], tournament_id=req['tournament'])

        playerlist = []
        scorelist = []
        
        for player in req['players']:
            player = Player.query.filter(Player.name == player).first()
            if not player:
                player = Player(name=player.name, user_id=User.query.filter(User.id == session.get('user_id')).first())
                playerlist.append(player)
                new_score = player.addScorecard()
            
        for player in playerlist:
            new_score = Scorecard(player=player, round=r)
            scorelist.append(new_score)
        try:
            db.session.add_all([r, *playerlist, *scorelist])
            db.session.commit()
        except:
            db.session.rollback()
            return make_response({'error': 'error 400: Unable to create new game.'}, 400)
        return make_response({'round': r.to_dict(only=('id', 'date', 'course_id', 'tournament_id'))}, 201)

api.add_resource(Rounds, '/rounds')

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
    
api.add_resource(RoundById, '/rounds/<int:id>')

class ScorecardByRoundId(Resource):
    def get(self, id):
        score_list = Scorecard.query.filter(Scorecard.round_id == id).all()
        return make_response(list(map(lambda score: score.to_dict(rules=('-children',)), score_list)), 200)
    
    def patch(self, id):
        score_list = Scorecard.query.filter(Scorecard.round_id == id).all()
        req = request.get_json()
        for score in score_list:
            for player in req.players:
                if player.id == score.player_id:
                    score.set_score_from_hole(req.hole, player.score)
        db.session.commit()
        res = {'hole': req.hole,
                'players': list(map(lambda s: {'id': s.player_id, 'score': s.get_score_from_hole(req.hole)}))
            }
        return make_response(res, 200)

api.add_resource(ScorecardByRoundId,'/rounds/<int:id>/scorecards')\

# {'hole': int(),
#  'players': [
#     {'id': 1, 'score': 2},
#     {'id': 2, 'score': 4},
#     {'id': 3, 'score': 3}
#  ]}

class PlayerByRoundId(Resource):
    def get(self, id):
        player_list = Player.query.where(Player.rounds.any(Round.id == id))
        res = {'players': list(map(lambda p: {'id': p.id, 'name':p.name}, player_list))}
        return make_response(res, 200)
        
api.add_resource(PlayerByRoundId, '/rounds/<int:id>/players')


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
api.add_resource(ClearSession, '/clear')
api.add_resource(CheckSession, '/check_session')


if __name__ == '__main__':
    app.run(port=5555, debug=True)


