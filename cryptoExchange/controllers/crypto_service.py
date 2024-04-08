from cryptoExchange import db, exchange
from cryptoExchange.models import Cryptocurrency
from cryptoExchange.schema import crypto_currency_schema
from cryptoExchange import Config as conf
from cryptoExchange.connectors.stock_exchange import UnknownExchangeError


def get_and_create_cryptocurrency_entry(currency_symbol: str) -> dict:
    """
    Gets the latest price of a cryptocurrency and create a new entry in the database
    :param currency_symbol: currency symbol in the format '<COIN>'. E.g. 'BTC'
    :return: JSON object of the new entry
    """
    try:
        latest_currency_price = exchange.fetch_latest_price(
            f'{currency_symbol}/{conf.LOCAL_PRICE_CURRENCY}'
        )
    except (UnknownExchangeError, Exception) as e:
        raise ValueError(f'An error occurred: {str(e)}')


    new_entry = Cryptocurrency(
        currency=currency_symbol,
        price=latest_currency_price.price,
        date=latest_currency_price.datetime
    )

    # Persist the new entry to the database
    db.session.add(new_entry)
    db.session.commit()

    return crypto_currency_schema.dump(new_entry)


def show_price_history(page: int, per_page: int = 10) -> dict:
    """
    Shows the paginated price history of all cryptocurrencies.
    :param page: page number
    :param per_page: number of entries per page
    :return: JSON object of the price history
    """
    entries = Cryptocurrency.query.order_by(Cryptocurrency.date_.desc()).paginate(page=page, per_page=per_page)
    return crypto_currency_schema.dump(entries.items, many=True)


def delete_price_history() -> None:
    """
    Deletes all price history entries
    :return: None
    """
    Cryptocurrency.query.delete()
    db.session.commit()
