# app通用配置
from redis import Redis


class BaseConfig:
    pass


# 开发配置
class DevConfig(BaseConfig):
    # 调试模式
    DEBUG = True
    # 服务器名称
    SERVER_NAME = 'elm.com:5000'
    # 配置orm 数据库引擎
    SQLALCHEMY_DATABASE_URI = 'sqlite:///H:myDB\\orm.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "ABC"
    SESSION_PERMANENT = False
    SESSION_TYPE = "redis"
    SESSION_REDIS = Redis("127.0.0.1",6379)




# 上线配置
class ProConfig(BaseConfig):
    DEBUG = False
