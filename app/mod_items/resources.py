import sys

from flask_jwt import jwt_required
from flask_restful import Resource

from app.mod_items import ItemModel
from app.mod_store import StoreModel
from app.parse_input import ValueParser


class Item(Resource):

    @staticmethod
    @jwt_required()
    def get(name):
        item = ItemModel.find_by_name(name)

        return item.json() if item else {'message': 'item NOT found'}, 403

    @staticmethod
    @jwt_required()
    def post(name):
        item = ItemModel.find_by_name(name)

        if item:
            return {'message': 'item {0} already in DB'.format(name)}

        data = ValueParser.parse_price_store_id().parse_args()

        if not StoreModel.find_by_id(data['store_id']):
            return {'message': 'Store with id {0} \
                    does NOT exist'.format(data['store_id'])}, 403

        new_item = ItemModel(name, **data)
        new_item.save_to_db()

        return {'message': 'SUCCESS'}, 201

    @staticmethod
    @jwt_required()
    def delete(name):
        item = ItemModel.find_by_name(name)

        if not item:
            return {'message': 'item {0} does NOT exists'.format(name)}, 403

        item.delete_from_db()

        return {'message': 'SUCCESS'}, 200

    @staticmethod
    @jwt_required()
    def put(name):
        data = ValueParser.parse_price_store_id().parse_args()

        if not StoreModel.find_by_id(data['store_id']):
            return {'message': 'Store with id {0} \
                    does NOT exist'.format(data['store_id'])}, 403

        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
            item.store_id = data['store_id']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return {'added': 'SUCCESS'}, 200


class Items(Resource):

    @staticmethod
    @jwt_required()
    def get():
        return {'items': [item.json() for item in ItemModel.query.all()]}


if __name__ == '__main__':
    sys.exit()
