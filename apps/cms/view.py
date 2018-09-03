from apps.cms import cms_bp
from flask import render_template, request, redirect, url_for
import uuid
from apps.libs.helper import set_attrs
from apps.model import db
from apps.forms.user_form import RegisterForm, UserLogin
from apps.model.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash


@cms_bp.route("/", endpoint='user_home', methods=["POST", "GET"])
def user_home():
    '''
    后台用户首页,用于用户管理
    要求:
        1.如果用户登陆(session存在标记,直接访问用户页面,如果没有登陆,重定向到登陆页面)
    :return:
    '''
    if request.method == "GET":
        return render_template("user/userhome.html", )


# 用户注册
@cms_bp.route("/register/", endpoint="register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate():
        h_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data,
                        password=h_password,
                        # 取uuid 后12位
                        uuid=str(uuid.uuid4())[-12:])
        db.session.add(new_user)
        db.session.commit()

        # 如何使用 set_attrs
        # new_user = set_attrs(new_user, form.data)
        # db.session.add(new_user)

        return redirect(url_for("cms.user_home"))
    else:
        return render_template("user/register.html", form=form)


# 用户登陆
@cms_bp.route("/login/", endpoint="login", methods=["POST", "GET"])
def login():
    '''
    post:提交用户登陆信息
    get:展示登陆页面
    :return:
    '''
    form = UserLogin()
    if request.method == "POST" and form.validate():
        form = request.form
        print()
        return
    else:
        return render_template("user/login.html", form=form)
