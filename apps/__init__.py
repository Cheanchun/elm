from flask import Flask
from flask_session import Session
from apps.cms import cms_bp
from apps.model import db
from flask_login import LoginManager

from apps.model.user_model import User

login_manager = LoginManager()
login_manager.login_view = 'cms.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def register_blue(app):
    app.register_blueprint(cms_bp)


def register_session(app):
    # 设置session过期时间
    # app.permanent_session_lifetime = timedelta(seconds=10)
    Session(app)


def app_config(app):
    # 加载app 配置文件
    app.config.from_object("apps.settings.DevConfig")


def create_app():
    app = Flask(__name__)
    app_config(app)
    # 初始化 数据库模型
    db.init_app(app)
    login_manager.init_app(app)
    # 注册session
    register_session(app)
    # 注册蓝图
    register_blue(app)

    # print(app.url_map)
    print(app.config)
    return app
