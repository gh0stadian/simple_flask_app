import os
import pytest
from cryptoExchange.connectors.stock_exchange import Exchange, UnknownExchangeError, ExchangeResult


class TestExchange():
    exchange = Exchange('binance')

    def test_wrong_exchange(self):
        with pytest.raises(UnknownExchangeError) as e:
            Exchange('wrong_exchange')
        assert str(e.value) == f'Unknown exchange: wrong_exchange'

    def test_wrong_currency(self):
        currency_symbol = 'wrong_currency'
        with pytest.raises(UnknownExchangeError) as e:
            self.exchange.fetch_latest_price(currency_symbol)
        assert str(e.value) == f'Exchange error: binance does not have market symbol {currency_symbol}'

    def test_fetch_latest_price(self, exchange_override=None, local_currency='USDT'):
        exchange = exchange_override if exchange_override else self.exchange
        currency_symbol = f'BTC/{local_currency}'
        result = exchange.fetch_latest_price(currency_symbol)
        assert isinstance(result, ExchangeResult)
        assert result.price > 0

    def test_selected_exchange(self):
        exchange_name = os.environ.get('EXCHANGE_NAME')

        if not exchange_name:
            pytest.skip('env. variable EXCHANGE_NAME is not set. Skipping test...')

        else:
            self.test_fetch_latest_price(exchange_override=Exchange(exchange_name))

    def test_selected_local_currency(self):
        local_currency = os.environ.get('LOCAL_PRICE_CURRENCY')

        if not local_currency:
            pytest.skip('env. variable LOCAL_PRICE_CURRENCY is not set. Skipping test...')
        else:
            self.test_fetch_latest_price(local_currency)
