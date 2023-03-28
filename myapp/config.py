# -*- coding: utf-8 -*- 
import os
import logging
from logging.handlers import RotatingFileHandler
import time

class BaseConfig(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'qb76d7681fqbe2fbaefqb41f862efbb7c91a92a492fb271t'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = '/tmp/app.log'
    LOGGING_LEVEL = logging.DEBUG

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


config = {
    "development": "config.DevelopmentConfig",
    "production": "config.ProductionConfig",
}


def configure_app(app):
    # Set Env variable
    config_name = os.getenv('FLASK_CONFIGURATION', 'development')

    # object-based default configuration
    app.config.from_object(config[config_name]) 

     # Configure Logger
    handler = RotatingFileHandler(app.config['LOGGING_LOCATION'], maxBytes=10000, backupCount=1)
    handler.setLevel(app.config['LOGGING_LEVEL'])

    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    
    app.logger.setLevel(app.config['LOGGING_LEVEL'])
    app.logger.addHandler(handler)
    