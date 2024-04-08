from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from cryptoExchange.connectors.stock_exchange import Exchange

from config import Config

# app
app = Flask(__name__)
app.config.from_object(Config)

# schema
ma = Marshmallow(app)


# db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# exchange
exchange = Exchange(Config.EXCHANGE_NAME)

# routes and models
from cryptoExchange import routes, models


