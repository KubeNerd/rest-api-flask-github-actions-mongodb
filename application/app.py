from flask import jsonify
from flask_restful import Resource, reqparse
from mongoengine import NotUniqueError
from datetime import datetime
from .model import UserModel


user_parser = reqparse.RequestParser()
user_parser.add_argument(
    'cpf',
    type=str,
    required=True,
    help="CPF is required"
)
user_parser.add_argument(
    'email',
    type=str,
    required=True,
    help="Email is required"
)
user_parser.add_argument(
    'first_name',
    type=str,
    required=True,
    help="First name is required"
)
user_parser.add_argument(
    'last_name',
    type=str,
    required=True,
    help="Last name is required"
)
user_parser.add_argument(
    'birth_date',
    type=str,
    required=True,
    help="Birth date is required"
)


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
        return {"message": "User does not exist."}, 404

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
            return {"message": f"User ID: {response.id} has been created"}, 201
        except NotUniqueError:
            return {"message": "CPF already exists in database"}, 400


class Users(Resource):
    def get(self):
        return jsonify(UserModel.objects())
