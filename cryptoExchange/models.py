from datetime import datetime
from uuid import uuid4

from cryptoExchange import db


def generate_uuid():
    return str(uuid4())


class Cryptocurrency(db.Model):
    __tablename__ = 'currencies'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    currency = db.Column(db.String(100), nullable=False)
    date_ = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, currency: str, date: datetime, price: float):
        self.currency = currency
        self.date_ = date
        self.price = price

    def __repr__(self):
        return f'<Crypto {self.currency}> has price {self.price} as of {self.date_}'
