import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


load_dotenv(os.path.join(basedir, '.env'))


class Config:
    ADMINS = ['HFA7^#k7G?c?']
    SECRET_KEY = 'my_precious'
    SECURITY_PASSWORD_SALT = 'my_precious_two'

    # mail settings
    MAIL_SERVER = 'mail.tritel.co.ke'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False

    # gmail authentication
    MAIL_USERNAME = "noreply@tritel.co.ke"
    MAIL_PASSWORD = 'HFA7^#k7G?c?'

    # mail accounts
    MAIL_DEFAULT_SENDER = 'noreply@tritel.co.ke'

    PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
    UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# class DevelopementConfig(BaseConfig):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#                               'sqlite:///' + os.path.join(basedir, 'app.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#
# class TestingConfig(BaseConfig):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or \
#                               'mysql+pymysql://root:pass@localhost/flask_app_db'
#
#
# class ProductionConfig(BaseConfig):
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or \
#                               'mysql+pymysql://root:pass@localhost/flask_app_db'
