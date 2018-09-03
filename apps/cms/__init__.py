from flask import Blueprint

cms_bp = Blueprint("cms", __name__, subdomain="cms")

from . import view
