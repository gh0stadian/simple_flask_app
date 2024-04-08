import ccxt

from datetime import datetime


class ExchangeResult:
    _dateformat = '%Y-%m-%dT%H:%M:%S'

    def __init__(self, timestamp: str, price: float):
        self.datetime = datetime.fromisoformat(timestamp).strftime(self._dateformat)
        self.price = price


class UnknownExchangeError(Exception):
    pass


class Exchange:

    def __init__(self, exchange_name: str):
        """
        Initializes the Exchange object with the given exchange name
        :param exchange_name: name of the exchange to use. E.g. 'binance'
        """
        try:
            self.exchange = getattr(ccxt, exchange_name)()
        except AttributeError as e:
            raise UnknownExchangeError(f'Unknown exchange: {exchange_name}')

    def fetch_latest_price(self, currency_symbol: str) -> ExchangeResult:
        """
        Fetches the latest price of a cryptocurrency from an exchange
        :param currency_symbol: currency symbol in the format '<COIN>/<PRICE_CURRENCY>'. E.g. 'BTC/USDT'
        :return: ExchangeResult object
        """
        try:
            ticker = self.exchange.fetch_ticker(currency_symbol)
            return ExchangeResult(ticker['datetime'], ticker['last'])

        except ccxt.errors.ExchangeError as e:
            raise UnknownExchangeError(f'Exchange error: {e}')

        except AttributeError as e:
            raise Exception('Error while parsing exchange response. Please try again later.')
