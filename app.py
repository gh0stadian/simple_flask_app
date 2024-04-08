from config import Config
from cryptoExchange import app

if __name__ == '__main__':
    app.secret_key = Config.SECRET_KEY
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run(host='0.0.0.0', port=8087)
