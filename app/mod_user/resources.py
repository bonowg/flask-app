import sys

from flask_jwt import jwt_required
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from app.mod_user import UserModel
from app.parse_input import ValueParser


class UserRegister(Resource):

    @staticmethod
    def post():
        new_user = ValueParser.parse_all_for_user().parse_args()

        if UserModel.find_by_username(new_user['username']):
            return {'message': 'User {0} \
                    already in DB'.format(new_user['username'])}

        new_user = UserModel(username=new_user['username'],
                             email=new_user['email'],
                             password=generate_password_hash(new_user['password']))
        new_user.save_to_db()

        return {'message': 'SUCCESS'}, 201


class UserEdit(Resource):

    @staticmethod
    @jwt_required()
    def put(name):
        updated_values = ValueParser.parse_all_for_user().parse_args()

        user = UserModel.find_by_username(name)

        if not user:
            return {'message': 'User name {0} \
                    does NOT exists'.format(name)}, 404
        elif UserModel.find_by_email(updated_values['email']):
            return {'message': 'email  {0} \
                    already exists'.format(updated_values['email'])}, 403

        user.username = updated_values['username']
        user.email = updated_values['email']
        user.password = generate_password_hash(updated_values['password'])
        user.save_to_db()

        return {'message': 'SUCCESS'}, 201


if __name__ == '__main__':
    sys.exit()
