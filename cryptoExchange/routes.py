from flask import request

from cryptoExchange import app, db
from cryptoExchange.controllers.crypto_service import get_and_create_cryptocurrency_entry, show_price_history, \
    delete_price_history


@app.route('/price/<currency>', methods=['GET'])
def get_currency_price(currency=None):
    try:
        return get_and_create_cryptocurrency_entry(currency), 201
    except ValueError as e:
        return f'An error occurred: {str(e)}', 400
    except Exception as e:
        return f'An error occurred: {str(e)}', 500


@app.route('/price/history', methods=['GET'])
def price_history():
    try:
        page = request.args.get('page', default=1, type=int)
        return show_price_history(page), 200
    except Exception as e:
        return f'An error occurred: {str(e)}', 500


@app.route('/price/history', methods=['DELETE'])
def delete_history():
    try:
        delete_price_history()
        return 'Price history deleted successfully', 204
    except Exception as e:
        return f'An error occurred: {str(e)}', 500


@app.route('/migrate', methods=['POST'])
def migrate_db():
    try:
        db.create_all()
        return 'Database migrated successfully', 201
    except Exception as e:
        return f'An error occurred: {str(e)}', 500
