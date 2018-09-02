from flask import Blueprint

user_bp = Blueprint("user", __name__, subdomain="user")

from . import view
