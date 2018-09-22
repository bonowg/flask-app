#!/home/wojtek/Venv/udemy-flask/bin/python
from app import create_app
from app.dbase import db
from flask_migrate import MigrateCommand, migrate, Manager, Migrate

appx = create_app()

migrate = Migrate(appx, db)
manager = Manager(appx)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
