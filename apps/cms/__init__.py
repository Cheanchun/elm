from flask import Blueprint

cms_bp = Blueprint("cms", __name__, subdomain="cms")

from . import seller_view
from . import shop_view
from . import food_view

