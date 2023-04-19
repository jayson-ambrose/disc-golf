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


if __name__ == '__main__':
    app.run(port=5555, debug=True)
