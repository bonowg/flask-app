#!/home/wojtek/Venv/udemy-flask/bin/python
from flask_migrate import MigrateCommand, migrate, Manager, Migrate

migrate = Migrate()
manager = Manager()
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
