from apps.model import db
from flask_login.mixins import UserMixin


# 写model基本类  被继承数据模型和model基本类会组合成一个表
class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def set_attrs(self, attrs):
        for k, v in attrs.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)


# 用户数据表
class User(BaseModel, UserMixin):
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))
    uuid = db.Column(db.String(36))

    def __repr__(self):
        return "<Seller{}>".format(self.username)


# 商品表
class Goods(BaseModel):
    GoodsName = db.Column(db.String(64))
    Brief = db.Column(db.String(64))


# TodoList 表
class TodoList(BaseModel):
    title = db.Column(db.String(64))
    content = db.Column(db.String(255))
    add_time = db.Column(db.String(30))
