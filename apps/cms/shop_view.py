from uuid import uuid4
from flask import url_for, request, render_template, abort
from werkzeug.utils import redirect
from apps.model import db
from apps.cms import cms_bp
from flask_login import current_user, login_required

from apps.forms.shop_form import ShopForm
from apps.model.food_model import MenuCategory
from apps.model.shop_model import SellerShop


# 效验shop_id的合法性,得到shop对象
def check_shop_pub_id(shop_id):
    shop = SellerShop.query.filter_by(seller=current_user, pub_id=shop_id).first()
    if not shop:
        return abort(redirect(url_for("cms.user_home")))
    # print(dir(shop))
    return shop


@cms_bp.route("/my_shop/", endpoint="my_shop", methods=["GET"])
@login_required
def my_shop():
    stores = SellerShop.query.filter_by(seller_pid=current_user.id).all()

    return render_template("shop/shoplist.html", stores=stores)


# 店铺添加
@cms_bp.route("/add_shop/", endpoint="add_shop", methods=["GET", "POST"])
@login_required
def add_shop():
    shopform = ShopForm()
    if request.method == "POST" and shopform.validate():
        '''添加店铺信息'''
        new_shop = SellerShop()
        form = request.form
        new_shop.set_attrs(form)
        new_shop.pub_id = str(uuid4())[-12:]
        print(current_user.id)
        new_shop.seller_pid = current_user.id
        new_shop.seller = current_user
        db.session.add(new_shop)
        db.session.commit()
        return redirect(url_for("cms.my_shop"))
    else:
        '''显示店铺添加列表'''
        return render_template("shop/add_shop.html", shopform=shopform)



@cms_bp.route("/shop_upgrade/<pub_id>/", endpoint="shop_update", methods=["GET", "POST"])
@login_required
def shop_update(pub_id):
    shop = check_shop_pub_id(pub_id)
    print(dir(shop))
    update_form = ShopForm(request.form)
    if request.method == "GET":
        shop_form = ShopForm(data=dict(shop))
        return render_template("shop/update_cls.html", shop=shop, flag="店铺", form=shop_form)
    elif request.method == "POST" and update_form.validate():
        # post提交数据
        shop.set_attrs(update_form.data)
        db.session.add(shop)
        db.session.commit()
        return redirect(url_for("cms.my_shop"))


