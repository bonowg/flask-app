import sys

from flask_restful import Resource
from app.parse_input import ValueParser
from app.mod_user import UserModel
from werkzeug.security import generate_password_hash
from flask_jwt import jwt_required


class UserRegister(Resource):

    @staticmethod
    def post():
        new_user = ValueParser.parse_username_password().parse_args()

        if UserModel.find_by_username(new_user['username']):
            return {'message': 'User {0} \
                    already in DB'.format(new_user['username'])}

        new_user = UserModel(new_user['username'],
                             generate_password_hash(new_user['password']))
        new_user.save_to_db()

        return {'message': 'SUCCESS'}, 201


class UserEdit(Resource):

    @staticmethod
    @jwt_required()
    def put(name):
        updated_values = ValueParser.parse_username_password().parse_args()

        user = UserModel.find_by_username(name)

        if not user:
            return {'message': 'User name {0} \
                    does NOT exists'.format(name)}, 404

        user.username = updated_values['username']
        user.password = generate_password_hash(updated_values['password'])
        user.save_to_db()

        return {'message': 'SUCCESS'}, 201


if __name__ == '__main__':
    sys.exit()
