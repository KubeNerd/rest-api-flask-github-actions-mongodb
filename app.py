from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
from mongoengine import NotUniqueError
from datetime import datetime

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "db": "users",
    "host": "mongodb",
    "username": "admin",
    "password": "MinhaSenha123@Forte!!",
    "port": 27017,
}

api = Api(app)
db = MongoEngine(app)

user_parser = reqparse.RequestParser()
user_parser.add_argument('cpf', type=str, required=True, help="CPF is required")
user_parser.add_argument('email', type=str, required=True, help="Email is required")
user_parser.add_argument('first_name', type=str, required=True, help="First name is required")
user_parser.add_argument('last_name', type=str, required=True, help="Last name is required")
user_parser.add_argument('birth_date', type=str, required=True, help="Birth date is required")

class UserModel(db.Document):
    cpf = db.StringField(max_length=200, unique=True)
    email = db.StringField(max_length=200, required=True)
    first_name = db.StringField(max_length=200, required=True)
    last_name = db.StringField(max_length=200, required=True)
    birth_date = db.DateTimeField(required=True)

class User(Resource):
    def get(self, cpf: str):
        response = UserModel.objects(cpf=cpf).first()
        if response:
           return {
                "cpf": response.cpf,
                "email": response.email,
                "first_name": response.first_name,
                "last_name": response.last_name,
                "birth_date": response.birth_date.strftime('%Y-%m-%d')
            }, 200
        return {"message": "User no exists."}, 200
    
    def post(self):
        data = user_parser.parse_args()
        birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')
        user = UserModel(
            cpf=data['cpf'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            birth_date=birth_date
        )

        try:
            response = user.save()
            return {"message": f" User ID: {response.id} has been created" }, 201
        except NotUniqueError:
            return {"message":"CPF alredy exists in database"}

        

class Users(Resource):
    def get(self):
        return jsonify(UserModel.objects())

api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
