from config import Config

from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Manager
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager

from app.mod_user.resources import UserRegister, UserEdit
from app.mod_items.resources import Item, Items
from app.mod_store.resources import Store, StoreList
from app.security import authenticate, identity
from app.views import main_page
from app.mod_items.views import items_page
from app.mod_auth.views import login_page, logout_page
from app.dbase import db
from app.dbase import login_manager
from app.mod_manage.manage import migrate, manager
from flask_migrate import Manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    api = Api(app)
    jwt = JWT(app, authenticate, identity)
    debugtoolbat = DebugToolbarExtension(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login_page.login_show'
    migrate.init_app(app, db)
    manager.__init__(app)

    # create end point route to student get
    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(Items, '/items')
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserEdit, '/userchange/<string:name>')
    api.add_resource(Store, '/store/<string:name>')
    api.add_resource(StoreList, '/stores')

    app.register_blueprint(main_page)
    app.register_blueprint(items_page)
    app.register_blueprint(login_page)
    app.register_blueprint(logout_page)

    #create db objects
    @app.before_first_request
    def create_tables():
        db.create_all()

    # Sample HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    return app

