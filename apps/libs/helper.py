
from flask import session, redirect, url_for


# 定义从attrs字典结构中,赋值表字段名
def set_attrs(self, attrs):
    for k, v in attrs.items():
        if hasattr(self, k) and k != 'id':
            setattr(self, k, v)
# 登陆装饰器
# def login_verify():
#     if not session.get("username"):
#         return redirect(url_for("cms.login"))
