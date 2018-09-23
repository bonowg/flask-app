import sys

from flask_jwt import jwt_required
from flask_restful import Resource

from app.mod_store import StoreModel


class Store(Resource):

    @staticmethod
    @jwt_required()
    def get(name):
        store = StoreModel.find_by_name(name)

        if not store:
            return {'message': 'Store name: {0} NOT found'.format(name)}

        return store.json()

    @staticmethod
    @jwt_required()
    def post(name):
        if StoreModel.find_by_name(name):
            return {'message': 'Store name: {0} \
                    already in DB'.format(name)}, 400

        new_store = StoreModel(name)
        new_store.save_to_db()

        return {'message': 'SUCCESS'}, 201

    @staticmethod
    @jwt_required()
    def delete(name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()

        return {'message': 'Store name {0} deleted.'.format(name)}


class StoreList(Resource):

    @staticmethod
    @jwt_required()
    def get():
        return {'stores': [store.json() for store in StoreModel.query.all()]}


if __name__ == '__main__':
    sys.exit()
