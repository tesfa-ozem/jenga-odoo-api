import os
from logging.handlers import RotatingFileHandler
import logging
from flask import Flask
from flask_cors import CORS
from config import Config
from flask_mail import Mail

mail = Mail()


def create_app(config_class=Config, ):
    # create application instance
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    mail.init_app(app)

    from gateway.api import mod as mod
    app.register_blueprint(mod)

    if not app.debug:

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/sacoo.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s:\
                 %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Saccostartup')

    return app
