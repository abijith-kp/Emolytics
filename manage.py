#!/usr/bin/python2.7

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from server import emolytics, db

migrate = Migrate(emolytics, db)
manager = Manager(emolytics)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
