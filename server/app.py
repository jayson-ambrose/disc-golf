#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import DefaultBase, User, Player, Round, Tournament, Scorecard, Course, Hole

app.secret_key = "hello"

# Views go here!

class ClearSession(Resource):
    def get(self):
        session['user_id'] = None

        return {}, 204

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(users, 200)
    

class Login(Resource):

    def post(self):
        req_data = request.get_json()
        user = User.query.filter(User.username == req_data['username']).first()
        
        try:
            session['user_id'] = user.id
            print(session)
            return user.to_dict()
        
        except:
            return make_response( {'error': '404 user not found'}, 404)

api.add_resource(Users, '/users')
api.add_resource(Login, '/login')
api.add_resource(ClearSession, '/clear')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
