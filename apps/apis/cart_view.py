import datetime
import random
import time
import uuid
from apps.model import db

from flask import jsonify, request, g, json
from apps.apis import api_bp
from apps.libs.tools import token_require
from apps.model.buyer_model import BuyerAddressModel
from apps.model.cart_model import OrderInfo, OrderGoods
from apps.model.food_model import MenuFood
from apps.settings import api_redis


@api_bp.route('/addcart/', methods=['POST'])
@token_require
def add_cart():
    foods = request.form.getlist("goodsList[]")
    counts = request.form.getlist("goodsCount[]")
    cart_key = "cart_" + g.current_user.tel
    for g_id, cnt in zip(foods, counts):
        food = MenuFood.query.filter_by(goods_id=g_id).first()
        data = {"goods_id": food.goods_id,
                "goods_name": food.goods_name,
                "goods_img": food.goods_img,
                "amount": cnt,
                "goods_price": food.goods_price
                }
        rs = api_redis.hset(cart_key, g_id, json.dumps(data))
        if rs:
            data = {
                "status": "true",
                "message": "添加成功"
            }
            return jsonify(data)
        # print(json.dumps(data))
    # data = {
    #     "goods_list": [{
    #         "goods_id": "1",
    #         "goods_name": "汉堡",
    #         "goods_img": "http://www.homework.com/images/slider-pic2.jpeg",
    #         "amount": 6,
    #         "goods_price": 10
    #     }, {
    #         "goods_id": "1",
    #         "goods_name": "汉堡",
    #         "goods_img": "http://www.homework.com/images/slider-pic2.jpeg",
    #         "amount": 6,
    #         "goods_price": 10
    #     }],
    #     "totalCost": 120
    # }/
    data = {
        "status": "false",
        "message": "添加失败"
    }
    return jsonify(data)


# # 获取购物车数据
@api_bp.route('/cart/', methods=['GET'])
@token_require
def get_cart_goods():
    cart_key = "cart_" + g.current_user.tel
    redis_data = api_redis.hgetall(cart_key)
    goods_list = []
    for _, v in redis_data.items():
        goods_list.append(json.loads(v))
    data = {"goods_list": goods_list}
    # data = {json.loads(v) for _, v in redis_data.items()}

    # print(type(redis_data))
    # data = json.loads(data)
    # data = {
    #     "goods_list": [{
    #         "goods_id": "1",
    #         "goods_name": "汉堡",
    #         "goods_img": "http://www.homework.com/images/slider-pic2.jpeg",
    #         "amount": 6,
    #         "goods_price": 10
    #     }, {
    #         "goods_id": "1",
    #         "goods_name": "汉堡",
    #         "goods_img": "http://www.homework.com/images/slider-pic2.jpeg",
    #         "amount": 6,
    #         "goods_price": 10
    #     }],
    #     "totalCost": 120
    # }
    # print(data)
    return jsonify(data)


# # 获取订单列表
# @api_bp.route('/orders/', methods=['GET'])
# def get_order_list():
#     data = [
#         {
#             "id": "1",
#             "order_code": "0000001",
#             "order_birth_time": "2017-02-17 18:36",
#             "order_status": "已完成",
#             "shop_id": "1",
#             "shop_name": "上沙麦当劳",
#             "shop_img": "/images/shop-logo.png",
#             "goods_list": [{
#                 "goods_id": "1",
#                 "goods_name": "汉堡",
#                 "goods_img": "/images/slider-pic2.jpeg",
#                 "amount": 6,
#                 "goods_price": 10
#             }, {
#                 "goods_id": "1",
#                 "goods_name": "汉堡",
#                 "goods_img": "/images/slider-pic2.jpeg",
#                 "amount": 6,
#                 "goods_price": 10
#             }],
#             "order_price": 120,
#             "order_address": "北京市朝阳区霄云路50号 距离市中心约7378米北京市朝阳区霄云路50号 距离市中心约7378米"
#         },
#         {
#             "id": "1",
#             "order_code": "0000001",
#             "order_birth_time": "2017-02-17 18:36",
#             "order_status": "已完成",
#             "shop_id": "1",
#             "shop_name": "上沙麦当劳",
#             "shop_img": "/images/shop-logo.png",
#             "goods_list": [{
#                 "goods_id": "1",
#                 "goods_name": "汉堡",
#                 "goods_img": "/images/slider-pic2.jpeg",
#                 "amount": 6,
#                 "goods_price": 10
#             }, {
#                 "goods_id": "1",
#                 "goods_name": "汉堡",
#                 "goods_img": "/images/slider-pic2.jpeg",
#                 "amount": 6,
#                 "goods_price": 10
#             }],
#             "order_price": 120,
#             "order_address": "北京市朝阳区霄云路50号 距离市中心约7378米北京市朝阳区霄云路50号 距离市中心约7378米"
#         }
#     ]
#     return jsonify(data)
#
#
# # 得到指定订单
# @api_bp.route('/order/', methods=['GET'])
# def get_order():
#     data = {
#         "id": "1",
#         "order_code": "0000001",
#         "order_birth_time": "2017-02-17 18:36",
#         "order_status": "代付款",
#         "shop_id": "1",
#         "shop_name": "上沙麦当劳",
#         "shop_img": "/images/shop-logo.png",
#         "goods_list": [{
#             "goods_id": "1",
#             "goods_name": "汉堡",
#             "goods_img": "/images/slider-pic2.jpeg",
#             "amount": 6,
#             "goods_price": 10
#         }, {
#             "goods_id": "1",
#             "goods_name": "汉堡",
#             "goods_img": "/images/slider-pic2.jpeg",
#             "amount": 6,
#             "goods_price": 10
#         }],
#         "order_price": 120,
#         "order_address": "北京市朝阳区霄云路50号 距离市中心约7378米北京市朝阳区霄云路50号 距离市中心约7378米"
#     }
#     return jsonify(data)
#
#
# 添加到订单
@api_bp.route('/order/', methods=['POST'])
@token_require
def add_order():
    if request.method == "POST":
        addr_id = request.form.get("address_id")
        if addr_id != "0":
            order_info = OrderInfo()
            cart = api_redis.hgetall("cart_" + g.current_user.tel)
            # 取 hash 对象的 field值
            shop_id = 0
            total = 0
            for x, _ in cart.items():
                count = int(json.loads(_).get("amount"))
                good_info = MenuFood.query.filter_by(goods_id=x.decode("utf-8")).first()
                total += int(good_info.goods_price) * count
                shop_id = good_info.shop_pid
            #     准备订单码,收货人地址,
            order_code = datetime.datetime.now().strftime('%Y%m%d') + str(random.randint(1000, 9999))
            addr = BuyerAddressModel.query.get(addr_id)
            address = addr.provence + addr.city + addr.area + addr.detail_address

            data = {"order_code": order_code,
                    "shop_id": shop_id,
                    "user_id": g.current_user.id,
                    "order_address": address,
                    "order_price": total,
                    "order_status": "待支付",
                    "created_time": datetime.datetime.now(),
                    # "created_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "trade_sn": str(uuid.uuid4())
                    }
            order_info.set_attrs(data)
            db.session.add(order_info)
            db.session.commit()
            for _, info in cart.items():
                order_good = OrderGoods()
                goods_info = json.loads(info)
                order_good.set_attrs(goods_info)
                order_good.order_id = order_code
                db.session.add(order_good)
                db.session.commit()
            data = {
                "status": "false",
                "message": "添加成功",
                "id": order_code
            }

            return jsonify(data)
        data = {
            "status": "false",
            "message": "无效收货地址",
        }
        return jsonify(data)
