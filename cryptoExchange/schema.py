from cryptoExchange import ma
from cryptoExchange.models import Cryptocurrency


class CryptoCurrencySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cryptocurrency
        load_instance = True
        fields = ('currency', 'date_', 'price')


crypto_currency_schema = CryptoCurrencySchema()
crypto_currency_history_schema = CryptoCurrencySchema(many=True)
