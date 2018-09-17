from flask import Blueprint

cms_bp = Blueprint("cms", __name__, url_prefix="/cms")

from . import seller_view
from . import shop_view
from . import food_view

