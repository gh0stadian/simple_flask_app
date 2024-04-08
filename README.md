# CryptoExchange app
This is a simple app that allows you to check the current price of cryptocurrencies in selectable currency. 
It uses the ccxt library to get the data.

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
