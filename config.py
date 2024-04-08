from os import environ, path

BASE_DIR = path.abspath(path.dirname(__file__))


class Config(object):
    DEBUG = environ.get('DEBUG', False)

    EXCHANGE_NAME = environ.get('EXCHANGE_NAME', "kucoin")
    LOCAL_PRICE_CURRENCY = environ.get('LOCAL_PRICE_CURRENCY', "USDT")

    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
