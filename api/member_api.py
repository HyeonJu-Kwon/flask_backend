from flask import request, Blueprint
from flask_restful import Resource, Api
from db import db

member_blueprint = Blueprint('member_api', __name__)
member_api = Api(member_blueprint)

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {"message": "Invalid data"}, 400

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return {"message": "Login Successful"}, 200
        else:
            return {"message": "Invalid credentials"}, 401

member_api.add_resource(Register, '/register')
member_api.add_resource(Login, '/login')
