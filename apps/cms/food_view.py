from uuid import uuid4
from flask import url_for, request, render_template, abort
from werkzeug.utils import redirect

from apps.forms.food_form import MenuCategoryForm, MenuFoodForm
from apps.model import db
from apps.cms import cms_bp
from flask_login import current_user, login_required

from apps.forms.shop_form import ShopForm
from apps.model.food_model import MenuCategory, MenuFood
from apps.model.shop_model import SellerShop

# 添加分类
from apps.model.food_model import MenuCategory


# 效验cate_id的合法性,得到分类对象
def check_cate_pub_id(shop_id, pub_id):
    cate = MenuCategory.query.filter_by(pub_id=pub_id, shop_id=shop_id).first()
    if not cate:
        return abort(redirect(url_for("cms.user_home")))
    return cate


@cms_bp.route("/cate_add/<shop_pub_id>/", endpoint="cate_add", methods=["GET", "POST"])
@login_required
def cate_add(shop_pub_id):
    cate_form = MenuCategoryForm()
    if request.method == "POST" and cate_form.validate():
        cate = MenuCategory()
        form = request.form
        cate.set_attrs(form)
        cate.pub_id = str(uuid4())[-12:]
        cate.shop_id = shop_pub_id
        db.session.add(cate)
        db.session.commit()
        return redirect(url_for("cms.my_shop"))
    return render_template("food/add_cate.html", form=cate_form)


# 分类列表
@cms_bp.route("/my_cate/<shop_id>", endpoint="my_cate", methods=["GET"])
@login_required
def my_cate(shop_id):
    cates = MenuCategory.query.filter_by(shop_id=shop_id).all()
    return render_template("food/cate_list.html", cates=cates)


# 分类更新
@cms_bp.route("/cate_update/<shop_id>/<pub_id>/", endpoint="cate_update", methods=["GET", "POST"])
@login_required
def cate_update(shop_id, pub_id):
    cate = check_cate_pub_id(shop_id, pub_id)
    print(dir(cate))

    update_form = MenuCategoryForm(request.form)
    if request.method == "GET":
        cate_form = MenuCategoryForm(data=dict(cate))
        return render_template("food/cate_update.html", cate=cate_form)
    elif request.method == "POST" and update_form.validate():
        # post提交数据
        cate = check_cate_pub_id(shop_id, pub_id)
        cate.set_attrs(update_form.data)
        db.session.add(cate)
        db.session.commit()
        return redirect(url_for("cms.my_cate", shop_id=shop_id))


@cms_bp.route("/food_add/<shop_pub_id>", endpoint="food_add", methods=["GET", "POST"])
@login_required
def food_add(shop_pub_id):
    cates = MenuCategory.query.filter_by(shop_id=shop_pub_id).all()
    food_form = MenuFoodForm(cates)
    if request.method == "POST":
        food = MenuFood()
        form = request.form
        food.set_attrs(form)
        food.goods_id = str(uuid4())[-12:]
        food.shop_id = shop_pub_id
        db.session.add(food)
        db.session.commit()
        return redirect(url_for("cms.my_shop"))
    return render_template("food/add_food.html", form=food_form)


# 查看店铺菜品
@cms_bp.route("/my_food/<shop_id>", endpoint="my_food", methods=["GET"])
@login_required
def my_food(shop_id):
    foods = MenuFood.query.filter_by(shop_id=shop_id).all()
    print(dir(foods))
    return render_template("food/food_list.html", foods=foods)


@cms_bp.route("/food_update/<food_pid>/<shop_pub_id>/", endpoint="food_update", methods=["GET", "POST"])
@login_required
def food_update(food_pid, shop_pub_id):
    food = MenuFood.query.filter_by(goods_id=food_pid).first()
    update_form = MenuFoodForm(request.form)
    if request.method == "GET":
        cates = MenuCategory.query.filter_by(shop_id=shop_pub_id).all()
        food_form = MenuFoodForm(cates, data=dict(food))
        return render_template("food/food_update.html", food=food_form)
    elif request.method == "POST" and update_form.validate():
        # post提交数据
        food.set_attrs(update_form.data)
        db.session.add(food)
        db.session.commit()
        return "修改成功"


@cms_bp.route("/test/")
def test():
    form = MenuCategoryForm()
