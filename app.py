from flask import Flask,jsonify
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
        "db": "users",
        "host": "mongodb",
        "username":"admin",
        "password":"MinhaSenha123@Forte!!",
        "port": 27017,
    }

api = Api(app)
db = MongoEngine(app)


class UserModel(db.Document):
    cpf = db.StringField(max_length=200, unique=True)
    email = db.StringField(max_length=200, required=True)
    first_name = db.StringField(max_length=200, required=True)
    last_name = db.StringField(max_length=200, required=True)
    birth_date = db.DateTimeField(required=True)



class User(Resource):
    def get(self, cpf):

        return {"message": "user 1"}
    
    def post(self):
        return {"message":"user 1"}

class Users(Resource):
    def get(self):
        return jsonify(UserModel.objects())

    
api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/users/<string:cpf>')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
