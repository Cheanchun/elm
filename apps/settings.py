import os
from datetime import timedelta
from redis import Redis

# redis 连接基本配置
# 阿里云 redis
# api_redis = Redis(host="47.105.54.129", port=6388)
# 本地redis
# api_redis = Redis(host="127.0.0.1", port=6388)
# 虚拟机 redis
api_redis = Redis(host="192.168.231.134", port=6388)


# app通用配置
class BaseConfig:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "ABC"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/orm.sqlite'.format(os.getcwd())


# 开发配置
class DevConfig(BaseConfig):
    # 调试模式
    DEBUG = True
    # 服务器名称
    # SERVER_NAME = 'elm.com:5000'
    SESSION_TYPE = "redis"
    SESSION_REDIS = Redis("192.168.231.134", 6388)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 设置会话session True 打开,关闭流浪器删除
    SESSION_PERMANENT = False
    # 设置session过期时间
    PERMANENT_SESSION_LIFETIME = timedelta(weeks=2)


# 上线配置
class ProConfig(BaseConfig):
    DEBUG = False


class ApiConfig(BaseConfig):
    DEBUG = True
    # SERVER_NAME = 'elm.com:8080'
    # 验证码过期时间
    SMS_LIFETIME = timedelta(days=1)
    TOKEN_EXPIRES = 3600
