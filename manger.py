from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_session import Session

from apps import create_app
from apps.model import db
from flask_migrate import Migrate, MigrateCommand

app = create_app()
Migrate(app, db=db)
Bootstrap(app)
Session(app)

# manger = Manager(app,) 也行
manger = Manager(app, db)
manger.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manger.run()
