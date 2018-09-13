from flask_bootstrap import Bootstrap
from flask_script import Manager
# from flask_session import Session
from apps import create_api_app
from apps.model import db
from flask_migrate import Migrate, MigrateCommand

vue_app = create_api_app()
Migrate(vue_app, db=db)
Bootstrap(vue_app)
# Session(vue_app)
manger = Manager(vue_app, db)
manger.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manger.run()
