from flask import Blueprint

api_bp = Blueprint("api", __name__, subdomain="api")

from . import apis_view