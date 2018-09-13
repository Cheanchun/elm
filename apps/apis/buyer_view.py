from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import random
from apps.model import db
from flask import jsonify, request, current_app, g
from apps.libs.tools import token_require
from apps.apis import api_bp

from apps.forms.buyer_form import BuyerRegisterForm, BuyerLoginForm, BuyerAddressForm
from apps.model.buyer_model import BuyerUser, BuyerAddressModel
from apps.settings import api_redis


# 短信验证码api
@api_bp.route('/sms/', methods=['GET'])
def get_sms():
    tel = "reg_" + request.args.get("tel")
    # 生成验证码
    code = "".join([str(random.randint(0, 9)) for _ in range(6)])
    print("本次验证码为:", code)
    # 获得自定义配置文件的过期时间
    time = current_app.config.get("SMS_LIFETIME")
    # 设置到redis数据库
    api_redis.setex(tel, code, time)
    data = {
        "status": True,
        "message": "获取短信验证码成功"
    }
    return jsonify(data)


# 买家用户注册 api
@api_bp.route('/register/', endpoint='register', methods=['POST'])
def register():
    register_form = BuyerRegisterForm(request.form)
    if register_form.validate():
        u1 = BuyerUser()
        u1.set_attrs(register_form.data)
        db.session.add(u1)
        db.session.commit()
        data = {
            "status": "true",
            "message": "注册成功"
        }
        return jsonify(data)
    return jsonify({"status": "false", "message": [v for _, v in register_form.errors.items()][0]})


# 登陆api
@api_bp.route('/login/', endpoint='login', methods=['POST'])
def login():
    login_form = BuyerLoginForm(request.form)
    if login_form.validate():
        user = BuyerUser.query.filter_by(username=login_form.name.data).first()
        '''产生token'''
        s = Serializer(current_app.config["SECRET_KEY"], expires_in=current_app.config["TOKEN_EXPIRES"])
        data = s.dumps({"tel": user.tel, "username": user.username})
        response = jsonify({
            "status": "true",
            "message": "登录成功",
            "user_id": user.id,
            "username": user.username,

        })
        response.set_cookie('token', data.decode('ascii'))
        # todo-------------网传方法---------------------------------
        # m = hashlib.md5()
        # m.update(phone_number)
        # m.update(password)
        # m.update(str(int(time.time())))
        # token = m.hexdigest()
        # api_redis.hmset('user:%s' % user.phone_number, {'token': token, 'nickname': user.nickname, 'app_online': 1})
        # api_redis.set('token:%s' % token, user.phone_number)
        # api_redis.expire('token:%s' % token, 3600 * 24 * 30)
        # -----------------------------------------------

        return response
    date = {"status": "false", "message": [v for _, v in login_form.errors.items()][0]}

    return jsonify(date)


# 收获地址api
@api_bp.route('/addresslist/', endpoint='addresslist', methods=['GET'])
@token_require
def get_address_list():
    addresses = g.current_user.addresses
    data = [dict(address) for address in addresses]
    return jsonify(data)


@api_bp.route('/address/', endpoint="showaddress", methods=['GET'])
@token_require
def single_address():
    add_id = request.args.get("id")
    addr = BuyerAddressModel.query.get(add_id)
    data = dict(addr)
    return jsonify(data)


# 新增/修改地址API
@api_bp.route('/address/', endpoint="address", methods=['POST'])
@token_require
def address():
    address_form = BuyerAddressForm(request.form)
    if request.form.get("id") and address_form.validate():
        address = BuyerAddressModel.query.filter_by(id=request.form.get("id")).first()

        address.set_attrs(address_form.data)
        db.session.add(address)
        db.session.commit()
        data = {
            "status": "true",
            "message": "修改成功"
        }
        return jsonify(data)
    address = BuyerAddressModel()
    address.set_attrs(address_form.data)
    address.user_id = g.current_user.id
    db.session.add(address)
    db.session.commit()
    data = {
        "status": "true",
        "message": "添加成功"
    }
    return jsonify(data)


@api_bp.route('/password/', methods=['POST'])
def change_password():
    data = {
        "status": "true",
        "message": "修改成功"
    }
    return jsonify(data)


# 忘记密码接口
@api_bp.route('/new_password/', methods=['POST'])
def forget_password():
    data = {
        "status": "true",
        "message": "添加成功"
    }
    return jsonify(data)
