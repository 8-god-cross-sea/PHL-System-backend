import os
import tempfile


class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'a default secret key')
    CORS_SUPPORTS_CREDENTIALS = True


class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True
    DATABASE = {
        'name': 'dev.db',
        'engine': 'peewee.SqliteDatabase'
    }


class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    DEBUG = True
    TESTING = True
    DATABASE = {
        'name': tempfile.NamedTemporaryFile().name,
        'engine': 'peewee.SqliteDatabase'
    }


class ProductionConfig(BaseConfig):
    """
    Production application configuration
    """
    DEBUG = True
    DATABASE = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': 'phl',
        'user': 'postgres',
        'password': 'hh',
        'host': '127.0.0.1',
        'port': 5432,
    }


class HerokuDeployConfig(BaseConfig):
    """
    Heroku deploy application config
    """
    DEBUG = True

    # parse database url for flask_peewee
    from urllib.parse import urlparse
    url = urlparse(os.getenv('DATABASE_URL'))
    DATABASE = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': url.path[1:],
        'user': url.username,
        'password': url.password,
        'host': url.hostname,
        'port': url.port,
    }
