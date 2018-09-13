from flask_sqlalchemy import SQLAlchemy
from redis import Redis

db = SQLAlchemy()
from . import seller_model
from . import shop_model
from . import food_model
from . import buyer_model
from . import cart_model
