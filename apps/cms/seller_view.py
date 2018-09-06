from apps.cms import cms_bp
from flask import (render_template,
                   request,
                   redirect,
                   url_for,
                   flash,
                   session)
import uuid
from apps.model import db
from apps.forms.user_form import (RegisterForm,
                                  UserLogin,
                                  )
from apps.model.user_model import User
from werkzeug.security import (generate_password_hash,
                               check_password_hash,
                               )
from flask_login import login_user, login_required, logout_user, current_user


@cms_bp.route("/", endpoint='user_home', methods=["POST", "GET"])
def user_home():
    '''
    后台用户首页,用于用户管理
    要求:
        1.如果用户登陆(session存在标记,直接访问用户页面,如果没有登陆,重定向到登陆页面)
    :return:
    '''
    return render_template("user/userhome.html")


# 用户注册
@cms_bp.route("/register/", endpoint="register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate():
        h_password = generate_password_hash(form.password.data)
        new_user = User()
        # 使用set_attr
        new_user.set_attrs(request.form)
        new_user.password = h_password
        new_user.uuid = str(uuid.uuid4())[-12:]
        db.session.add(new_user)
        db.session.commit()
        # 基本方法
        # new_user = User(username=form.username.data,
        #                 password=h_password,
        #                 # 取uuid 后12位
        #                 uuid=str(uuid.uuid4())[-12:])
        # db.session.add(new_user)
        # db.session.commit()

        return redirect(url_for("cms.login"))
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
        # 格式验证成功
        login_info = request.form
        password = login_info.get("password")
        username = login_info.get("username")

        user = User.query.filter_by(username=username).first()
        if user:
            h_password = user.password
            # 验证密码是否正确
            if check_password_hash(h_password, password):
                login_user(user)
                return redirect(url_for("cms.user_home"))
            else:
                # flash的用法
                '''
                相当于一个可迭代对象,
                '''
                flash("用户名或密码错误!")
        else:
            # flash的用法
            '''
            相当于一个可迭代对象,
            '''
            flash("用户名或密码错误!")
    return render_template("user/login.html", form=form)


# 用户注销
@cms_bp.route("/logout/", endpoint="logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("cms.user_home"))
