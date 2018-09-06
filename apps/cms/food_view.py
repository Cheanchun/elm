from apps.cms import cms_bp
from flask_login import current_user,login_required


@cms_bp.route("/goods_add/", endpoint="goods_add", methods=["GET", "POST"])
@login_required
def goods_add():
    shop_id = 1
    return "{}商家在商品id为{}中添加菜名".format(current_user.username, shop_id)
