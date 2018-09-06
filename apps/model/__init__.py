from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from . import user_model
from . import shop_model
from . import food_model
