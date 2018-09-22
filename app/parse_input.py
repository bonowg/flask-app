import sys

from flask_restful import reqparse


class ValueParser(object):

    @staticmethod
    def parse_username_password():
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help='username field cannot be empty!')
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help='password field cannot be empty!')
        return parser

    @staticmethod
    def parse_all_for_user():
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            type=str,
                            required=True,
                            help='username field cannot be empty!')
        parser.add_argument('email',
                            type=str,
                            required=True,
                            help='email field cannot be empty!')
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help='password field cannot be empty!')
        return parser

    @staticmethod
    def parse_price():
        parser = reqparse.RequestParser()
        parser.add_argument('price',
                            type = float,
                            required = True,
                            help = "price filed cannot be empty!")
        return parser

    @staticmethod
    def parse_price_store_id():
        parser = reqparse.RequestParser()
        parser.add_argument('price',
                            type = float,
                            required = True,
                            help = "price filed cannot be empty!")
        parser.add_argument('store_id',
                            type = int,
                            required = True,
                            help = "store_id filed cannot be empty!")
        return parser

    @staticmethod
    def parse_name():
        parser = reqparse.RequestParser()
        parser.add_argument('name',
                            type = str,
                            required = True,
                            help = 'name field cannot be empty!')
        return parser


if __name__ == '__main__':
    sys.exit()