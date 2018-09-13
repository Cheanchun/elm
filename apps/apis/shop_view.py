import random

from flask import render_template, redirect, url_for, jsonify, request

from apps.apis import api_bp

# @api_bp.route("/", endpoint="index", methods=["GET"])
# def index():
#     return redirect(url_for("static", filename="index.html"))
from apps.model.food_model import MenuCategory
from apps.model.shop_model import SellerShop


@api_bp.route("/shop_list/", endpoint="shop_list")
def shop_list():
    shops = SellerShop.query.all()
    shop = [dict(**dict(x), **{"id": x.pub_id}, **{"distance": random.randint(100, 1000)}) for x in shops]
    # print(shop)
    return jsonify(shop)


@api_bp.route("/shop/", endpoint="shop")
def shop():
    id = request.args.get("id")
    shop = SellerShop.query.filter_by(pub_id=id).first()
    cates = shop.categories
    data = {
        "commodity": [{**dict(cate), "goods_list": [{**dict(good), "goods_id": good.goods_id} for good in cate.foods]}
                      for cate
                      in cates]}
    shop = dict(shop)
    data = {**shop, **data}
    print(data)
    return jsonify(data)
