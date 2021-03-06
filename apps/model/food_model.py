from apps.model import db
from .seller_model import BaseModel


class MenuCategory(BaseModel):
    # 对外ID
    pub_id = db.Column(db.String(16))
    # 分类名称
    name = db.Column(db.String(32))
    # 分类描述
    description = db.Column(db.String(128), default='')
    # 分类编号
    type_accumulation = db.Column(db.String(16))
    # 是否默认
    is_default = db.Column(db.Boolean, default=False)
    # 归属店铺
    shop_pid = db.Column(db.Integer, db.ForeignKey('seller_shop.pub_id'))

    shop = db.relationship('SellerShop', backref='categories')

    def keys(self):
        return "pub_id", "name", "description", "type_accumulation", "is_default"

    def __repr__(self):
        return "<MenuCate {}>".format(self.name)


# 菜品信息
class MenuFood(BaseModel):
    # 对外ID
    goods_id = db.Column(db.String(8))
    # 菜品名称
    goods_name = db.Column(db.String(64))
    # 菜品评分
    rating = db.Column(db.Float, default=5.0)
    # 归属店铺
    shop_pid = db.Column(db.Integer, db.ForeignKey('seller_shop.pub_id'))
    # 归属分类
    category_pid = db.Column(db.Integer, db.ForeignKey('menu_category.pub_id'))
    cates = db.relationship('MenuCategory', backref='foods')  # 添加一条关系
    # 菜品价格
    goods_price = db.Column(db.Float, default=0.0)
    # 菜品描述
    description = db.Column(db.String(128), default='')
    # 月销售额
    month_sales = db.Column(db.Integer, default=0)
    # 评分数量
    rating_count = db.Column(db.Integer, default=0)
    # 提示信息
    tips = db.Column(db.String(128), default='')
    # 菜品图片
    goods_img = db.Column(db.String(128), default='')

    def keys(self):
        return "goods_name", "shop_id", "category_id", "goods_price", "description", "tips", "goods_img"

    def __repr__(self):
        return "<Food: {}-{}>".format(self.food_name, self.food_price)
