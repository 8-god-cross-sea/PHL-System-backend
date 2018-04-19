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
        'engine': 'playhouse.pool.PooledSqliteDatabase'
    }


class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    TESTING = True
    DATABASE = {
        'name': tempfile.NamedTemporaryFile().name,
        'engine': 'playhouse.pool.PooledSqliteDatabase'
    }


class ProductionConfig(BaseConfig):
    """
    Production application configuration
    """
    DATABASE = {
        'engine': 'playhouse.pool.PooledPostgresqlDatabase',
        'name': 'postgres',
        'user': 'postgres',
        'host': 'db',
        'port': 5432,
    }


class HerokuDeployConfig(BaseConfig):
    """
    Heroku deploy application config
    """
    # parse database url for flask_peewee
    from urllib.parse import urlparse
    url = urlparse(os.getenv('DATABASE_URL'))
    DATABASE = {
        'engine': 'playhouse.pool.PooledPostgresqlDatabase',
        'name': url.path[1:],
        'user': url.username,
        'password': url.password,
        'host': url.hostname,
        'port': url.port,
    }
