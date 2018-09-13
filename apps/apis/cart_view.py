from flask import jsonify, request, g, json
from apps.apis import api_bp
from apps.libs.tools import token_require
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


# 获取购物车数据
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


# 获取订单列表
@api_bp.route('/orders/', methods=['GET'])
def get_order_list():
    data = [
        {
            "id": "1",
            "order_code": "0000001",
            "order_birth_time": "2017-02-17 18:36",
            "order_status": "已完成",
            "shop_id": "1",
            "shop_name": "上沙麦当劳",
            "shop_img": "/images/shop-logo.png",
            "goods_list": [{
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }, {
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }],
            "order_price": 120,
            "order_address": "北京市朝阳区霄云路50号 距离市中心约7378米北京市朝阳区霄云路50号 距离市中心约7378米"
        },
        {
            "id": "1",
            "order_code": "0000001",
            "order_birth_time": "2017-02-17 18:36",
            "order_status": "已完成",
            "shop_id": "1",
            "shop_name": "上沙麦当劳",
            "shop_img": "/images/shop-logo.png",
            "goods_list": [{
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }, {
                "goods_id": "1",
                "goods_name": "汉堡",
                "goods_img": "/images/slider-pic2.jpeg",
                "amount": 6,
                "goods_price": 10
            }],
            "order_price": 120,
            "order_address": "北京市朝阳区霄云路50号 距离市中心约7378米北京市朝阳区霄云路50号 距离市中心约7378米"
        }
    ]
    return jsonify(data)


# 得到指定订单
@api_bp.route('/order/', methods=['GET'])
def get_order():
    data = {
        "id": "1",
        "order_code": "0000001",
        "order_birth_time": "2017-02-17 18:36",
        "order_status": "代付款",
        "shop_id": "1",
        "shop_name": "上沙麦当劳",
        "shop_img": "/images/shop-logo.png",
        "goods_list": [{
            "goods_id": "1",
            "goods_name": "汉堡",
            "goods_img": "/images/slider-pic2.jpeg",
            "amount": 6,
            "goods_price": 10
        }, {
            "goods_id": "1",
            "goods_name": "汉堡",
            "goods_img": "/images/slider-pic2.jpeg",
            "amount": 6,
            "goods_price": 10
        }],
        "order_price": 120,
        "order_address": "北京市朝阳区霄云路50号 距离市中心约7378米北京市朝阳区霄云路50号 距离市中心约7378米"
    }
    return jsonify(data)


# 添加到订单
@api_bp.route('/order/', methods=['POST'])
def add_order():
    data = {
        "status": "true",
        "message": "添加成功",
        "order_id": 1
    }
    return jsonify(data)
