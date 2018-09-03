from datetime import timedelta


from flask import Flask
from flask_session import Session
from redis import Redis

from apps.cms import cms_bp
from apps.model import db


def create_app():
    app = Flask(__name__)
    # 加载app 配置文件
    app.config.from_object("apps.settings.DevConfig")
    # 设置session过期时间
    app.permanent_session_lifetime = timedelta(seconds=10)
    Session(app)

    # 初始化 数据库模型
    db.init_app(app)
    # 注册蓝图
    app.register_blueprint(cms_bp)
    # 设置session过期时间

    # print(app.url_map)
    print(app.config)
    return app
