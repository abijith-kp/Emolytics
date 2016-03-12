import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
RQ_DEFAULT_HOST = 'localhost'
RQ_DEFAULT_PORT = 6379
RQ_DEFAULT_DB = 0

# change this function as per the implementation to load the dataset for
# supervised classifier
LOAD_FUNCTION = 'server.dataset.load_dataset'
