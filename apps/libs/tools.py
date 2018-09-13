from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from functools import wraps

from flask import request, jsonify, current_app, g

from apps.model.buyer_model import BuyerUser


# 用户认证装饰器
def token_require(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        # 判断cookie中是否有token
        token = request.cookies.get("token")
        if not token:
            return jsonify({"status": "false", "message": "没有token"})
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
            return jsonify({"status": "false", "message": "错误的token"})
        tel = data.get("tel")
        # 判断用户
        user = BuyerUser.query.filter_by(tel=tel).first()
        if not user:
            return jsonify({"status": "false", "message": "无效用户"})
        g.current_user = user
        # g.user = user  自定义上下文变量(装饰器中)
        return fn(*args, **kwargs)

    return decorated
