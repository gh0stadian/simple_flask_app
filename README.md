# CryptoExchange app
This is a simple app that allows you to check the current price of cryptocurrencies in selectable currency. 
It uses the ccxt library to get the crypto price data.
These prices are stored in a database and can be viewed in paginated form. 

## Endpoints
1. GET  `/price/<currency>` - Gets and stores the price of the cryptocurrency price
2. GET  `/price/history?page=1` - List of all the prices stored in the database. If you not specify the page, it will default to 1
3. DELETE `price/history` - Deletes all the prices stored in the database

## Prerequisites
1. Python 3.11
2. PostgreSQL database (or any other database that SQLAlchemy supports, but you will have to install required dependencies)

## Installation
1. Clone the repository
2. Install the requirements
```bash
pip install -r requirements.txt
```
3. Set the environment variable
```bash
export DEBUG=flag_to_enable_debug_mode, default is False

export SQLALCHEMY_DATABASE_URI=fill_this_with_your_database_uri
export SECRET_KEY=fill_this_with_your_secret_key

# Optional exchange configuration
export EXCHANGE_NAME=exchange_name, defaults to kucoin
export LOCAL_PRICE_CURRENCY=currency, defaults to USDT (Note: this is the currency in which the prices are stored in db)
```

4. Migrate database
```bash
flask db init
flask db migrate -m tables
flask db upgrade
```

5. Run the app
```bash
flask run
# OR
python app.py
```
