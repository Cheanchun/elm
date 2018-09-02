from flask import Flask
from apps.cms import user_bp
from apps.model import db


def create_app():
    app = Flask(__name__)
    # 加载app 配置文件
    app.config.from_object("apps.settings.DevConfig")
    # 初始化 数据库模型
    db.init_app(app)
    # 注册蓝图
    app.register_blueprint(user_bp)
    print(app.url_map)
    return app
