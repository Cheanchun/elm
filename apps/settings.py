import os
from datetime import timedelta
from redis import Redis

# app通用配置
class BaseConfig:
    pass


# 开发配置
class DevConfig(BaseConfig):
    # 调试模式
    DEBUG = True
    # 服务器名称
    SERVER_NAME = 'elm.com:5000'
    # 配置orm 数据库引擎
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///H:myDB\\orm.sqlite'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}\\orm.sqlite'.format(os.getcwd())
    # print(dirname(os.getcwd()))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "ABC"
    # 设置会话session True 打开,关闭流浪器删除
    SESSION_PERMANENT = False
    SESSION_TYPE = "redis"
    SESSION_REDIS = Redis("127.0.0.1", 6379)
    # 设置session过期时间
    PERMANENT_SESSION_LIFETIME = timedelta(weeks=2)




# 上线配置
class ProConfig(BaseConfig):
    DEBUG = False


