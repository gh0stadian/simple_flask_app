import pytest

from cryptoExchange.controllers.crypto_service import get_and_create_cryptocurrency_entry, show_price_history, \
    delete_price_history

from cryptoExchange import app


class TestCryptoServiceController:
    def test_get_and_create_cryptocurrency_entry(self):
        currency_symbol = 'BTC'

        with app.app_context():
            result = get_and_create_cryptocurrency_entry(currency_symbol)

        assert result['currency'] == currency_symbol
        assert result['price'] > 0
        assert 'date_' in result

    def test_get_and_create_cryptocurrency_entry_error(self):
        currency_symbol = 'WRONG'


        with app.app_context():
            with pytest.raises(ValueError) as e:
                get_and_create_cryptocurrency_entry(currency_symbol)

    def test_show_price_history(self):
        with app.app_context():
            result = show_price_history(1)

            if len(result) == 0: # If there are no entries in the database
                get_and_create_cryptocurrency_entry('BTC')
                result = show_price_history(1)

        assert isinstance(result, list)
        assert len(result) > 0

    def test_delete_price_history(self):
        with app.app_context():
            if len(show_price_history(1)) == 0: # If there are no entries in the database
                get_and_create_cryptocurrency_entry('BTC')
                assert len(show_price_history(1)) > 0

            delete_price_history()
            result = show_price_history(1)
        assert len(result) == 0